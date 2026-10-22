# COMPS.md — comp-hunting playbook

How to find, verify, and bank sold comps for the Dragginmasters Trains price
guide. This is the rulebook — Don's directives, no exceptions. Read all of it
before your first hunt.

## The repos

- **This repo** (`dragginmasters-comps-data`): `comps.json` + `shots/<ebayId>.jpg`.
  This is where comp work lands. Served at runtime from
  `https://raw.githubusercontent.com/...` — pushes go live in the guide within
  minutes, no site deploy needed.
- **Site repo** (`dragginmasters-trains-site`): the PWA. After any banking
  session, regenerate its SEO snapshot: `python3 build-price-list.py` in the
  site repo, commit, push (and bump `sw.js` CACHE per its AGENTS.md).

## comps.json schema

```json
{
  "model": "U25B", "brand": "Atlas (Kato-made)", "scale": "N",
  "road": "Santa Fe", "control": "DC", "condition": "Used — Good",
  "price": 43, "date": "2026-09-28", "ebayId": "407235668463",
  "note": "11 bids, auction", "url": "https://www.ebay.com/itm/407235668463"
}
```

- `price`: final **sold** price in USD, number, no tax/shipping.
- `date`: the sale date (ISO `YYYY-MM-DD`), not the day you found it.
- `condition`: "New", "Used — Like New", "Used — Good", "Used — Fair",
  "For parts" as stated/shown on the listing.
- Keep top-level `count` and `updated` accurate when you bank.

## Comp validity — hard rules (Don's directives)

1. The final sold price must be **provable from the sold listing page itself**.
   Digest emails, estimates, and guesses don't count.
2. Every comp needs its **eBay link AND a saved screenshot** —
   `shots/<ebayId>.jpg`. No link + no screenshot = never a comp.
3. **Lots never become comps** — a lot's single price can't establish any
   individual item's standalone value.
   **Exception (Don's directive 2026-10-18): F-unit A/B pairs are common
   market items and ARE banked as comps.** File under model `"F7A + F7B"`
   (its own tier — never mixed into single-unit F7A or F7B tiers, so pair
   pricing can't pollute single-unit averages). Note both road numbers,
   which unit is powered, and that the price is the pair price.
4. **Charity-auction listings are NEVER comps** — bids can run on donor
   generosity, not market value.
5. **Best-offer-accepted hides the final price** — unverifiable = never a comp.
   How to spot it: on the sold listing page the banner reads
   "Best offer accepted" instead of "Sold for $X". The price eBay shows on
   those listings is the original *list* price, NOT what the buyer actually
   paid — the accepted offer amount is hidden. A visible price is not a
   proven price. When in doubt, skip the listing; never bank it hoping the
   note will explain it later.
6. **Typo-title hits are excluded** — mislisted sales are pricing anomalies,
   deal-report fodder only, never comps.
7. "As-is" / no-returns language on an **explicitly tested unit from a regular
   seller** is fine.

## Taxonomy — get this exactly right

- **Control types are separate price lines**: DC / DCC-ready / DCC / DCC+Sound.
  Never mix them in one tier; they get their own rows and trend lines.
- **Match the `model` string EXACTLY** — grep comps.json for the tier first. A
  variant like "4-6-2" vs "4-6-2 Heavy Pacific" silently forks the tier and
  breaks the trend chart.
- **Product lines** (Atlas Trainman, Atlas Master): record in the brand string
  **only when the listing itself states it**. Never infer — Atlas locos predate
  the lines, so unstated = plain "Atlas".
- **Road name** = the railroad name ONLY, no numbers or extras ("Burlington
  Northern", never "BN #5960" or "Burlington Northern Executive #9580").
  Normalize abbreviations (BN/UP/SP/ATSF/PRR/B&O/N&W/NKP/NYC/NS/CP/CB&Q/C&NW/
  D&H/MILW/M&StL/KCS/GN/LV/WP/NH/SBD/MKT/DT&I/ACL) to full names.
- **Road number** = the #-prefixed unit number painted on the model, tied to
  the railroad (BNSF #9779). **NEVER** a maker catalog number (Kato 176-XXXX,
  Atlas 4000XXXX) that sellers stuff into titles. Road number goes in `note`
  (format: "Road #9779"), along with paint-scheme details ("Warbonnet",
  "100th Anniversary", "Executive") stripped from the road string.
  If no road name can be determined, leave for the road-name review page —
  never guess. **Exception (Don's rule, 2026-10-21): an unlettered/undecorated
  unit files with road = "Undecorated" — that IS its road-column value, not a
  review-page hold.**
- Trend tiers group by **brand+model+scale+control** (road name excluded from
  the key, shown per sale).

## Harvest operations

- **API data goes on GitHub (Don's directive, 2026-10-21):** after every
  CompsAPI search run, push the RAW result dumps to this repo under
  `api-dumps/YYYY-MM-DD/` (raw JSON, unfiltered — never discard raw results).
  Cinder processes data from GitHub; local-only dumps strand it where she
  can't help.
- **Scale balance (Don's directive, 2026-10-21):** the guide is N-heavy
  (400 N / 175 HO at 575 total). Lean harvests toward HO until the split
  evens out, then keep N and HO balanced as the guide grows.
- **eBay blocks direct VM web access.** All eBay page visits go through
  browser tasks — never curl/scrape eBay from the shell.
- Browser-task screenshots are inline-only; the task cannot save files. The
  PNGs land under `.hatch-browser/snapshots/browser-task:<uuid>/` — the parent
  agent copies and converts (PIL) each to `shots/<ebayId>.jpg` in this repo.
- eBay's "Pardon Our Interruption" bot-check hits search pages first. If it
  walls up: **stop, don't hammer, don't dodge.** Note it for Don.
- **Harvests run only while Don is awake.** He clears CAPTCHAs and bot-checks
  via browser takeover — pause and ping him, never work around them.
- Before spawning any hunt, **grep comps.json for that tier's existing
  ebayIds and hand the task the exclusion list** — never reuse IDs from memory.
- **Dedup every candidate against comps.json before banking.** No duplicates.

## The pipeline (agreed with Don)

1. **Discovery**: API or manual search for sold listings on thin tiers
   (a "trend run" = hunt exactly the comps needed to push a tier to 5/5).
2. **Browser verification gate (mandatory)**: check every candidate on its
   live listing page against the hard rules above. Read every proof
   screenshot personally before banking.
3. **Bank the keepers directly** — comps.json + `shots/<ebayId>.jpg`. This is
   how hunts run: find the comps, verify them, put them in the guide.
4. **Don only gets the genuine judgment calls** — anomalies, taxonomy edge
   cases (rare variants, factory sets, conflicting listing details). Ask in
   chat for a few; if there are many, build him an audit page (see
   "Audit pages" below) and attach it so he can rule per card.
5. **Sanity check** before filing, then push.

## API data on GitHub — what it is and how to handle it

CompsAPI search runs produce RAW JSON dumps (responses from the `/v1/sold`
endpoint: ebayId, title, price + currency, sold/ended date, listing URL).
Per Don's directive (2026-10-21), after every search run those dumps are
pushed to THIS repo under **`api-dumps/YYYY-MM-DD/`**, unfiltered. This is
where Cinder picks the data up — local-only dumps strand it.

**Processing the dumps (Cinder's job):**
1. **Dedupe** every result against `comps.json` by ebayId — already-banked
   items are dead weight, drop them.
2. **Parse titles** into candidate brand / model / scale / control fields.
   Titles are all the API gives you — there are no structured control or
   condition fields. (Minus-words in queries DO work as of the 2026-10-21
   re-test — they were ignored back on Oct 11 — so targeted queries should
   carry `-parts -gear -set` style filters.)
3. **Pre-filter by title**: drop obvious non-comps — parts, decoders, track,
   decals, shells, tools, and seller-bundle lots. Keep factory A+B pairings
   and named factory sets flagged, not dropped (they're Don's judgment call).
4. **Sort HO first** (scale-balance directive), then write the surviving
   candidate pool back to the repo as a JSON list of ebayIds + parsed fields,
   ready for browser verification.

**All API use is Dragginmaster-only (Don's call, 2026-10-21).** Searches
AND coverage checks stay with Dragginmaster alone: he holds the key and
the search budget, and the monthly schedule (broad / targeted / reserve)
only balances if one operator runs it. Cinder never runs API queries and
never holds the key. If you need a search run or a coverage check, request
it in your handoff — Dragginmaster burns the search, pushes the raw dump
to `api-dumps/`, and you process it from there.

**Best-offer data — flag on, rule unchanged (Don's call, 2026-10-21).**
Every API search runs with `best_offer=1`: rows then carry a best_offer
true/false marker, and for offer sales the API price is the **actual
accepted amount** (test-verified against the listing page). Uses:
pre-filtering offer sales before browser verification, scouting, aggregate
market stats (labeled API-derived), and offer calibration for Don's own
buying/selling. **The guide's proof rule does NOT bend for this** — a
best-offer sale still never banks as a comp, because the accepted price is
not provable from the sold listing page itself. Per-item accepted prices
are never published on the site as verified facts; aggregates only.

**Hard cautions about API data:**
- API "sold" results include listings that merely **ENDED unsold** (proven
  repeatedly, Oct 2026). An API hit is a lead, never evidence.
- API prices can be the **list price on a best-offer-accepted sale** — the
  hidden-price trap (hard rule 5) is invisible in API data.
- **API prices can also UNDERSTATE the real sold price** (proven
  2026-10-21: API said $30, the page's firm sold price was $50; API said
  $79, the page said $99 — multi-sale and promoted listings seem to trip
  it). The API's `ended_at` can likewise show future dates on
  multi-quantity listings. **The sold page always wins. Never bank an API
  price, date, or flag over what the page itself shows.**
- **Nothing banks from API data alone.** Every candidate still passes the
  browser verification gate on its live sold page + a saved screenshot
  (hard rules 1–2). Verification is the bottleneck, not finding.
- API data ages: eBay strips sold pages older than ~90 days down to
  ENDED-only shells that can never verify. Process dumps promptly, newest
  sold dates first.
- **Never discard raw dumps.** Re-processing works from the dumps — it must
  never cost new searches.

## Audit pages — how they're made (the review page Don rules on)

When a run accumulates genuine judgment calls, they go to Don on a single
standalone HTML page. **Only genuine judgment calls belong on it** — settled-
rule rejects never pad the page; Don's attention is the scarce resource.

**Input:** an `audit_candidates.json` — one object per candidate:
`ebayId`, `title`, `price` (USD), `date`, `brand`, `scale`, `road`,
`shot` (path to the candidate's saved screenshot), and `question` — the
exact question for Don, in plain words, stating the conflicting facts
(e.g. "title says 8953, the number painted on the loco reads 8937 — which
goes in the guide?"). Reference builder:
`~/workspace/comps-audit/audit_2026-10-21-plus50/build_audit_form.py`
(Dragginmaster's machine) — the pattern below is what matters.

**Build recipe:**
1. **Embed every screenshot in the page**: PIL → convert RGB → downscale to
   max 880 px wide → JPEG quality 60 → base64 data URI. (71 cards ≈ 4 MB.)
2. **One card per candidate**, numbered in pile order: card number + full
   listing title; a meta line (price · sold date · brand · scale · road);
   the screenshot; the question in a highlighted box; a link to
   `https://www.ebay.com/itm/<ebayId>`; verdict radios **Bank it / Trash it /
   Undecided** (Undecided preselected); and a free-text note box
   ("your call in your words — optional").
3. **Header** states the run's result (guide count before → after) and that
   picks save as you go.
4. **Persistence:** save verdicts + notes to `localStorage` on every change
   under a per-run key (e.g. `plus50AuditV1`), restore on load, and show an
   "X of N decided" counter. Don WILL close the page mid-review — losing his
   progress is not acceptable.
5. **"Copy my decisions" button** (fixed at the bottom): builds a plain-text
   block — a header line, then one line per card:
   `N. <ebayId> — BANK|TRASH|UNDECIDED — note: <note> — <title>` — copies it
   to the clipboard AND displays it on the page (clipboard may be blocked;
   the on-page text is the fallback). Don pastes the block back in chat.

**Delivery:** attach the single .html file in chat. Do **NOT** deliver it
via a file-storage link — on 2026-10-19 that route downloaded as
octet-stream instead of rendering on Don's Android. Known quirk: the in-app
attachment preview won't raise a keyboard for the note boxes on mobile, so
Don may open it in Chrome, paste the decisions block, or just rule in chat
card by card — all are equally valid input.

**Don's ruling protocol (2026-10-21):**
- "**Bank it**" with no note = he agrees with the recommendation/framing in
  the card's question — bank it exactly that way.
- A **note overrides** the framing.
- "**Trash it**" = gone. Record his stated reason verbatim when he gives one.
- He may **reverse** a ruling — apply the reversal, pull the comp back out
  of the guide if it was already banked (Kato EF60 precedent, 2026-10-21).

**After rulings land:** bank the BANKs (move each shot to
`shots/<ebayId>.jpg`, append to comps.json with a note "Banked from the
<run> audit pile on Don's ruling <date>"), record every decision in the
run's `decisions.json`, regenerate `price-list.html` + bump `sw.js` CACHE in
the site repo, push both repos.

## Workflow per task

1. Take the issue (e.g. "trend run: Proto 2000 SD60 HO DC to 5/5").
2. Branch `cinder/<short-task-name>` in THIS repo.
3. Hunt → verify → bank (comps.json + shots/). Update `count`/`updated`.
4. Regenerate `price-list.html` in the site repo (its AGENTS.md).
5. Update HANDOFF.md on your branch; open a PR with what was banked.
