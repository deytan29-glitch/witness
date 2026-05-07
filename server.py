#!/usr/bin/env python3
"""
Witness — backend server
Serves the app, receives journal entries, persists them to entries.jsonl
Routes:
  GET  /          → index.html
  GET  /log       → human-readable log page
  GET  /entries   → raw JSON array of all entries
  POST /entry     → save a new entry { text, timestamp }
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

PORT      = 8080
LOG_FILE  = os.path.join(os.path.dirname(__file__), 'entries.jsonl')
STATIC    = os.path.dirname(__file__)


def load_entries():
    if not os.path.exists(LOG_FILE):
        return []
    entries = []
    with open(LOG_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return entries


def save_entry(entry):
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')


LOG_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Witness — Log</title>
  <link href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&display=swap" rel="stylesheet"/>
  <meta http-equiv="refresh" content="6"/>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      background: #0a0a0a;
      color: #e8e3d6;
      font-family: 'IM Fell English', Georgia, serif;
      font-size: 18px;
      line-height: 1.85;
    }}
    main {{
      max-width: 640px;
      margin: 0 auto;
      padding: 8vh 28px 12vh;
    }}
    h1 {{
      font-size: 12px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #888070;
      margin-bottom: 1.2rem;
      font-style: normal;
    }}
    .entry {{
      margin-bottom: 2.6rem;
      padding-bottom: 2.6rem;
      border-bottom: 1px solid #221f1a;
    }}
    .entry:last-child {{ border-bottom: none; }}
    .entry-time {{
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #8a8170;
      margin-bottom: 0.6rem;
    }}
    .entry-text {{
      font-style: italic;
      color: #f0ebde;
    }}
    .empty {{
      color: #6a6155;
      font-style: italic;
      margin-top: 4vh;
    }}
    .count {{
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #6a6155;
      margin-bottom: 5vh;
    }}
  </style>
</head>
<body>
<main>
  <h1>Witness — Session Log</h1>
  <p class="count">{count} {entry_word}</p>
  {body}
</main>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # quiet server logs
        pass

    def send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        path = self.path.split('?')[0]

        if path == '/' or path == '/index.html':
            self._serve_file('index.html', 'text/html')

        elif path == '/log':
            entries = load_entries()
            if entries:
                rows = '\n'.join(
                    f'<div class="entry">'
                    f'<div class="entry-time">{e.get("timestamp","")}</div>'
                    f'<div class="entry-text">{e.get("text","")}</div>'
                    f'</div>'
                    for e in entries
                )
            else:
                rows = '<p class="empty">No entries yet.</p>'

            count = len(entries)
            word  = 'entry' if count == 1 else 'entries'
            html  = LOG_HTML_TEMPLATE.format(
                count=count, entry_word=word, body=rows
            )
            self._send(200, 'text/html', html.encode())

        elif path == '/entries':
            entries = load_entries()
            self._send(200, 'application/json', json.dumps(entries).encode())

        else:
            # Try to serve static file
            filepath = os.path.join(STATIC, path.lstrip('/'))
            if os.path.isfile(filepath):
                self._serve_file(path.lstrip('/'), 'text/plain')
            else:
                self._send(404, 'text/plain', b'Not found')

    def do_POST(self):
        if self.path == '/entry':
            length  = int(self.headers.get('Content-Length', 0))
            body    = self.rfile.read(length)
            try:
                data = json.loads(body)
                entry = {
                    'text':      data.get('text', '').strip(),
                    'timestamp': data.get('timestamp', datetime.now().isoformat())
                }
                if entry['text']:
                    save_entry(entry)
                    print(f"[{entry['timestamp']}] {entry['text'][:80]}")
                self._send(200, 'application/json', b'{"ok":true}')
            except Exception as e:
                self._send(400, 'application/json',
                           json.dumps({'error': str(e)}).encode())
        else:
            self._send(404, 'text/plain', b'Not found')

    def _serve_file(self, filename, mime):
        filepath = os.path.join(STATIC, filename)
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            self._send(200, mime, data)
        except FileNotFoundError:
            self._send(404, 'text/plain', b'Not found')

    def _send(self, code, mime, data):
        self.send_response(code)
        self.send_header('Content-Type', mime)
        self.send_cors()
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    server = HTTPServer(('localhost', PORT), Handler)
    print(f"Witness running at http://localhost:{PORT}")
    print(f"Log page:         http://localhost:{PORT}/log")
    print(f"Raw entries:      http://localhost:{PORT}/entries")
    print(f"Log file:         {LOG_FILE}")
    server.serve_forever()
