# Authentication & access modes (back-office config)

**Milestone:** 🚪 Back-office and arena customisation (#17)
**Related:** 🗝️ Authentication (#11) · brief #477
**Labels:** front, arena

## Mockup

> 📎 Attach `02 _ Users.png` here (left column — Authentication settings).

## Summary

Back-office UI to pick how users access the arena and configure the chosen provider. This is the *configuration surface* for the broader auth work in #11 / #477.

## Scope (to detail later)

- **Access modes:** No authentication · Anonymous + sign-in · Sign-in required (sector-restricted deployments e.g. Compar:IA Santé).
- **OIDC / SSO:** display name, discovery URL, client ID/secret, email-claim mapping, Test connection, optional email-domain allowlist (wildcards).
- **Email one-time code:** depends on SMTP env config (surface "not configured" state).

## Notes

Auth itself is tracked separately (#11, brief #477). This issue is only the back-office config screen — keep auth logic in the auth subject.
