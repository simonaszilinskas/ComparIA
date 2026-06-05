# Models management + move models to the DB

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Related:** no dedicated milestone yet — this is also the home for the models JSON → DB migration.
**Labels:** front, arena, models

## Mockup

> 📎 Attach `03 _ Content _ Models.png` here.

## Summary

Manage the model catalog from the back-office: list, search, filter by status, add, and archive. Archiving removes a model from arena rotation but keeps its historical votes.

## Scope (to detail later)

- Searchable, status-filterable models table (Available / Archived).
- Add model + archive action.
- **Foundational: move models out of `models.json` into the DB** so they can be edited at runtime per instance instead of shipped in code.

## Notes

The JSON → DB migration is the bulk of the work and may become its own issue once scoped. Touches the model catalog used by arena, ranking, and `modeles` pages.
