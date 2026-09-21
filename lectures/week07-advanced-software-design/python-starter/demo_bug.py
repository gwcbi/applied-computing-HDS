"""Run this to see the planted bug in action.

Expected (correct) behavior: calling summarize_by_site() with two different
batches of patient records should return two independent summaries -- the
second call's numbers should not be influenced by data passed to an earlier
call.

What actually happens: run this script and look at `second_summary`. It
still contains the "DC" site from the *first* call, and "VA"'s mean is
averaged across data from both calls, even though `second_batch` below has
only one VA record. No error, no warning -- just a wrong (contaminated)
answer, the same "confident but wrong" failure mode this course has flagged
since Week 4.

Debugging exercise (see ../practical.md): set a breakpoint inside
summarize_by_site() (in stats.py), step through both calls, and inspect
`_cache` before and after each call. Once you see what's happening, fix
stats.py so each call is independent -- don't just delete the docstring or
work around the symptom here in this script.
"""

from patientkit import summarize_by_site

first_batch = [
    {"site": "DC", "value": 4.2},
    {"site": "DC", "value": 3.8},
]
first_summary = summarize_by_site(first_batch)
print("First call:", first_summary)

second_batch = [
    {"site": "VA", "value": 5.0},
]
second_summary = summarize_by_site(second_batch)
print("Second call:", second_summary)
print("Bug check: 'DC' should NOT appear in the second call's output.")
