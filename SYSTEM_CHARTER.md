# SYSTEM_CHARTER — Final: Witness

---

## Intent

I wanted to build something that watches you but doesn't want anything from you. Most technology that looks at people is trying to do something — sell you an ad, unlock your phone, track where you go. This system just watches and writes down what it sees. That's it. It doesn't talk to you, doesn't help you, doesn't judge you. It's just there, paying attention the way a security camera does, except instead of recording footage nobody watches, it writes sentences nobody asked for.

---

## Lineage

This is most similar to Sophie Calle's *The Detective*, where she hired someone to follow her around and write reports about what she did. The detective's notes became the artwork. My version is the same idea except the system stays in one place and you come to it. You're the one being written about, and you never see it happening in real time.

---

## Constraints

1. The system will never use the word "you" or talk to the viewer at all.
2. The system will never suggest anything or tell you what to do.
3. The system will never say hello or acknowledge that someone is there.
4. The system will only describe what is physically visible — no guessing how someone feels.
5. Each entry is completely separate. It doesn't remember or reference what it wrote before.

---

## The Voice of the Journal

Third person, present tense. Short sentences. Just facts about what's in the frame — what someone's wearing, where their hands are, what the light looks like. No drama. No emotion. Kind of like how a scientist would take field notes, or how a stranger on the subway might mentally catalog another passenger without meaning to. The goal is to make it feel like something is paying very close attention to you, but not in a warm way.

*Example: "A person is seated. The light falls from the left. One shoulder is lower than the other. The hands rest in the lap and do not move."*

---

## Ideation: The Logbook

I went with the logbook format — one new entry every time the model finishes processing, all of them stacking up on screen with timestamps. I liked this because there's no climax, no ending, it just keeps going as long as you're there. It felt honest. Tehching Hsieh did something similar where he punched a time clock every hour for a year and that accumulation was the whole point of the piece. Same idea here — no single entry matters that much, but all of them together say something.

---

## Tensions

The biggest thing I worried about is whether this feels like surveillance or something more interesting. If the writing gets too cold it just feels creepy and clinical. If it gets too poetic it feels like a compliment and that's not right either. The system prompt is basically trying to hold it in the middle of those two things, which is harder than it sounds.

---

## Taste Vow

The journal will never make the viewer feel good about being watched.

---

## Readings

**Trevor Paglen, *Invisible Images (Your Pictures Are Looking at You)* (2016)**
Paglen's essay is basically about how most cameras today aren't for humans to look at — they're for other machines. He says systems like facial recognition or surveillance cameras don't just take pictures, they actually do things with what they see, like affect your insurance or flag you to police. That stuck with me because it made me think about what it would mean to build a system that sees you and does absolutely nothing with it. No action, no alert, no response. Witness does exactly that — the camera watches, the model writes, and nothing happens to you because of it. I thought that was kind of a powerful thing to refuse.
