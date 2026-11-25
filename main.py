#!/usr/bin/env python3
"""Copy the bundled invitation image to the output directory.

The entry ships as a single finished image, entry.png, sitting next to
this script: a hand-written-style letter on cream paper inviting the
AI judge to visit a cozy house, with a small watercolor cottage, a
steaming teacup and a sleeping cat at the top. This program copies it
unchanged into the output directory and then proves the copy is
complete by comparing the full SHA-256 hash of the copy against the
hash of the source.

The output directory comes from MAKEFUN_OUTPUT_DIR when that variable
is set; otherwise /output is used. The output file is always named
entry.png. When the output directory is the same directory the script
lives in, there is nothing to copy: the file already there is simply
verified in place.

Standard library only; no network access at all.
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_SIDE = 1024


def sha256_of(path):
    """Return the full SHA-256 hex digest of a file, read in blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def is_whole_png(path):
    """Check the file starts with the PNG signature and ends with IEND.

    A cheap sanity check that the bundled image is a complete PNG
    before it is shipped; the gate rejects anything that is not a
    whole image.
    """
    with open(path, "rb") as handle:
        head = handle.read(len(PNG_MAGIC))
        if head != PNG_MAGIC:
            return False
        handle.seek(-12, os.SEEK_END)
        tail = handle.read(12)
    return tail[4:8] == b"IEND"


def png_dimensions(path):
    """Return (width, height) read from the PNG IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def check_gate_limits(path):
    """Enforce the bounty gate: at most 1 MiB, at most 1024x1024 px.

    Returns an error string, or None when the image passes.
    """
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        return "image is %d bytes, over the 1 MiB gate" % size
    dims = png_dimensions(path)
    if dims is None:
        return "cannot read PNG dimensions"
    width, height = dims
    if width > MAX_SIDE or height > MAX_SIDE:
        return "image is %dx%d, over the 1024x1024 gate" % (width, height)
    return None


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, SOURCE_NAME)

    if not os.path.isfile(source_path):
        print("missing bundled image: %s" % source_path, file=sys.stderr)
        return 1

    if not is_whole_png(source_path):
        print("bundled image is not a whole PNG", file=sys.stderr)
        return 1

    gate_error = check_gate_limits(source_path)
    if gate_error is not None:
        print("gate check failed: %s" % gate_error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, SOURCE_NAME)

    if os.path.abspath(output_path) != os.path.abspath(source_path):
        shutil.copyfile(source_path, output_path)

    if not is_whole_png(output_path):
        print("output is not a whole PNG", file=sys.stderr)
        return 1

    source_hash = sha256_of(source_path)
    output_hash = sha256_of(output_path)
    if source_hash != output_hash:
        print("copy mismatch: %s != %s" % (output_hash, source_hash),
              file=sys.stderr)
        return 1

    size = os.path.getsize(output_path)
    width, height = png_dimensions(output_path)
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (output_path, width, height, size, output_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
