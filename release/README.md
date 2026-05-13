# Release — Witness

*Dylan Eytan, 2025*

---

## Contents

| File | Description |
|---|---|
| `ARTIST_STATEMENT.md` | 200-300 word artist statement |
| `screenshots/` | 3-5 still frames from a live session |
| `screen-capture.mov` | 60-second screen capture of the system running *(see instructions below)* |
| `session-print.png` | Screenshot of a printed log page from a real session |

---

## How to run for demo

```bash
# 1. Start Ollama
ollama serve

# 2. Start backend
cd ~/witness
python3 server.py

# 3. Open in browser
open http://localhost:8080
```

- Allow camera permission when prompted
- First entry appears after ~15 seconds
- Log visible at http://localhost:8080/log (auto-refreshes every 6s)
- All entries saved to entries.jsonl

---

## Screen capture instructions

To record the 60-second screen capture:
1. Open the app at http://localhost:8080 in full screen (⌘ + Shift + F)
2. Open QuickTime Player → File → New Screen Recording
3. Record for 60 seconds with the system running and writing
4. Export and save to this folder as `screen-capture.mov`

---

## Print instructions

1. Open http://localhost:8080/log after a session
2. Print the page (⌘ + P) → Save as PDF or print to paper
3. Sign and date the bottom of the page
4. This is the physical artifact deliverable

---

## GitHub

https://github.com/deytan29-glitch/witness
