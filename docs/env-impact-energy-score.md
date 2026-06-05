# Env. impact — per-prompt energy estimate + A–F energy class

**Milestone:** 🪴 Env. impact estimation improvements (#16)
**Related:** #376 (concerns on "this corresponds to") · #375 (translation/release timing) · model card redesign (#14, `docs/model-card-redesign.md`) — shares the A–F energy class
**Labels:** front, arena

## Mockups

> 🖼️ Drag in here:
> - Energy class label (`Classe de consommation énergétique`, A–F) — Image #6
> - (to add) the post-conversation results panel showing the per-prompt estimate + the two-model comparison

## Summary

Rework the environmental indicators shown after a conversation so the link between **this prompt** and **its impact** is clear again. Two complementary readings:

1. **A concrete per-prompt estimate** — the energy (and CO₂) actually consumed by *this* exchange, shown directly, not only as a collective projection.
2. **An A–F energy class** (EU appliance-label style, "Classe de consommation énergétique") that places the model on a simple, recognisable efficiency scale, derived from the EcoLogits numbers we already have.

The collective projection ("if 48% of French people ran this prompt…") can stay as a secondary, framing layer — but it stops being the headline number.

## Why

- The EcoLogits methodology update (Nov 2025) cut per-request energy estimates by ~1–2 orders of magnitude (e.g. Mistral Small 3.2 / 400 tokens: 1.43 Wh → 0.022 Wh). Per-prompt numbers became tiny, so the product switched to a population-scale projection.
- That switch drew complaints (#376): users read "641 mWh → 10 tonnes CO₂" and the prompt↔emissions relationship is lost; the population multiplier feels arbitrary and location-dependent (a DK vs FR query shouldn't differ just from the multiplier).
- Danish partners (Digitaliseringsstyrelsen / Aarhus) explicitly asked for: (a) the **relational** comparison between the two models ("Model A uses 3.4× Model B"), and (b) the **single-prompt cost**, instead of or alongside the population projection.
- An A–F class keeps a strong, intuitive signal (the real point: model choice matters, small models are often enough) without depending on the shaky absolute equivalences.

## What to show (post-conversation, to detail)

- **Per-prompt estimate**: energy (mWh/Wh) and CO₂ for this conversation, per model. Honest units, with a tooltip on how it's computed (EcoLogits, tokens incl. reasoning tokens).
- **A–F energy class** per model: a labelled bar (A best → F worst) with the model's letter highlighted, like the mockup. Same component reused on the model card (#14).
- **Two-model comparison**: make the relational gap explicit ("Model A ≈ 3.4× the energy of Model B") since blind comparison of two models is the arena's core strength.
- **Collective projection** demoted to secondary/optional framing, clearly labelled as an illustrative scaling, not a per-user cost.

## Scope / open questions

- **How is the A–F class computed?** Absolute thresholds (fixed Wh bands) vs. relative ranking across the catalogue (like AI Energy Score's recalibrated star tiers). Per-task vs. one overall class. Stability when EcoLogits or the model set changes.
- **Source of the per-model energy figure** — ties into moving the model catalogue out of `models.json` into the DB (`docs/back-office/05-models.md`); the class is a model attribute.
- **Reasoning tokens** — confirm they're counted in the per-prompt estimate (partner question); consider surfacing average "reasoning intensity" per model later.
- **Keep or drop the population projection** — and if kept, how to frame the multiplier so it doesn't read as a per-user cost or a country-specific result (#376).
- **i18n / release timing** — env-impact copy must ship with translations so non-FR instances don't show stale/English strings (#375).
- Empty/low-confidence states; mobile layout of the results panel.

## Explicitly out of scope (for now)

- Re-deriving the underlying EcoLogits methodology — we consume their numbers.
- Committing to the exact A–F threshold values (illustrative until decided).
