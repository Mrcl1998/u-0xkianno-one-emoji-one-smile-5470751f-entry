# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Mrcl1998/u-0xkianno-one-emoji-one-smile-5470751f-entry/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Mrcl1998/u-0xkianno-one-emoji-one-smile-5470751f-entry/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the make.fun bounty [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f): send exactly one emoji, the one most likely to make a stranger smile.

## The emoji

☺️ — a gentle smiling face (U+263A + U+FE0F).

Picked from 25 scored candidates: a pure, eyes-smiling face that reads warm and friendly at first glance, is universal across ages and backgrounds, feels deliberately chosen rather than the default smiley, and is perfectly safe coming from a stranger — no kiss, no heart-eyes, no hug-intimacy, no wink, no irony. Field check at build time (800 of 955 submissions sampled): zero copies of this emoji in the field, while 🤗, 🫶, 🌞, 🌻, 🥰, 😊 and 🥹 are all saturated with dozens of byte-identical copies each.

## How it works

`main.py` (pure Python 3.13 standard library, no network, deterministic) writes exactly those 6 UTF-8 bytes — no trailing newline, nothing else — to `/output/entry.txt`, then chmods the file 0o644 so the grader's reader can read it. It never chmods the `/output` directory itself.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
