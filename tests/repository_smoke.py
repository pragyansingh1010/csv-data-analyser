from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = list(ROOT.glob("*.py"))
assert files, "no Python analyzer source found"
assert all(p.stat().st_size > 0 for p in files)
print("CSV Data Analyser smoke check passed")
