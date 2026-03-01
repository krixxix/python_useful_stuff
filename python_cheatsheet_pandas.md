# Python Cheatsheet: pandas

## Creating Data
```python
# From dictionary
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

# From CSV
df = pd.read_csv("file.csv")

# From Excel
df = pd.read_excel("file.xlsx")

# From list of dicts
df = pd.DataFrame([
    {"A": 1, "B": 2},
    {"A": 3, "B": 4}
])
```

## Inspecting Data
```python
df.head(5)        # First 5 rows
df.tail(5)        # Last 5 rows
df.shape          # (rows, columns)
df.columns        # Column names
df.index          # Index
df.info()         # Summary info
df.describe()     # Stats summary
df.dtypes         # Data types
df.sample(3)      # Random rows
```

## Selecting Data

### Select Columns
```python
df["A"]                 # Single column (Series)
df[["A", "B"]]          # Multiple columns
```

### Select Rows
```python
df.loc[0]               # By label
df.iloc[0]              # By position
df.loc[0:3]             # Slice by label
df.iloc[0:3]            # Slice by position
```
### Conditional Filtering
```python
df[df["A"] > 2]
df[(df["A"] > 1) & (df["B"] < 6)]
df.query("A > 1 and B < 6")
```

## Modifying Data
```python
df["C"] = df["A"] + df["B"]   # New column
df.drop("C", axis=1)          # Drop column
df.drop(0, axis=0)            # Drop row

df.rename(columns={"A": "Alpha"})
df.sort_values("A")
df.sort_values("A", ascending=False)

df.reset_index(drop=True)
df.set_index("A")
```

## Handling Missing Data
```python
df.isna()
df.isna().sum()

df.dropna()                   # Drop rows with NA
df.fillna(0)                  # Replace NA
df.fillna(method="ffill")     # Forward fill
```

## Grouping and Aggregation
```python
df.groupby("A").mean()
df.groupby("A")["B"].sum()

df.groupby("A").agg({
    "B": ["mean", "sum"],
    "C": "max"
})
```

## Merging and Joining
```python
pd.merge(df1, df2, on="id", how="inner")
pd.merge(df1, df2, on="id", how="left")
pd.merge(df1, df2, on="id", how="right")
pd.merge(df1, df2, on="id", how="outer")

df1.join(df2, on="id")

pd.concat([df1, df2], axis=0)   # Stack rows
pd.concat([df1, df2], axis=1)   # Stack columns
```

## Applying Functions
```python
df["A"].apply(lambda x: x * 2)

df.apply(np.sum)             # Column-wise
df.apply(np.sum, axis=1)     # Row-wise

df["A"].map({1: "One", 2: "Two"})
```

## Working with String
```python
df["col"].str.lower()
df["col"].str.upper()
df["col"].str.contains("abc")
df["col"].str.replace("a", "b")
df["col"].str.strip()
```

## Working with Dates
```python
df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

df.set_index("date").resample("M").mean()
```

## Pivot Tables
```python
df.pivot(index="A", columns="B", values="C")

df.pivot_table(
    values="C",
    index="A",
    columns="B",
    aggfunc="mean"
)
```

## Exporting Data
```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")
```