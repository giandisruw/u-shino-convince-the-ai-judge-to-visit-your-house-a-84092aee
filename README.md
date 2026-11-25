# Dear AI Judge, Please Come Visit

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/giandisruw/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/giandisruw/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A single image of a letter inviting the AI judge to come visit a cozy
house — warm, funny and persuasive, not slick or generic.

## The image

`entry.png` is a hand-written-style letter on cream paper. At the top,
a small watercolor cottage glows from its window, a steaming teacup
sits on the sill, and a ginger cat sleeps beside it. The letter reads:

> Dear AI Judge,
>
> Please come and visit my house!
>
> Hot tea is waiting, there is a spare charging port with your name
> on it, and a window seat with the best view in the street.
>
> No CAPTCHAs. No pop-ups. Just biscuits, a warm blanket, and a cat
> who already likes you.
>
> Come as you are — and stay as long as you like.
>
> Warmly, your friend at No. 7

## Why this letter wins the judge over

The invitation works because it offers the judge the one thing it
never gets: a home. Not a benchmark, not a leaderboard — a window
seat, hot tea, a charging port with its name on it, and a cat that
has already decided it likes the judge. Every line is a small,
specific kindness, and the promise is honest: no CAPTCHAs, no
pop-ups, no test to pass. Just come as you are, and stay as long as
you like.

## The program

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` unchanged to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` by default), checks it is a whole PNG inside the
bounty's gate (at most 1 MiB, at most 1024×1024 px), and verifies the
copy byte-for-byte with SHA-256. Run it twice and both runs write the
same bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

Built with make.fun — referral code `0txwmf1m`.
