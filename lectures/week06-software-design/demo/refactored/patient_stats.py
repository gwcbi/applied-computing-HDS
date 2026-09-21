"""
AFTER (part 1 of 2): the computation, pulled out into a module.

This is the same logic as monolith_report.py's three copy-pasted blocks
and its BP-flag loop -- but as small, named, reusable functions that don't
know or care that the result is going to be printed. That's the point of
"modular": each piece does one thing and can be tested, reused, or swapped
independently of how it's eventually used.

Nothing in this file prints anything. That's deliberate -- see
generate_report.py for the part that turns these results into the report
a human reads.
"""


def average_age_by_site(patients, site):
    """Return the mean age of patients at a given site.

    Raises ZeroDivisionError if no patients match `site` -- in real code
    you'd likely guard this, but the live demo asks the room to point that
    out rather than silently handling it here.
    """
    ages = [p["age"] for p in patients if p["site"] == site]
    return sum(ages) / len(ages)


def sites_present(patients):
    """Return the distinct site codes in `patients`, in first-seen order."""
    seen = []
    for p in patients:
        if p["site"] not in seen:
            seen.append(p["site"])
    return seen


def high_bp_patients(patients, threshold=140):
    """Return the patients whose systolic_bp is at or above `threshold`."""
    return [p for p in patients if p["systolic_bp"] >= threshold]
