# borovikov

Working notes and reference material for a Perkins Sabre M92 marine
diesel engine, serial `AR50750U038560F`, built 1999.

## Contents

| Path | What it is |
|---|---|
| `GUIDE_to_M92.md` | **The main document.** Repair, service and tuning guide for this engine |
| `GUIDE_to_M92.pdf` | Printable version, US Letter, built from the Markdown |
| `resources/` | Manuals for this engine in a boat. `_more_resources/` holds background material for other builds and applications, `_txt_versions/` holds extracted text |
| `images/` | Images used by the guide, standardised to 800x600 JPEG |
| `myprompts.md` | Research notes and prompts that led to the guide |

The engine data plate photographs in `images/` are originals.
They cannot be re-downloaded, so keep them in version control.

## The engine

The data plate photographs in `images/` decode as follows:

| Part | Value | Meaning |
|---|---|---|
| `AR` | Type code | Perkins 1004-42, the base engine of the M92 |
| `50750` | Build list | Build specification |
| `U` | Country | Built in the UK |
| `038560` | Serial | Engine serial number |
| `F` | Year | Built 1 April to 31 December 1999 |

The plate also carries `1396/2400` above the caption `TPL No`.
Quote both numbers when ordering parts.

For parts information, service literature and manuals tied to
this serial number, register the engine at
[myengine.perkins.com](https://myengine.perkins.com/). It is
free and runs in a browser.

The type code is the useful part. Because it is `AR`, the correct
factory repair manual is the Perkins New 1000 Series workshop
manual covering models AJ to AS, publication TPD 1350E. That
manual is in `resources/`, along with the M92 user handbook, the
Sabre marine installation manual, and two parts books: Perkins
build list AR50750 for the base engine, and a Sabre SPi-Lite
print for the marine equipment bolted on top of it.

## Resources

See `resources/README.md` for the file list, or section 2 of
`GUIDE_to_M92.md` for the same list plus online sources, parts
suppliers, forums and video.

Every PDF is also present as extracted plain text, so
they can be searched from the command line:

```bash
grep -n -i "valve tip clearance" resources/_txt_versions/*.txt
```

## Rebuilding the guide

Three scripts, run in order. Each is safe to re-run.

```bash
python3 s1_download_images.py   # collect images into images/
python3 s2_clean_images.py      # standardise them
python3 s3_make_pdf.py          # render GUIDE_to_M92.pdf
```

`s4_ocr_pdfs.py` is separate from that pipeline and only
needs running when a new scanned manual is added.

**`s1_download_images.py`** downloads a thumbnail for each
YouTube video the guide links to. Files already present are
skipped, so use `--force` to fetch them again. It also checks
that the three data plate photographs are still in `images/` and
warns if one is missing, since those are originals and cannot be
fetched back.

**`s2_clean_images.py`** converts everything under `images/` to
one standard: 800x600 JPEG, 72 DPI, trimmed and centred on a
white canvas with a 16 px margin. It backs the directory up to
`~/backups` first and keeps the three most recent backups. Needs
ImageMagick (`brew install imagemagick`).

**`s3_make_pdf.py`** renders any Markdown file in the repo to
PDF through WeasyPrint. Page setup is US Letter with 0.7 inch
margins, defined in `styles.css` rather than in the Python, so
the look can be changed without touching code. Heading anchors
are slugified the GitHub way, so the table of contents stays
clickable in the finished PDF.

```bash
python3 s3_make_pdf.py                    # GUIDE_to_M92.pdf
python3 s3_make_pdf.py README.md          # README.pdf
python3 s3_make_pdf.py README.md out.pdf
```

Requires `pip install markdown weasyprint`.

**`s4_ocr_pdfs.py`** adds a searchable text layer to any PDF in
`resources/` that has none, writing the result alongside the
original with `_OCR` in the name. Originals are never touched,
and files that already have text, or an `_OCR` copy, are
skipped. Requires `brew install ocrmypdf`.

```bash
python3 s4_ocr_pdfs.py                       # all scanned PDFs
python3 s4_ocr_pdfs.py resources/one.pdf     # just one
python3 s4_ocr_pdfs.py --force               # redo existing
```

OCR misreads characters. A part number read out of an `_OCR`
file is a lead, not a fact, and should be checked against the
page image before anything is ordered.
