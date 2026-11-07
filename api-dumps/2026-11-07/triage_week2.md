# Week 2 triage — 2026-11-07

Pool: 4722 new candidates (from pool_new_candidates.json).

## Buckets
- VERIFY (clean + ended within 90d, page likely alive): 709
- FLAG (needs judgment / sold page): 646
- REFERENCE (clean but ended >90d ago, page likely stripped): 2322
- OUT (hard rule violation from API/title alone): 1045

## Reasons (OUT + FLAG)
- best_offer: 658
- flag:model token not in title: 430
- parts/shell/decoder/track/tender: 233
- lot: 85
- flag:multi-qty units_sold=2: 79
- non-runner: 69
- flag:wording: 41
- flag:multi-qty units_sold=3: 32
- flag:multi-qty units_sold=4: 14
- flag:multi-qty units_sold=6: 8
- flag:multi-qty units_sold=7: 5
- flag:multi-qty units_sold=12: 4
- flag:multi-qty units_sold=5: 4
- flag:no usable title: 4
- flag:multi-qty units_sold=15: 3
- flag:multi-qty units_sold=24: 3
- flag:multi-qty units_sold=21: 2
- flag:multi-qty units_sold=13: 2
- flag:multi-qty units_sold=8: 2
- flag:multi-qty units_sold=10: 2
- flag:multi-qty units_sold=16: 1
- flag:multi-qty units_sold=26: 1
- flag:multi-qty units_sold=52: 1
- flag:multi-qty units_sold=36: 1
- flag:multi-qty units_sold=72: 1
- flag:multi-qty units_sold=85: 1
- flag:multi-qty units_sold=31: 1
- flag:multi-qty units_sold=110: 1
- flag:multi-qty units_sold=42: 1
- flag:multi-qty units_sold=9: 1
- flag:multi-qty units_sold=14: 1

## Per-tier (verify / flag / ref-old / out)
- Brass (N): 155 / 18 / 0 / 44
- Burlington Northern (N): 91 / 9 / 0 / 41
- Brass steam (N): 53 / 2 / 0 / 20
- Atlas U25B (N): 34 / 0 / 0 / 17
- Burlington CB&Q (N): 31 / 2 / 0 / 9
- Atlas GP7: 30 / 19 / 134 / 55
- Atlas VO-1000: 27 / 13 / 146 / 69
- Atlas GP40-2: 24 / 63 / 212 / 98
- Atlas GP9: 24 / 15 / 134 / 38
- Atlas SD9: 22 / 20 / 153 / 43
- Burlington Route (N): 20 / 1 / 0 / 2
- Fox Valley ES44AC: 20 / 3 / 162 / 25
- Kato GP38-2: 20 / 15 / 158 / 55
- InterMountain SD45-2: 19 / 10 / 76 / 25
- Kato U30C (N): 19 / 2 / 0 / 9
- Atlas B23-7: 18 / 14 / 137 / 67
- Broadway Limited SD40-2: 17 / 13 / 172 / 39
- Model Power 4-6-2 Pacific: 14 / 86 / 91 / 45
- Bachmann Explorer Set: 12 / 11 / 131 / 84
- Model Power 2-6-0 Mogul: 11 / 19 / 59 / 26
- Bachmann GP7: 8 / 3 / 58 / 11
- Con-Cor 4-6-4 Hudson: 8 / 83 / 83 / 63
- Fox Valley GP60M: 7 / 0 / 52 / 18
- Bachmann F7B: 6 / 6 / 116 / 26
- Life-Like SW1200: 6 / 21 / 35 / 11
- Life-Like 2-8-4 Berkshire: 4 / 22 / 37 / 9
- Atlas C630: 2 / 10 / 32 / 14
- Bachmann F7A + F7B: 2 / 0 / 28 / 5
- Bachmann Plus F7A: 2 / 4 / 48 / 20
- Atlas 0-6-0 Switcher: 1 / 152 / 33 / 51
- Bachmann 2-6-0 Mogul: 1 / 0 / 4 / 1
- Bachmann Plus DD40AX: 1 / 0 / 28 / 3
- Broadway Limited E9: 0 / 0 / 3 / 1
- Life-Like 0-8-0 Switcher: 0 / 10 / 0 / 1

Verify queue ordered by tier size (most candidates first), newest first.
Verification still needs a working eBay route (sold page + screenshot).
