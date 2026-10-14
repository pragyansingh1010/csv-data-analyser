## CSV import edge cases

- Handle an empty file and a header-only file explicitly.
- Detect rows with inconsistent column counts.
- Preserve quoted fields containing commas and escaped quotes.
- Treat blank cells and non-numeric cells consistently during numeric summaries.
- Report skipped or invalid rows so the user can understand the output.