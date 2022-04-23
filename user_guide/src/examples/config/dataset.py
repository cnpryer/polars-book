import polars as pl
import numpy as np

n = 10

df = pl.DataFrame([list(range(n))], columns=list(map(str, range(n))))


def full_str(dataframe: pl.DataFrame) -> str:
    pl.Config.set_tbl_cols(n)

    return dataframe.__str__()
