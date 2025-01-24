# omasjl

`omasjl` is an experimental Python package that in combination with `OMAS.jl` package, exposes the functionality of `IMAS.jl` to Python.

The idea is that `omasjl.ODS()` is a class that exactly mirrors the API and functionality of the `omas.ODS()`.

```python
import omasjl

ods = omasjl.ODS()

ods["equilibrium.time"] = [1.0]
```