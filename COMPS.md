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
  never guess.
- Trend tiers group by **brand+model+scale+control** (road name excluded from
  the key, shown per sale).

## Harvest operations

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
   chat for a few; if there are many, build the HTML review page
   (`python3 build-triage-page.py candidates.json triage-review.html` — see
   the script's docstring; every candidate MUST carry its ebayId) and attach
   it so he can mark Keep/Drop per card.
5. **Sanity check** before filing, then push.

## Workflow per task

1. Take the issue (e.g. "trend run: Proto 2000 SD60 HO DC to 5/5").
2. Branch `cinder/<short-task-name>` in THIS repo.
3. Hunt → verify → bank (comps.json + shots/). Update `count`/`updated`.
4. Regenerate `price-list.html` in the site repo (its AGENTS.md).
5. Update HANDOFF.md on your branch; open a PR with what was banked.
