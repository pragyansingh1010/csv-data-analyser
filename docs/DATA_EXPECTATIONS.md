# Data Expectations

The tool works best with a valid, rectangular CSV dataset with a header row.

- Numeric columns are analyzed with NumPy/Pandas numeric operations.
- Missing values are reported rather than silently removed.
- Filter input is treated as text so it can also work with non-numeric columns.
- Very large CSV files may require more memory than small datasets.
