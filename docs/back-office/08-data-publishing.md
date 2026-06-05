# Data publishing pipeline config + move pipeline config to the DB

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Related:** no dedicated milestone yet — also the home for making the export pipeline config-driven.
**Labels:** front, arena, dataset/db

## Mockup

> 📎 Attach `06 _ Content _ Data publishing.png` here.

## Summary

Configure where collected preference data is exported, on what schedule, and how it's anonymised before publication.

## Scope (to detail later)

- **Destinations** (multiple): Hugging Face (API key, repo ID) and S3-compatible bucket (keys, endpoint, region), each with Test connection.
- **Schedule:** publishing frequency + next-run display.
- **Anonymisation:** optional PII screening that runs a configured model over each record and holds flagged ones back; "off" publishes raw.

## Foundational dependency

Make the export pipeline driven by DB-stored config instead of hardcoded destinations/credentials. The PII-screening model is selected from the models configured in the Models tab (depends on `05-models.md`).
