#!/usr/bin/env python3
"""
Add a searchable text layer to the scanned PDFs in
"resources".

Five of the manuals are page images from a scanner, so
grep finds nothing in them. This runs OCR over any PDF
with no usable text layer and writes the result beside
the original with "_OCR" added to the name. Originals are
never modified.

Files that already have a text layer are skipped, and so
are files whose _OCR copy exists, which makes the script
safe to re-run.

OCR misreads characters. Treat a part number taken from an
_OCR file as a lead, not as fact, and check it against the
page image before ordering anything.

Needs ocrmypdf: brew install ocrmypdf

Usage:
    python3 s4_ocr_pdfs.py
    python3 s4_ocr_pdfs.py --force
    python3 s4_ocr_pdfs.py resources/some_manual.pdf

Created: 2026-09-12
Last updated: 2026-09-12
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RESOURCES_DIR = "resources"
OCR_SUFFIX = "_OCR"

# A page image carries no text. Anything under this many
# non-space characters is a scan, possibly with a
# watermark or a stray caption on top.
TEXT_THRESHOLD = 2000

# --redo-ocr keeps any real text and OCRs the image areas,
# which matters because some scans carry a watermark on
# every page. --force-ocr rasterises instead, and is the
# fallback when the first pass will not run.
OCR_ARGS = ["-l", "eng", "--rotate-pages", "--quiet"]

LOG_FILE = "/tmp/ocr_pdfs.log"


# --------------------------------------------------------------
def log_message(message):
    """Print timestamped log message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


# --------------------------------------------------------------
def check_ocrmypdf():
    """Check that ocrmypdf is on the path."""
    try:
        subprocess.run(
            ["ocrmypdf", "--version"],
            capture_output=True, check=True
        )
        return True
    except (subprocess.CalledProcessError, OSError):
        log_message("ERROR: ocrmypdf not found. "
                    "Install: brew install ocrmypdf")
        return False


# --------------------------------------------------------------
def text_length(pdf_path):
    """Count non-space characters pdftotext can pull out."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, check=True
        )
    except (subprocess.CalledProcessError, OSError):
        return 0
    return len("".join(result.stdout.split()))


# --------------------------------------------------------------
def ocr_path(pdf_path):
    """Build the _OCR output path for a source PDF."""
    path = Path(pdf_path)
    return path.with_name(f"{path.stem}{OCR_SUFFIX}.pdf")


# --------------------------------------------------------------
def run_ocrmypdf(source, target, mode):
    """Run one ocrmypdf pass, returning True on success."""
    command = ["ocrmypdf", mode] + OCR_ARGS
    command += [str(source), str(target)]
    try:
        with open(LOG_FILE, "a") as handle:
            handle.write(f"\n=== {source} ({mode}) ===\n")
            subprocess.run(
                command, stdout=handle, stderr=handle,
                check=True
            )
        return True
    except (subprocess.CalledProcessError, OSError) as exc:
        log_message(f"  {mode} failed: {exc}")
        return False


# --------------------------------------------------------------
def ocr_one_file(pdf_path, force):
    """OCR a single PDF, returning a status string."""
    target = ocr_path(pdf_path)

    if target.exists() and not force:
        return "skipped, _OCR copy exists"

    chars = text_length(pdf_path)
    if chars > TEXT_THRESHOLD:
        return f"skipped, has a text layer ({chars} chars)"

    log_message(f"OCR {Path(pdf_path).name} ({chars} chars)")
    for mode in ("--redo-ocr", "--force-ocr"):
        if run_ocrmypdf(pdf_path, target, mode):
            found = len("".join(
                subprocess.run(
                    ["pdftotext", str(target), "-"],
                    capture_output=True, text=True
                ).stdout.split()
            ))
            size_mb = target.stat().st_size / 1048576
            return (f"done with {mode}, {found} chars, "
                    f"{size_mb:.1f} MB")

    return "FAILED, see " + LOG_FILE


# --------------------------------------------------------------
def collect_targets():
    """Return PDF paths from argv, or every resources PDF."""
    if len(sys.argv) > 1:
        named = [a for a in sys.argv[1:]
                 if a.endswith(".pdf") and os.path.isfile(a)]
        if named:
            return named

    if not os.path.isdir(RESOURCES_DIR):
        log_message(f"ERROR: {RESOURCES_DIR} not found")
        sys.exit(1)

    found = Path(RESOURCES_DIR).rglob("*.pdf")
    return sorted(
        str(p) for p in found
        if not p.stem.endswith(OCR_SUFFIX)
    )


# --------------------------------------------------------------
def main():
    """Add a text layer to every scanned PDF found."""
    force = "--force" in sys.argv

    log_message("Starting OCR pass")
    if not check_ocrmypdf():
        sys.exit(1)

    targets = collect_targets()
    log_message(f"Checking {len(targets)} PDFs")

    done = 0
    for pdf_path in targets:
        status = ocr_one_file(pdf_path, force)
        if status.startswith("done"):
            done += 1
            log_message(f"  {Path(pdf_path).name}: {status}")
        elif status.startswith("FAILED"):
            log_message(f"  {Path(pdf_path).name}: {status}")

    log_message("=" * 50)
    log_message(f"OCR copies written: {done}")
    log_message(f"ocrmypdf log: {LOG_FILE}")


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
