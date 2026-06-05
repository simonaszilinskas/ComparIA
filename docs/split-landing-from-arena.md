# Split landing/informational site out of the arena repo

## Summary

Move the informational/marketing site into its own repository, separate from the arena application. The two products would share a brand and cross-link via environment-variable URLs, but not a codebase.

## Why

- **Multi-tenancy is the real driver.** We already run multiple arenas (FR `comparia.beta.gouv.fr`, DK `ai-arenaen.dk`) and expect more. Each operator wants its own landing page — its own copy, partners, news, legal pages — over the *same* arena engine. Today that requires forking the whole monorepo and touching arena code to change marketing copy.
- **Keep a content/CMS layer out of the arena.** Landing content is editorial and will likely need non-dev editing (comms teams, per country). We don't want a CMS — or its content model, build, and deploy concerns — living inside the arena's runtime repo.
- **Independent deploys.** The arena is a dynamic app (FastAPI backend, streaming, model pipeline). The landing site is largely static. They have different release cadences, hosting needs, and uptime profiles.

## Current state

Single SvelteKit app. Relevant seam already exists:

- Informational routes under `src/routes/(pages)/`: `/` (home), `product/*`, `news/*`, `datasets`, `duel`, legal pages under `(general)/*`.
- Arena under `src/routes/arene/`.
- Data-driven pages that *look* informational but depend on the live model catalog / ELO: `ranking`, `modeles`, `modalites`.
- Shared `$lib`: DSFR wrappers, `Footer`, `header`, `ModelCard`, `SEOHead`, i18n, helpers.
- No CMS today — landing content is hardcoded Svelte (`product/[tab]/components/*`, `news/*`).

## Proposed boundary

Split on the **data boundary**, not the "landing vs app" label.

**Portal repo (static, no backend):** `/` home, `product/*`, `news/*`, `datasets`, `duel`, legal pages. Env var `PUBLIC_ARENA_URL`.

**Arena repo (stays here):** `arene/*`, plus `ranking`, `modeles`, `modalites` — these read live model data and belong with the engine. FastAPI backend, model pipeline, runtime API. Env var `PUBLIC_PORTAL_URL`.

## Open questions / decisions needed

1. **Portal stack: static site vs real CMS.** Who edits landing content? If non-devs per country → content layer/CMS; if dev-edited → static SvelteKit/Astro is enough. This decision drives everything else.
2. **TOS handoff.** Home currently gates entry with a TOS checkbox then redirects to `/arene/?cgu_acceptees` (`src/routes/(pages)/+page.svelte`), sharing a `localStorage` flag. Cross-domain, this needs an explicit contract.
3. **Shared UI duplication.** Portal will need its own copies of DSFR wrappers, `Footer`, `header`, i18n setup, `SEOHead`. Prior decision: duplication is acceptable, no shared package. Confirm that still holds.
4. **i18n / per-locale content** ownership across the two repos.
5. **Hosting + DNS** for the new portal repo and cross-link env wiring.

## Out of scope

- Choosing/standing up a specific CMS (tracked separately once decision #1 is made).
- Any change to arena runtime behavior.
