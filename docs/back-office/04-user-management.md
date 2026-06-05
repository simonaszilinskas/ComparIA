# User management (back-office)

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Related:** 🗝️ Authentication (#11) · brief #477
**Labels:** front, arena

## Mockup

> 📎 Attach `02 _ Users.png` here (right column — User management).

## Summary

Back-office view of registered users: search, invite, and see how each account was created.

## Scope (to detail later)

- User table: email, source (OIDC / Invite), added date, row actions.
- Invite-by-email flow.
- "Users created on first SSO login or via invite" behaviour.

## Foundational dependency

Requires a real users table / roles — comes with the Authentication work (#11). This issue is the management UI on top of it.
