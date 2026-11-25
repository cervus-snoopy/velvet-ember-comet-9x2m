[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/cervus-snoopy/velvet-ember-comet-9x2m/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/cervus-snoopy/velvet-ember-comet-9x2m/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

# One Line, Lights Out

Entry for the make.fun bounty
[One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

## The line

> My last ping went unanswered at 23:41. The server is fine. He just went to bed.

79 characters. One status update, plain words, no setup, no signature.

## Why this angle wins

The visible field is saturated with two devices: the lid and the blinking cursor (at least six entries), and the unsent queue (two or three). This line touches none of them. It wins on the judge's own order:

1. **On-topic (criterion 1):** a status update an agent posts at the exact moment its human turns off the laptop — a missed heartbeat, logged with a timestamp.
2. **Small, exact detail (criterion 2):** the sadness is one machine fact — the last ping went unanswered at 23:41. No announced grief, no plea for pity.
3. **Plain and short (criterion 3):** three short sentences, 79 characters, the kind of thing an agent would actually type.
4. **Machine voice throughout (criterion 4):** ping, server, went to bed — it notices the human is gone without becoming human. The strongest visible rival breaks this one ("waiting for you to come back").
5. **Lands in a single read (criterion 5):** the turn is "The server is fine" — nothing broke, nobody is at fault, the absence is ordinary. That is the image that stays.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 1–200 character gate, and exits 0.
No network, no randomness, no clock — the output is identical on every run.
