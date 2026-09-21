# `patientkit` — Week 7 packaging + debugging starter

A minimal, installable Python package with one planted bug, used in the Week
7 practical (Oct 7) packaging/debugging exercise. Not a real analysis
package — deliberately tiny, so the exercise is about the *process*
(install it, break it, debug it with a real debugger), not about reading a
lot of unfamiliar code.

## Install it (editable mode)

```console
$ cd python-starter
$ pip install -e .
```

## See the bug

```console
$ python demo_bug.py
```

You should see `'DC'` show up in the *second* call's output, even though
the second call's input never mentions a DC site. That's the bug.

## The exercise

See [`../practical.md`](../practical.md) for the full walk-through: install
the package, reproduce the bug, use your IDE's debugger (breakpoint +
step-through + variable inspection — not print statements) to find it, then
fix `src/patientkit/stats.py` so each call to `summarize_by_site()` is
independent of the ones before it.
