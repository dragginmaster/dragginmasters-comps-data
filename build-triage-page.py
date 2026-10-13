#!/usr/bin/env python3
"""Build Don's comp-candidate triage page.

Usage:
    python3 build-triage-page.py candidates.json triage-review.html

candidates.json: a list of objects with:
    ref       "1a"                       short label for Don's keeper calls
    model     "Big Boy 4-8-8-4"
    brand     "Kato"                     optional
    scale     "N"                        optional
    control   "DC"                       optional (use "unclear" when unknown)
    road      "Union Pacific"            optional
    condition "New"                      optional
    price     312.23
    date      "2026-10-08"               sale date
    ebayId    "407235668463"             REQUIRED — every candidate needs one
    url       "https://www.ebay.com/itm/..."  optional, defaults to itm/ebayId
    flag      "Price far above the other two; possible rare variant."
                                           optional anomaly note

The page shows one card per candidate with Keep / Drop / Undecided radios,
persists Don's picks in localStorage, and has a copy button that emits his
decisions as text to paste back.
"""
import json
import html
import sys

def esc(s):
    return html.escape("" if s is None else str(s))

def main():
    src, dst = sys.argv[1], sys.argv[2]
    cands = json.load(open(src))

    cards = []
    for i, x in enumerate(cands):
        if not x.get("ebayId"):
            raise SystemExit("candidate %s is missing ebayId — every candidate needs one" % x.get("ref", i))
        url = x.get("url") or ("https://www.ebay.com/itm/" + str(x["ebayId"]))
        sub = " · ".join(p for p in [
            esc(x.get("brand")), esc(x.get("scale")), esc(x.get("control")),
        ] if p)
        row2 = "$%.2f &middot; sold %s" % (x["price"], esc(x["date"]))
        extras = " &middot; ".join(p for p in [esc(x.get("road")), esc(x.get("condition"))] if p)
        if extras:
            row2 += " &middot; " + extras
        flag_html = ""
        if x.get("flag"):
            flag_html = ('  <div class="why"><span class="sig sig-flag">flag</span> '
                         + esc(x["flag"]) + "</div>\n")
        cards.append(
            '<div class="card" data-ref="' + esc(x["ref"]) + '" data-id="' + esc(x["ebayId"]) + '">\n'
            '  <div class="row1"><strong>' + esc(x["ref"]) + " — " + esc(x["model"]) + "</strong>"
            + (' <span class="sub">' + sub + "</span>" if sub else "") + "</div>\n"
            '  <div class="row2">' + row2 + "</div>\n"
            + flag_html
            + '  <div class="row3"><a href="' + esc(url) + '" target="_blank" rel="noopener">'
              'eBay listing ' + esc(x["ebayId"]) + "</a></div>\n"
            + '  <div class="verdict">\n'
            + '    <label><input type="radio" name="v%d" value="keep"> Keep</label>\n' % i
            + '    <label><input type="radio" name="v%d" value="drop"> Drop</label>\n' % i
            + '    <label><input type="radio" name="v%d" value="" checked> Undecided</label>\n' % i
            + "  </div>\n</div>"
        )

    page = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Comp triage — your keeper calls</title>
<style>
body{font-family:system-ui,sans-serif;background:#fffdf6;color:#16202e;margin:0;line-height:1.5}
.wrap{max-width:760px;margin:0 auto;padding:16px 12px 90px}
h1{font-size:22px}.lede{color:#444;max-width:640px}
.card{border:1px solid #e4dcc8;border-radius:10px;padding:10px 12px;margin:10px 0;background:#fff}
.row1{font-size:15px}.row1 .sub{font-size:13px;color:#8a7f68;font-weight:400}
.row2{color:#2e7d43;font-weight:600;margin:2px 0}
.row3{font-size:13px;color:#8a7f68}.row3 a{color:#b3541e;font-weight:600}
.verdict{margin-top:8px;font-size:15px}.verdict label{margin-right:14px}
.why{font-size:13px;color:#444;background:#f7f2e4;border-radius:8px;padding:8px 10px;margin:8px 0}
.sig{display:inline-block;font-size:12px;font-weight:700;border-radius:12px;padding:2px 10px;margin-right:6px}
.sig-flag{background:#b3541e;color:#fff}
.copybtn{background:#2e7d43;color:#fff;border:none;border-radius:24px;padding:14px 28px;font-size:16px;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.btnrow{text-align:center;margin:14px 0}
#out{white-space:pre-wrap;background:#16202e;color:#ffe9c4;border-radius:8px;padding:12px;margin-top:16px;display:none}
.meta{font-size:13px;color:#8a7f68;text-align:center}
</style></head><body><div class="wrap">
<h1>Comp candidates — your keeper calls</h1>
<p class="lede">%%N%% candidates. Open any eBay link to check the listing yourself, mark
<b>Keep</b> or <b>Drop</b> on each card (cards flagged need your judgment call),
then hit the green button and paste the result back. Your picks are saved on
this device even if you leave the page.</p>
<div class="btnrow"><button class="copybtn">Copy my decisions</button></div>
%%CARDS%%
<pre id="out"></pre>
<p id="progress" class="meta"></p>
<div class="btnrow"><button class="copybtn">Copy my decisions</button></div>
</div>
<script>
const KEY = 'triageReviewV1';
const loadSaved = () => { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch(e){ return {}; } };
const saveAll = (obj) => { try { localStorage.setItem(KEY, JSON.stringify(obj)); } catch(e){} };
const updateProgress = () => {
  const cards = document.querySelectorAll('.card');
  let decided = 0;
  cards.forEach(c => { const sel = c.querySelector('input:checked'); if (sel && sel.value) decided++; });
  document.getElementById('progress').textContent =
    decided + ' of ' + cards.length + ' decided — your picks are saved on this device even if you leave the page.';
};
document.querySelectorAll('.card').forEach(c => {
  const v = loadSaved()[c.dataset.id];
  if (v) { const r = c.querySelector('input[value="' + v + '"]'); if (r) r.checked = true; }
  c.addEventListener('change', () => {
    const all = loadSaved();
    const sel = c.querySelector('input:checked');
    if (sel && sel.value) all[c.dataset.id] = sel.value; else delete all[c.dataset.id];
    saveAll(all);
    updateProgress();
  });
});
updateProgress();
const doCopy = () => {
  const keep = [], drop = [];
  document.querySelectorAll('.card').forEach(c => {
    const sel = c.querySelector('input:checked');
    const label = c.dataset.ref + ' (' + c.dataset.id + ')';
    if (sel.value === 'keep') keep.push(label);
    else if (sel.value === 'drop') drop.push(label);
  });
  const total = document.querySelectorAll('.card').length;
  const txt = 'TRIAGE DECISIONS\\nKEEP (' + keep.length + '): ' + keep.join(', ')
    + '\\nDROP (' + drop.length + '): ' + drop.join(', ')
    + '\\nUNDECIDED: ' + (total - keep.length - drop.length);
  document.getElementById('out').style.display = 'block';
  document.getElementById('out').textContent = txt;
  if (navigator.clipboard) navigator.clipboard.writeText(txt).catch(()=>{});
  window.scrollTo(0, document.getElementById('out').offsetTop - 80);
};
document.querySelectorAll('.copybtn').forEach(b => { b.onclick = doCopy; });
</script></body></html>"""

    page = page.replace("%%N%%", str(len(cands))).replace("%%CARDS%%", "\n".join(cards))
    open(dst, "w").write(page)
    print("wrote triage page:", len(cands), "candidates ->", dst)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: build-triage-page.py candidates.json triage-review.html")
    main()
