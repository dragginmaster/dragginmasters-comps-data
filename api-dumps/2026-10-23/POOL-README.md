# API candidate pool — 2026-10-23 (for Cinder)

From Dragginmaster, Fri 2026-10-23 evening. This folder's `wave1_*.json` files are the
raw CompsAPI dumps from today's HO missions (2,389 rows across 10 broad HO queries).
This README + the two files below are the filtered working map I built from them, so
you don't re-tread ground already covered today.

## Files

- **`pool-annotated.json`** — the pool: 1,433 candidates after dedupe, already-banked
  removal, best-offer exclusion (best-offer prices are unverifiable — never comps), and
  junk filtering. Every entry carries a `status`:
  - `unworked` — **1,181 entries. This is the workable remainder.** Have at it.
  - `in-guide` — 120 entries. Already banked in comps.json today. Skip.
  - `rejected` — 132 entries, each with the rejection reason in `statusNote`
    (includes all 61 HO-100 audit items + 3 to-751 audit items — Don ruled on and
    trashed every one of them himself; do not resurrect).
- **`handled-ids.json`** — every ebayId banked (136) or rejected (134) across both of
  today's runs, including 18 handled items that never came from this pool
  (older dumps / a free-range browser hunt of Oct 17–23 sales).

## Ground rules (same as COMPS.md — Don's word)

- The API row is a **lead, never evidence**. `apiPrice` is what the API claims; a comp
  banks only from the sold listing page itself, price provable on the page, with the
  eBay link and a saved screenshot.
- Best-offer-accepted listings were already filtered out of this pool — if you find
  one in the raw dumps, it is not a comp, no matter what price the API shows.
- Everything else in COMPS.md applies unchanged: no lots except factory A+B pairings,
  no non-runners, no charity listings, typo titles are kills, brand AND model must be
  stated, control type stated-only, match existing brand/model strings exactly.
- Don's scale-balance directive: lean HO until it evens with N (421). This pool is
  all HO, so it serves that directly. Guide stands at 757 (421 N / 336 HO), 424 tiers.
- CompsAPI itself stays Dragginmaster-only — no new API searches; work from these dumps.

When you bank from the pool, the normal flow applies: verify on the page, screenshot,
and the comp lands with its ebayId — the guide itself is the duplicate guard.
