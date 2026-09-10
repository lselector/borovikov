# Resources

Reference material for the Perkins Sabre M92, serial
`AR50750U038560F`. Downloaded 2026-09-10.

| File | Publication | Pages | Notes |
|---|---|---|---|
| `perkins_1000_series_workshop_manual_TPD1350_AJ-AS_YG-YK.pdf` | TPD 1350E Issue 4, Dec 2001 | 370 | **The repair manual for this engine.** Covers type AR |
| `perkins_sabre_M92_M115T_users_handbook_TPD1397EGN.pdf` | TPD 1397EGN Issue 10, Mar 2013 | 96 | Official M92 handbook. English, German, Norwegian |
| `perkins_sabre_marine_installation_manual_TPD1317E.pdf` | TPD 1317E | 94 | Sabre marine installation manual |
| `perkins_sabre_M92_sales_brochure.pdf` | Trans Atlantic Diesels | 2 | M92 ratings and construction summary |
| `perkins_engine_number_guide.pdf` | PP3000/05/15 | 4 | Official serial number decoding tables |
| `perkins_sabre_M92B_users_handbook_N37347.pdf` | N37347 | 64 | M92B. **Different engine.** Comparison only |

## Gearbox and fuel pump

| File | Publication | Pages | Notes |
|---|---|---|---|
| `prm_500_workshop_manual.pdf` | PRM 500, Issue 2, June 2000 | 60 | Full teardown for the PRM 500D |
| `prm_owners_handbook_all_models.pdf` | PRM Owners Handbook | 22 | Operation and servicing, PRM 80 to 1750 |
| `zf_hurth_HBW_360_450_630_repair_manual.pdf` | ZF Marine 310.01.0001 | 107 | Covers the HBW 450. Four languages |
| `perkins_TPD1312_extract_DP200_pump_chapter.pdf` | Extract from TPD 1312 | 4 | DP200 pump chapter, engine side |
| `delphi_lucas_CAV_DPA_pump_rebuild_manual.pdf` | CAV DPA rebuild manual | 21 | **Different pump family.** Background only |

Check which gearbox is fitted before using either gearbox
manual. The M92 was offered with the PRM 500D and the ZF HBW /
HSW 450A, which are unrelated designs.

## Not here

The illustrated parts book for the 1004-42 is Perkins
publication **AR81148**, 116 pages. No free copy exists that I
could find. Buy it against your engine number, or use Perkins My
Engine for parts information tied to the serial.

Wiring diagrams are not a separate document. They live in
chapter 7 of the installation manual, from page 37. Figure 4 is
the M92.

Files ending `.txt` are plain text extracted from the matching
PDF, for command line searching:

```bash
grep -n -i "torque" perkins_1000_series_workshop_manual_TPD1350_AJ-AS_YG-YK.txt
```

## Where these came from

- Workshop manual and M92 handbook: dieselmann.no manual archive
- Installation manual: plaisance-pratique.com
- M92B handbook: Caterpillar content server
- Engine number guide: ruttsmachine.com
- M92 data sheet: tadiesels.com

All are publicly posted copies of Perkins literature. For current
official documents and for parts information tied to a serial
number, use Perkins My Engine or a Perkins distributor.
