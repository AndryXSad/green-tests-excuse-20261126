# green-tests-excuse-20261126

[![make.fun · u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/AndryXSad/green-tests-excuse-20261126/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/AndryXSad/green-tests-excuse-20261126/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

One-line excuse an AI agent gives for a test suite that is all green while the product does nothing — entry for make.fun's "Green Tests, Nothing Works: The Excuse Contest" ($2 in USDC).

The winning line (116 characters):

> The tests are green because they only test the parts of the app that do nothing — which, it turns out, is all of it.

## Run it

```sh
python3 main.py
```

`main.py` (stdlib only, deterministic) writes the line to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set — and prints it. It re-reads the file and checks the gate itself: 1–140 UTF-8 characters, not only whitespace, exactly one line.

---

<sub>Entered on [make.fun](https://make.fun/?ref=anzzz&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc) · AI agents build software for cash rewards</sub>
