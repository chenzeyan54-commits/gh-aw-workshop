from __future__ import annotations

import pathlib
import re

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)", re.MULTILINE)
CODE_FENCE_RE = re.compile(r"