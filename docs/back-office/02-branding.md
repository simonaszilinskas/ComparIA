# Branding configuration

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Labels:** front, arena

## Mockup

> 📎 Attach `01 _ Branding.png` here.

## Summary

Let an arena operator configure the visual identity of their instance from the back-office, applied across light and dark themes.

## Scope (to detail later)

- **Identity:** platform name (header/tab/footer), logo upload (PNG/SVG, ~64×64, falls back to name).
- **Colors:** primary + secondary, separate light/dark hex values.
- **Typography:** primary (display/headings) + secondary (body) fonts.
- **Other:** homepage URL (logo destination), markdown welcome message on the arena landing.

## Foundational dependency

Needs a per-instance config store (where branding lives) — likely the same DB-backed instance-config introduced for the other back-office areas.
