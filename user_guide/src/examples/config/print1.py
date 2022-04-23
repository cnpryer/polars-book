import polars as pl

n = 10

df = pl.DataFrame([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], columns=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

print(df)
