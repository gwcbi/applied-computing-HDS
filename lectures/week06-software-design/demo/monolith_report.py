"""
BEFORE: a monolithic script, written the way a first draft usually looks.

This "reads" a clinic roster and prints a per-site summary plus a
high-blood-pressure flag list. It works. The problem isn't correctness --
it's that every piece of logic is welded to *this specific report*, at the
top level of the script, with no boundary between "get the data," "compute
something," and "print it."

Live-demo script for Week 6 (Software Design) -- lecture segment 3,
"Modular programming." Walk through this file top to bottom, ask the room
what would happen if:
  - we needed this same per-site average for a *different* report
  - we wanted to unit-test "is this patient high BP" without printing
  - the roster grew from 3 sites to 30
...then open refactored/patient_stats.py + refactored/generate_report.py
and show the same output produced a different way.

Run it:
    python3 monolith_report.py
"""

patients = [
    {"patient_id": "P001", "site": "DC", "age": 54, "systolic_bp": 128},
    {"patient_id": "P002", "site": "MD", "age": 61, "systolic_bp": 146},
    {"patient_id": "P003", "site": "DC", "age": 47, "systolic_bp": 118},
    {"patient_id": "P004", "site": "VA", "age": 72, "systolic_bp": 151},
    {"patient_id": "P005", "site": "MD", "age": 39, "systolic_bp": 122},
    {"patient_id": "P006", "site": "DC", "age": 58, "systolic_bp": 137},
]

# --- Per-site average age: DC ---
dc_ages = []
for p in patients:
    if p["site"] == "DC":
        dc_ages.append(p["age"])
dc_avg = sum(dc_ages) / len(dc_ages)
print(f"DC average age: {dc_avg:.1f} (n={len(dc_ages)})")

# --- Per-site average age: MD  (copy-pasted from the DC block above,
#     three-letter site code swapped -- this duplication is the tell) ---
md_ages = []
for p in patients:
    if p["site"] == "MD":
        md_ages.append(p["age"])
md_avg = sum(md_ages) / len(md_ages)
print(f"MD average age: {md_avg:.1f} (n={len(md_ages)})")

# --- Per-site average age: VA  (copy-pasted again) ---
va_ages = []
for p in patients:
    if p["site"] == "VA":
        va_ages.append(p["age"])
va_avg = sum(va_ages) / len(va_ages)
print(f"VA average age: {va_avg:.1f} (n={len(va_ages)})")

# --- High blood pressure flag list (>= 140 systolic) ---
print("\nHigh BP flags (systolic >= 140):")
for p in patients:
    if p["systolic_bp"] >= 140:
        print(f"  {p['patient_id']} ({p['site']}): {p['systolic_bp']}")
