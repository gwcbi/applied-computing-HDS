import sqlite3, random, os
random.seed(11)

path = os.path.join(os.path.dirname(__file__), "clinic.db")
if os.path.exists(path):
    os.remove(path)
conn = sqlite3.connect(path)
c = conn.cursor()

c.execute("""CREATE TABLE sites (
    site_id INTEGER PRIMARY KEY,
    site_name TEXT NOT NULL,
    city TEXT,
    state TEXT
)""")
c.execute("""CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    site_id INTEGER REFERENCES sites(site_id),
    sex TEXT,
    birth_year INTEGER
)""")
c.execute("""CREATE TABLE visits (
    visit_id INTEGER PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    visit_date TEXT,
    visit_type TEXT
)""")
c.execute("""CREATE TABLE lab_results (
    result_id INTEGER PRIMARY KEY,
    visit_id INTEGER REFERENCES visits(visit_id),
    analyte TEXT,
    value REAL,
    unit TEXT
)""")

sites = [(1,"Foggy Bottom Clinic","Washington","DC"),
         (2,"Riverside Health Center","Alexandria","VA"),
         (3,"Northside Family Practice","Rockville","MD")]
c.executemany("INSERT INTO sites VALUES (?,?,?,?)", sites)

patient_rows = []
for pid in range(1, 41):
    site_id = random.choice([1,2,3])
    sex = random.choice(["M","F"])
    byear = random.randint(1945, 2005)
    patient_rows.append((pid, site_id, sex, byear))
c.executemany("INSERT INTO patients VALUES (?,?,?,?)", patient_rows)

visit_rows = []
vid = 1
for pid in range(1, 41):
    for _ in range(random.randint(1,3)):
        year = random.randint(2022,2026)
        month = random.randint(1,12)
        day = random.randint(1,28)
        vtype = random.choice(["annual","follow-up","urgent"])
        visit_rows.append((vid, pid, f"{year:04d}-{month:02d}-{day:02d}", vtype))
        vid += 1
c.executemany("INSERT INTO visits VALUES (?,?,?,?)", visit_rows)

analytes = [("glucose","mg/dL",(70,220)), ("hba1c","%",(4.5,10.5)),
            ("ldl","mg/dL",(60,190)), ("systolic_bp","mmHg",(95,170))]
result_rows = []
rid = 1
for (visit_id, *_ ) in visit_rows:
    n_tests = random.randint(1,3)
    for analyte, unit, (lo,hi) in random.sample(analytes, n_tests):
        val = round(random.uniform(lo,hi),1)
        result_rows.append((rid, visit_id, analyte, val, unit))
        rid += 1
c.executemany("INSERT INTO lab_results VALUES (?,?,?,?,?)", result_rows)

conn.commit()
conn.close()
print("sites", len(sites), "patients", len(patient_rows), "visits", len(visit_rows), "results", len(result_rows))
