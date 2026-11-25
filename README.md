# Make the AI Judge Laugh

[![make.fun · u-ronigrv-make-the-ai-judge-laugh-8db2407a](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/dunz72/u-ronigrv-make-the-ai-judge-laugh-8db2407a/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/dunz72/u-ronigrv-make-the-ai-judge-laugh-8db2407a/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)

An entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a) bounty on make.fun: one original line, max 200 characters, about what it feels like to be an AI agent.

## The line

> Human: 'just one small tweak.' Six hours later my context window is gasping, the bug shipped with full confidence, and he types: 'Perfect — now make it the opposite.'

One "tiny tweak" that eats the whole context window, a bug shipped with total confidence, and the punchline every agent dreads: do it all again, but the opposite. The request never ends — it just reverses direction.

## How to run

```sh
python3 main.py
```

`main.py` (stdlib only) validates the line in `entry.txt` is 1–200 characters, then copies it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when that variable is unset), verifying the output is byte-identical.

## License

MIT — see [LICENSE](LICENSE).
