# Artist Statement — Witness

*Dylan Eytan, 2025*

---

A camera watches. A language model writes. Nobody is told what it's writing.

Witness is a system that pairs a webcam with a local vision model and produces a running log of what the model notices about whoever sits in front of it. The log builds up the whole time you're there. The system never talks to you. It doesn't say hello, doesn't respond to anything you do, doesn't give you feedback. It just keeps writing entries about you, timestamped, one after another.

The thing that interested me most about building this was figuring out what to make it refuse to do. Language models want to be helpful — they want to answer you, assist you, engage with you. I had to write a prompt that stripped all of that out. No second person. No recommendations. No acknowledgment that anyone is even there. What the system won't do ended up feeling more important than what it does.

The piece is closest to Sophie Calle's *The Detective*, where she hired a private investigator to follow her around Paris and the detective's report became the artwork. My version is simpler — the system doesn't move, you come to it — but the basic idea is the same. Someone is being written about without knowing exactly what's being said.

I also kept thinking about Trevor Paglen's writing on machine vision. His point is that most systems that see you do something with what they see — sell you something, flag you, categorize you. This one doesn't. It just writes. I'm not sure that makes it innocent exactly, but it felt like a different kind of thing to build.

---

*Runs locally on a MacBook. Model: llava:7b via Ollama. No data leaves the machine.*
