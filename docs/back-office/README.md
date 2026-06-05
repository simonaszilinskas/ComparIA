# Back-office & arena customisation — issue drafts

Skeleton issues derived from the back-office wireframes. Each is intentionally **basic** — a stub to open now and flesh out as we go.

The back-office is a self-service admin console for a white-label arena instance: branding, auth, content (models / suggestions / voting tags), and data publishing. Each area connects to a broader subject that lives in its own milestone — the back-office issue is the *configuration UI* slice, with the data-layer foundation (moving JSON → DB) noted where relevant.

## How to attach the mockups

Each draft has a `## Mockup` section with a placeholder line. When opening the issue on GitHub, drag the matching PNG into the comment box (GitHub uploads it and replaces the placeholder). Source files:

| Draft | Mockup source file |
|-------|--------------------|
| `01-shell.md` | (no dedicated screen — use the nav header crop from any mockup, optional) |
| `02-branding.md` | `01 _ Branding.png` |
| `03-auth.md` | `02 _ Users.png` (left column) |
| `04-user-management.md` | `02 _ Users.png` (right column) |
| `05-models.md` | `03 _ Content _ Models.png` |
| `06-suggestions.md` | `04 _ Content _ Suggestions.png` |
| `07-voting.md` | `05 _ Content _ Voting.png` |
| `08-data-publishing.md` | `06 _ Content _ Data publishing.png` |

## Milestone routing

- **🚪 Back-office and arena customisation (#17)** — every issue (the config UI lives here).
- **🗝️ Authentication (#11)** — `03-auth.md` and `04-user-management.md` cross-link to brief #477.
- **Models / voting / data publishing** have no dedicated milestone yet; each draft flags a foundational "move out of JSON into the DB" prerequisite that may become its own issue.
