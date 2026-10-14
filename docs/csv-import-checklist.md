# CSV Import Checklist

- Confirm the file is readable before parsing.
- Handle a header-only file as an empty dataset.
- Preserve quoted commas inside cells.
- Detect inconsistent row lengths and report their line numbers.
- Treat blank numeric cells as missing unless the project explicitly defines otherwise.
- Summarize parse errors before attempting calculations.