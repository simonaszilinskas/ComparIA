# Conversation history (logged-in users)

**Related:** 🗝️ Authentication (#11, brief #477) · personal ranking (`docs/personalised-ranking.md`)
**Labels:** front

## Mockups

> 🖼️ Drag in:
> - Logged-in sidebar with history (`MacBook Pro 12.png`)
> - Non-logged-in state (`MacBook Pro 10.png`)

## Summary

Persist each conversation a signed-in user has in the arena and list them in the left sidebar under **Conversations**, so the user can reopen a past comparison. **Scope: logged-in users only for now** — anonymous users see a prompt to sign in instead of a history.

## Why

- Today a conversation is lost on reload — there's no way back to a past comparison.
- It gives signed-in accounts lasting value and is the natural home for revisiting votes/results.
- Shares the same "you need to know who the user is" foundation as personal ranking.

## Logged-in behaviour

- **Sidebar list** under "Conversations": past conversations, most recent first, each as a clickable row with a truncated title.
- **Two model icons per row** showing which models were compared. Before the models are revealed (i.e. before the user votes), the icons are masked (shown as `?` / `?`) so identity stays hidden until reveal — matching the blind-comparison rule.
- **Open a conversation** restores its full state (messages, and post-vote the revealed models + energy/CO₂ results, as in the revealed view).
- **New conversation** starts a fresh one (button top-left / top-right).

## Non-logged-in behaviour

- The Conversations section shows "Sign in to access your conversation history" with a **Sign in** button. No history is stored or listed.

## Scope / to detail

- **Persistence model** — store conversations + messages per user (DB), including which two models, vote/reaction, and the computed environmental results.
- **Title generation** — auto-title from the first user message? Truncation rules.
- **Reveal state in the list** — exactly when masked icons flip to real logos (on vote / on reveal).
- **Empty state** for a signed-in user with no conversations yet.

## Open questions

- **Depends on Authentication (#11)** — requires user accounts to attach conversations to.
- Rename / delete a conversation? (out of scope for v1?)
- Retention limits (how many / how long kept).
- Do anonymous (pre-sign-in) conversations get migrated to the account on first sign-in, or are they dropped? 
- Search within history (the list could grow long).
