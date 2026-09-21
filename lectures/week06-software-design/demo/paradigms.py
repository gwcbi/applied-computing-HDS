"""
Same task, three paradigms: procedural, object-oriented, functional.

Task: given a list of patients (each with a BMI), print each patient's
weight-status category ("underweight" / "normal" / "overweight" / "obese"
per the standard WHO adult BMI cutoffs) alongside their ID.

This is NOT "which paradigm is correct" -- Python supports all three, and
real Python code mixes them constantly. The point is to *recognize* a
paradigm when reading someone else's code, and to notice what each one
optimizes for:
  - procedural: a sequence of steps, top to bottom. Simple to write once,
    but state (the accumulating `results` list) is mutated in place as
    you go.
  - object-oriented: data and the behavior that acts on it are bundled
    together in a class. Good when "a patient" is a recurring concept
    you'll attach more behavior to over time.
  - functional: small pure functions (same input -> same output, no
    mutation, no side effects) composed together, often via map/filter/
    comprehensions. Good when you want each step to be independently
    testable and order-independent.

Live-demo script for Week 6 -- lecture segment 2, "Software design
paradigms." Run each section, or the whole file:
    python3 paradigms.py
"""

patients = [
    {"patient_id": "P001", "bmi": 17.8},
    {"patient_id": "P002", "bmi": 22.4},
    {"patient_id": "P003", "bmi": 27.1},
    {"patient_id": "P004", "bmi": 33.6},
]


# --------------------------------------------------------------------
# 1. Procedural -- a sequence of steps operating on shared state
# --------------------------------------------------------------------
def bmi_category_procedural(patients):
    results = []
    for p in patients:
        bmi = p["bmi"]
        if bmi < 18.5:
            category = "underweight"
        elif bmi < 25:
            category = "normal"
        elif bmi < 30:
            category = "overweight"
        else:
            category = "obese"
        results.append((p["patient_id"], category))
    return results


# --------------------------------------------------------------------
# 2. Object-oriented -- data + behavior bundled into a class
# --------------------------------------------------------------------
class Patient:
    """A patient record that knows how to classify its own BMI."""

    def __init__(self, patient_id, bmi):
        self.patient_id = patient_id
        self.bmi = bmi

    def bmi_category(self):
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "overweight"
        else:
            return "obese"

    def __repr__(self):
        return f"Patient({self.patient_id!r}, bmi={self.bmi})"


def bmi_category_oop(patients):
    patient_objs = [Patient(p["patient_id"], p["bmi"]) for p in patients]
    return [(p.patient_id, p.bmi_category()) for p in patient_objs]


# --------------------------------------------------------------------
# 3. Functional -- small pure functions, composed, no mutation
# --------------------------------------------------------------------
def classify_bmi(bmi):
    """Pure function: same bmi in, same category out, every time."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def bmi_category_functional(patients):
    return [(p["patient_id"], classify_bmi(p["bmi"])) for p in patients]
    # Equivalent one-liner some students will reach for:
    # return list(map(lambda p: (p["patient_id"], classify_bmi(p["bmi"])), patients))


if __name__ == "__main__":
    print("Procedural:", bmi_category_procedural(patients))
    print("OOP:       ", bmi_category_oop(patients))
    print("Functional:", bmi_category_functional(patients))
