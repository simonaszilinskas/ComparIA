# Personal ranking — your own leaderboard from your own votes

**Milestone:** 🏆 Ranking 2.0 + mapping usages (#10)
**Related:** #483 (switching ranking to tiers) · 🗝️ Authentication (#11, brief #477)
**Labels:** ranking, front

## Mockups

> 🖼️ Drag the two mockups in here:
> - General view (`MacBook Pro.png`)
> - Personal view (`MacBook Pro-1.png`)

## Summary

Add a **General ⟷ Personal** toggle to the Leaderboard page. *General* is today's global ranking (all votes since launch); *Personal* re-runs the same ranking on **only the signed-in user's own votes**, so they see which models came out on top *for them*.

The two views share the exact same table and columns — only the data and the score-bar accent color change (blue for general, amber for personal), plus an intro line ("…based only on your own votes. Keep comparing and voting to refine your results over time!") and the totals (e.g. 1 344 personal votes vs 310 406 global).

## Why

- Every user has a different sense of what a good answer is; the global ranking averages that away. A personal ranking reflects an individual's own taste.
- It makes the user's accumulated voting feel worthwhile — their votes produce something they can come back to.
- Natural complement to the global Ranking 2.0 work: same scoring, scoped to one person's votes.

## Idea / scope (to detail)

- **General / Personal toggle** on the Leaderboard page (see mockups), reusing the existing table, columns, search, sort, pagination and Download data.
- **Compute a ranking from a single user's votes** — same method as the global ranking (Bradley-Terry / satisfaction score), restricted to that user's battles. Per-user totals shown in the summary bar.
- **Visual distinction** — amber score bars + the "based only on your own votes" intro copy so it's never mistaken for the official ranking.
- **Low-data handling** — most users will have few votes. Decide minimum votes before the Personal tab is meaningful/shown, how to present low-confidence results, and the empty state for users who haven't voted yet.

## Open questions

- **Depends on identifying the user.** Personal rankings require knowing whose votes are whose → ties to Authentication (#11). For anonymous users, is it session-scoped, or only available once signed in?
- How does this interact with the tiered ranking from #483 — personal tiers, or a personal ordering within the global tiers?
- Privacy: a personal ranking is derived from personal data — confirm it stays private to the user.
