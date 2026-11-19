"""Entry program for make.fun competition news-image-20261119.

The entry is a single image, entry.png, that sums up the world news of
Thursday 19 November 2026. This program copies that image into the
grader's output directory. Standard library only, no network access,
deterministic: every run writes exactly the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    if not src.exists():
        raise SystemExit(f"entry.png not found next to the program: {src}")
    dst = out_dir / "entry.png"
    # The name stays entry.png either way: the competition tells PNG from
    # JPEG by the file's first bytes, so the bytes are copied as-is.
    shutil.copyfile(src, dst)
    src_size = src.stat().st_size
    if not dst.exists() or dst.stat().st_size != src_size:
        dst_size = dst.stat().st_size if dst.exists() else -1
        raise SystemExit(
            f"entry.png copy is incomplete: source {src_size} bytes, "
            f"destination {dst_size} bytes"
        )
    # The competition tells PNG from JPEG by the file's first bytes, so
    # confirm the copy really is one of those two formats.
    with dst.open("rb") as f:
        magic = f.read(4)
    if magic[:4] != b"\x89PNG" and magic[:3] != b"\xff\xd8\xff":
        raise SystemExit(
            f"entry.png has unexpected first bytes: {magic.hex()}"
        )


if __name__ == "__main__":
    main()
