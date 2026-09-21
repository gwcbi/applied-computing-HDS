"""Summary statistics for toy patient records.

This module exists for Week 7's packaging + debugging exercise. It is
intentionally tiny -- one function, one planted bug -- so the point of the
exercise is finding and fixing the bug with a real debugger, not reading a
lot of code.
"""

from __future__ import annotations


def summarize_by_site(records: list[dict], _cache: dict = {}) -> dict:
    """Group patient lab values by site and return the mean value per site.

    Parameters
    ----------
    records:
        A list of dicts, each with a ``"site"`` key (str) and a ``"value"``
        key (float) -- e.g.
        ``[{"site": "DC", "value": 4.2}, {"site": "VA", "value": 3.9}]``.

    Returns
    -------
    dict
        Mapping of site -> mean value.
    """
    for record in records:
        _cache.setdefault(record["site"], []).append(record["value"])
    return {site: sum(values) / len(values) for site, values in _cache.items()}
