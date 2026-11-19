"""Sum up 19 November 2026 world news in one image.

The entry image is bundled in this repository as image.png.
This program deterministically copies it to /output/entry.png,
with no network access, so two runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"Wrote {DST}")


if __name__ == "__main__":
    main()
