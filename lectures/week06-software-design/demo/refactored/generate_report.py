"""
AFTER (part 2 of 2): the report, now just a thin caller of patient_stats.

Compare this file's length and shape to monolith_report.py. Same output,
same patient data -- but the "what do we compute" logic now lives in one
place (patient_stats.py) instead of being copy-pasted per site, and this
file's only job is turning results into printed text. Ask the room: what
would adding a fourth site cost in each version? (Here: nothing -- the
loop below already handles any number of sites. There: another
copy-pasted block.)

Run it (from this directory):
    python3 generate_report.py
"""

import patient_stats

patients = [
    {"patient_id": "P001", "site": "DC", "age": 54, "systolic_bp": 128},
    {"patient_id": "P002", "site": "MD", "age": 61, "systolic_bp": 146},
    {"patient_id": "P003", "site": "DC", "age": 47, "systolic_bp": 118},
    {"patient_id": "P004", "site": "VA", "age": 72, "systolic_bp": 151},
    {"patient_id": "P005", "site": "MD", "age": 39, "systolic_bp": 122},
    {"patient_id": "P006", "site": "DC", "age": 58, "systolic_bp": 137},
]

for site in patient_stats.sites_present(patients):
    avg = patient_stats.average_age_by_site(patients, site)
    n = len([p for p in patients if p["site"] == site])
    print(f"{site} average age: {avg:.1f} (n={n})")

print("\nHigh BP flags (systolic >= 140):")
for p in patient_stats.high_bp_patients(patients):
    print(f"  {p['patient_id']} ({p['site']}): {p['systolic_bp']}")
