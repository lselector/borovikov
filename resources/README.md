# Resources

Reference material for the Perkins Sabre M92, serial
`AR50750U038560F`. Last updated 2026-09-17.

Files are split three ways:

| Folder | What is in it |
|---|---|
| `resources/` | Documents that describe **this engine, in a boat** |
| `resources/_more_resources/` | Right family, wrong build or wrong application. Background only |
| `resources/_txt_versions/` | Plain text extracted from the PDFs, for grepping |

## resources/

| File | Publication | Pages | Notes |
|---|---|---|---|
| `perkins_sabre_M92_M115T_users_handbook_TPD1397EGN.pdf` | TPD 1397EGN Issue 10, Mar 2013 | 96 | **Marine.** The M92 handbook. Schedules, fluids, raw water side, fault charts |
| `perkins_sabre_marine_installation_manual_TPD1317E.pdf` | TPD 1317E | 94 | **Marine.** Installation, and every wiring diagram. Figure 4 is the M92 |
| `perkins_1000_series_workshop_manual_TPD1350_AJ-AS_YG-YK.pdf` | TPD 1350E Issue 4, Dec 2001 | 370 | **The repair manual for this engine.** Covers type AR |
| `perkins_PartsBook_AR50750-04.pdf` | Perkins AR50750, 16 Sep 2026 | 152 | **Parts book for this build list.** Base engine only; the Sabre marine equipment is not in it. Real text layer, so numbers in the text version are exact |
| `perkins_sabre_M92_sales_brochure.pdf` | Trans Atlantic Diesels | 2 | **Marine.** M92 ratings and construction |
| `perkins_engine_number_guide.pdf` | PP3000/05/15 | 4 | Official serial number decoding tables |
| `sabre_perkins_marine_parts_list.pdf` | Sabre Plant & Marine | - | **Marine.** Impellers, raw water pump cams, tubestacks, anodes, exhaust bellows, gearbox couplings |
| `prm_500_workshop_manual.pdf` | PRM 500, Issue 2, June 2000 | 60 | **Marine.** Full teardown for the PRM 500D |
| `zf_hurth_HBW_360_450_630_repair_manual.pdf` | ZF Marine 310.01.0001 | 107 | **Marine.** Covers the HBW 450. Four languages |

Two notes on that list.

**The workshop manual says "industrial and agricultural" on its
cover.** That is not a mistake and it has not been filed wrongly.
Perkins never published a separate marine workshop manual for the
M92, because the engine underneath the marine equipment is a
stock 1004-42 and TPD 1350E is its repair manual. The marine
equipment on top is covered by TPD 1397EGN and TPD 1317E.

**The Sabre marine parts list is a supplier stock list**, not an
engine parts catalogue. It is a flat list of marine part numbers
and descriptions, and some descriptions are cut off at the column
edge. Useful for cross-referencing a marine item, not for
identifying what your engine was built with.

Establish which gearbox is fitted before opening either gearbox
manual. The M92 was offered with the PRM 500D and the ZF HBW /
HSW 450A, which are unrelated designs and take different oil.

## resources/_more_resources/

Nothing here should be used to order a part or set a figure
without checking it against a document from the folder above.

| File | Publication | Pages | Why it is set aside |
|---|---|---|---|
| `perkins_1004-42_parts_manual_AR81148.pdf` | Perkins AR81148, June 2001 | 122 | Build list **81148**, a lift truck build. Ours is **50750**. Superseded by the AR50750 book. Keep as a second opinion only |
| `perkins_sabre_M92B_users_handbook_N37347.pdf` | N37347 | 64 | Marine, but the **wrong engine**. The M92B is 1100 Series, 4.4 litres |
| `perkins_TPD1312_extract_DP200_pump_chapter.pdf` | Extract from TPD 1312 | 4 | Industrial. Mostly duplicates TPD 1350E, but adds the 100 deg BTDC piston probe timing method |
| `delphi_lucas_CAV_DPA_pump_rebuild_manual.pdf` | Delphi / Lucas CAV | 21 | **Wrong pump family.** The M92 uses a DP200. Read it to understand how a Lucas rotary works, not to work on yours |
| `prm_owners_handbook_all_models.pdf` | PRM Newage | 22 | Marine, but generic across PRM 80 to 1750. The PRM 500 workshop manual is better here |
| `jabsco_flexible_impeller_pumps_service_manual.pdf` | Jabsco / Xylem | 46 | Marine, but general. Does not name the 29640-1101 fitted to the M92 |

## resources/_txt_versions/

Plain text extracted with `pdftotext -layout`, for command line
searching across every manual at once:

```bash
grep -n -i "valve tip clearance" resources/_txt_versions/*.txt
```

All fifteen manuals are searchable here: ten carry a real text
layer, and the other five are represented by their `_OCR`
copies. The folder is flat, so text from `_more_resources/` sits
alongside the rest; filenames match the PDFs they came from.

Anything with `_OCR` in the name came from optical recognition
and contains errors. See the warning below.

## OCR copies

Five PDFs arrived as page images from a scanner with no text in
them at all. Each now has a searchable twin alongside it, with
`_OCR` in the name, produced by `s4_ocr_pdfs.py`. The originals
are untouched and remain the authority.

| Original | OCR copy | Pages | Text recovered |
|---|---|---|---|
| `_more_resources/perkins_1004-42_parts_manual_AR81148.pdf` | `..._AR81148_OCR.pdf` | 116 | 31,587 chars |
| `zf_hurth_HBW_360_450_630_repair_manual.pdf` | `..._OCR.pdf` | 58 | 40,545 chars |
| `prm_500_workshop_manual.pdf` | `..._OCR.pdf` | 54 | 62,603 chars |
| `sabre_perkins_marine_parts_list.pdf` | `..._OCR.pdf` | 14 | 45,311 chars |
| `_more_resources/perkins_TPD1312_extract_DP200_pump_chapter.pdf` | `..._OCR.pdf` | 4 | 4,763 chars |

### Do not trust an OCR'd part number

This is not a theoretical warning. Checking page 55 of the
parts book against the original image, four of thirteen part
numbers came back wrong:

| On the page | OCR read it as | Error |
|---|---|---|
| `U5MW0178` | `USMW0178` | 5 became S |
| `U7LW0161` | `U7LWO161` | 0 became O |
| `U5MH0056` | `USMH0056` | 5 became S |
| `LBHA1879` | `LBHAI879` | 1 became I |

Every error is a digit and letter that look alike. Descriptions,
headings and plate titles came through clean, so the OCR is good
for **finding** things: which plate a component sits on, which
page covers the thermostat, whether a manual mentions a part at
all. It is not good for **reading numbers off**. Search with it,
then open the original PDF at that page and read the number with
your eyes before ordering.

## Not here

Parts information for the marine equipment: heat exchanger, raw
water pump, marine exhaust, alternator. The AR50750 book covers
the base engine only, and no publication number for an M92
marine parts book is known. (TPD 1399E, once named here, is the
M65 / M85T installation manual, not an M92 parts book.) Until
then, `sabre_perkins_marine_parts_list.pdf` and
[Sabre Plant & Marine](https://www.sabrepm.com/downloads) cover
common marine items.

Free route, in a browser on a laptop: register the engine at
[myengine.perkins.com](https://myengine.perkins.com/), the
Perkins Retail Customer Hub, which carries parts information,
service literature and OMMs. The My Engine phone app is the same
system.

Failing that, find a distributor at
[distributorlocator.perkins.com](https://distributorlocator.perkins.com/)
and quote `AR50750U038560F`, or contact Wimborne Marine Power
Centre, who built the engine:
Marine@Perkins.com, +44 (0)1202 796000.

Note that `b2b.perkins.com` is closed. Perkins is replacing it
and currently routes everyone to the distributor locator.

## Contacts

Quote `AR50750U038560F` (TPL 1396/2400) every time.

**Local dealer, recommended by Perkins:** Sarah Brown, Clarke
Power Solutions, 3133 E. Kemper Road, Cincinnati, OH 45241.
SBrown@clarkepsi.com, 913-928-6993 (desk), 913-284-2137 (mobile).

**Perkins:**

- US: 888-737-5364 (888-PERK-ENG). Perkins Engines Inc.,
  1600 W Kingsbury St, Seguin, TX 78155, USA
- UK: +44 (0)1733 583000
- Email: perkinsmarine@perkins.com
- Web: [perkins.com](https://www.perkins.com),
  [myengine.perkins.com](https://myengine.perkins.com)

**Sabre Plant & Marine** (source of the marine parts list):

- Phone: +44 (0)1224 877667
- Email: sales@sabrepm.com, accounts@sabrepm.com
- Web: [sabrepm.com](https://www.sabrepm.com)

## Where these came from

- Workshop manual and M92 handbook: dieselmann.no manual archive
- Installation manual: plaisance-pratique.com
- M92B handbook: Caterpillar content server
- Engine number guide: ruttsmachine.com
- M92 data sheet: tadiesels.com
- Marine parts list: sabrepm.com/downloads
- PRM and ZF manuals: public marine manual archives
- Parts books AR81148 and AR50750: supplied by the owner

All are publicly posted copies of manufacturer literature. For
current official documents and for parts information tied to a
serial number, use Perkins My Engine or a Perkins distributor.
