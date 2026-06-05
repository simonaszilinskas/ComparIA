# Back-office shell & navigation

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Labels:** front, arena
**Depends on / blocks:** foundational — the other back-office issues live inside this shell.

## Mockup

> 📎 Optional: attach a crop of the top nav (visible in any of the mockups). The header shows `Platform name` + logo on the left and `Branding · Users · Content` tabs on the right.

## Summary

The admin layout that wraps all back-office screens: top navigation (Branding / Users / Content), routing, and access control deciding who can reach the panel.

## Scope (to detail later)

- Admin route + layout, top-level nav (Branding / Users / Content) and the Content sub-tabs.
- Access control: who can open the back-office (admin role).
- Save / Discard pattern shared across config screens.

## Notes

Access control ties into Authentication (#11) — admin gating depends on having real users/roles.
