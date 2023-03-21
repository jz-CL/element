from pathlib import Path

line_cache : dict[Path, dict[str, str]] = {}

PEP_ROOT = Path(__file__).parent
print(PEP_ROOT)