import pandas as pd
import numpy as np

print("=" * 50)
print("           CSV DATA ANALYZER")
print("=" * 50)

file = input("\nEnter CSV file name: ")

try:
    df = pd.read_csv(file)
except:
    print("\nError: Could not load the CSV file.")
    exit()

print("\nCSV file loaded successfully!")

while True:

    print("\n" + "=" * 50)
    print("MENU")
    print("=" * 50)
    print("1. Dataset Information")
    print("2. Basic Statistics")
    print("3. Missing Values")
    print("4. Highest and Lowest Values")
    print("5. Filter Data")
    print("6. Summary Report")
    print("7. Display Data")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nDATASET INFORMATION")
        print("-" * 30)
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])
        print("\nColumns:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

    elif choice == "2":

        numeric = df.select_dtypes(include=np.number)

        if numeric.empty:
            print("\nNo numerical columns found.")
        else:
            print("\nBASIC STATISTICS")
            print("-" * 30)
            print("Mean:")
            print(numeric.mean().round(2))

            print("\nMedian:")
            print(numeric.median().round(2))

            print("\nStandard Deviation:")
            print(numeric.std().round(2))

            print("\nMinimum:")
            print(numeric.min())

            print("\nMaximum:")
            print(numeric.max())

    elif choice == "3":

        missing = df.isnull().sum()

        print("\nMISSING VALUES")
        print("-" * 30)
        print(missing)

        total_missing = missing.sum()

        print("\nTotal Missing Values:", total_missing)

    elif choice == "4":

        numeric = df.select_dtypes(include=np.number)

        if numeric.empty:
            print("\nNo numerical columns found.")
        else:

            print("\nHIGHEST AND LOWEST VALUES")
            print("-" * 30)

            for column in numeric.columns:

                print("\nColumn:", column)
                print("Highest:", numeric[column].max())
                print("Lowest:", numeric[column].min())

    elif choice == "5":

        print("\nAVAILABLE COLUMNS:")
        print(list(df.columns))

        column = input("\nEnter column name: ")

        if column not in df.columns:
            print("Column not found.")
            continue

        value = input("Enter value to filter: ")

        result = df[
            df[column].astype(str).str.contains(
                value,
                case=False,
                na=False
            )
        ]

        print("\nFILTERED DATA")
        print("-" * 30)

        if result.empty:
            print("No matching records found.")
        else:
            print(result.to_string(index=False))

    elif choice == "6":

        numeric = df.select_dtypes(include=np.number)

        print("\n" + "=" * 50)
        print("              SUMMARY REPORT")
        print("=" * 50)

        print("\nDataset Size:", df.shape[0], "rows x", df.shape[1], "columns")

        print("\nColumn Names:")
        for column in df.columns:
            print("-", column)

        print("\nMissing Values:")
        print(df.isnull().sum())

        if not numeric.empty:

            print("\nNumerical Summary:")

            for column in numeric.columns:

                print("\n", column)
                print("Mean:", round(numeric[column].mean(), 2))
                print("Median:", round(numeric[column].median(), 2))
                print("Minimum:", numeric[column].min())
                print("Maximum:", numeric[column].max())
                print(
                    "Standard Deviation:",
                    round(numeric[column].std(), 2)
                )

        print("\n" + "=" * 50)

    elif choice == "7":

        print("\nDATA")
        print("-" * 30)

        print(df.to_string(index=False))

    elif choice == "8":

        print("\nThank you for using CSV Data Analyzer!")
        break

    else:

        print("\nInvalid choice. Please try again.")