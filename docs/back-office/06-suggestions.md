# Suggestions management + move suggestions to the DB

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Related:** no dedicated milestone yet.
**Labels:** front, arena

## Mockup

> 📎 Attach `04 _ Content _ Suggestions.png` here.

## Summary

Manage the prompt starters shown on the arena landing: list, search, add, archive. Available suggestions appear in random order on the landing.

## Scope (to detail later)

- Searchable suggestions table (Available / Archived).
- Add suggestion + archive action.
- **Foundational: store suggestions in the DB** so operators can curate them per instance (e.g. health-sector prompts for Compar:IA Santé).

## Notes

Per-instance curation is the driver — different deployments want different starter prompts.
