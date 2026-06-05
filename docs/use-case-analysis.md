# Use-case analysis — topic map of conversations

**Status:** very early. Methodology to be defined with **PEREN** (Pôle d'Expertise de la Régulation Numérique).
**Related:** personal ranking (`docs/personalised-ranking.md`) · conversation history (`docs/conversation-history.md`)
**Labels:** front, dataset/db

## Mockups

> 🖼️ Drag in `MacBook Pro (6).png` — "Analyse des cas d'usage" on the "L'arène du Louvre" instance.

## Summary

A new section ("Analyse cas d'usage") that visualises *what people actually use the arena for*: conversations embedded and clustered by semantic similarity, plotted as a topic map with named clusters (e.g. "AI Ethics and Impact", "Academic Discussion Topics", "Cooking and Travel Tips", "Code and Scripting Help"…). Two scopes: **Analyse Générale** (all conversations on the instance) and **Mon analyse** (the signed-in user's own conversations).

## Why

- We collect a large volume of real prompts but have no view of the *usage landscape* — which tasks people bring to the arena.
- Useful for operators (per-instance, e.g. a Louvre deployment seeing its visitors' use cases) and for the user themselves (what do I use this for?).
- The methodology — how topics are defined, labelled and made meaningful/robust — is the hard part and will be developed **with PEREN**. This spec only frames the feature, not the method.

## What the mockup shows

- Left nav with a dedicated **"Analyse cas d'usage"** entry.
- Two tabs: **Analyse Générale** and **Mon analyse**.
- A scatter/topic map: each point = a conversation, positioned by semantic similarity (dimensionality-reduced embeddings), coloured by topic cluster, with cluster labels overlaid and a topic legend on the right.
- Interactive plot controls (zoom, pan, select, fullscreen) — looks like a Plotly-style chart.

## Scope / to detail (with PEREN)

- **Methodology** (PEREN): embedding model, clustering approach, how clusters are labelled, how many topics, stability over time, how to validate that clusters are meaningful. *This is the main open work.*
- **Pipeline**: embed conversations → reduce dimensions → cluster → label → serve to the front. Batch/offline vs. live; refresh cadence.
- **General vs. personal scope**: "Mon analyse" needs per-user conversations → depends on Authentication (#11) + conversation history.
- **Privacy & anonymisation**: the general map is built from real user prompts — must respect the same PII handling as data publishing before anything is shown/aggregated.
- **Per-instance**: each deployment ("L'arène du Louvre", etc.) analyses its own conversations.

## Open questions

- What's the minimum data volume for the personal map to be useful (most users have few conversations)?
- Static periodic snapshot vs. on-demand recompute.
- Click a point → open that conversation? Click a cluster → drill into example prompts?
- How much of the methodology is fixed by PEREN vs. configurable per instance.

## Explicitly out of scope (for now)

- The clustering/labelling methodology itself — to be designed with PEREN.
- Any commitment on the charting library or exact topics shown in the mockup (illustrative).
