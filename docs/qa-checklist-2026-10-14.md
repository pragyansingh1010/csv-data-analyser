# CSV Data Analyser — QA Checklist

- Handle empty files and files containing only headers.
- Detect missing values without silently treating them as zero.
- Test quoted fields containing commas and line breaks.
- Explain when a column cannot be interpreted as numeric.
- Check duplicate headers and inconsistent row lengths.
- Report row and column counts from parsed records.