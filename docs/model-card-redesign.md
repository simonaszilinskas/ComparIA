# Structured model card redesign

## Summary

Redesign the model detail card (opened from `/modeles`) into a structured, scannable layout that groups everything we know about a model into clear sections, with tooltips and color-coding. Replaces the current free-text card with a consistent template applied to every model.

> 🎥 Attach `nouvelles-cartes.mp4` (or key screenshots) here. The recording walks through the `/modeles` list and the new card for EuroLLM 22B Instruct and Gemma 4 26B A4B.

## Why

- The current card is largely prose; comparable facts (licence, params, context, openness) aren't presented consistently across models.
- A structured template makes models comparable at a glance and surfaces the sovereignty / environmental / ranking data we already collect.

## The card sections

Opened as a modal over `/modeles` (header: logo, `Vendor / Model name`, release date e.g. `SORTIE 04/2026`, Fermer ×).

1. **Caractéristiques techniques** — parameter count (+ active params for MoE), context window (tokens + approx. characters), architecture (Dense / MoE "Mélange d'experts"), input modalities (text / image / audio / video icons), knowledge cutoff.
2. **Ouverture et souveraineté** — openness badge (`SEMI-OUVERT` / `PROPRIÉTAIRE`), licence, model weights (public/private), output reuse, commercial use, training datasets, training code, editor country of origin (flag), EU-hostable. Values color-coded green (open/permissive) / red (closed/restricted).
3. **Impact environnemental** — required hardware tier (smartphone → laptop → workstation → server), A–F energy consumption class label, qualitative tags (e.g. "mélange d'experts", "modèle compact").
4. **Performances au classement** — performance tier (I–V), overall rank (`#20 sur 47 modèles`), Bradley-Terry score (± confidence), votes recorded.
5. **Plus d'informations et sources** — links: Hugging Face, fiche modèle, EcoLogits, site officiel, Artificial Analysis, Impact CO₂.

Every metric has a `?` tooltip explaining it.

## List page

The `/modeles` cards also get refreshed badges: openness (`PROPRIÉTAIRE` / `SEMI-OUVERT`), release date, estimated size.

## Scope / open questions (to detail)

- Which fields are required vs. optional, and the fallback when data is missing.
- Source of truth for each field (ties into moving the model catalog out of `models.json` into the DB — see `docs/back-office/05-models.md`).
- Tooltip copy + i18n (FR/EN).
- Mobile layout of the modal.

## Status

Prototype in progress on branch `experimental/structured-model-card`.
