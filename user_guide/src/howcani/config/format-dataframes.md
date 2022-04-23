# Formatting DataFrames

To configure how your `DataFrame` prints, use `polars.cfg.Config`.

## Printing

By default your `DataFrame` will print with a collapsed view of its data.

```python
{{#include ../../examples/config/print1.py}}
```

```text
{{#include ../../outputs/config/print1.txt}}
```

Use `Config` to print all of the columns.

```python
{{#include ../../examples/config/print2.py}}
```

```text
{{#include ../../outputs/config/print2.txt}}
```

Check the [API Reference](POLARS_PY_REF_GUIDE/config.html) for more on printing configuration.
