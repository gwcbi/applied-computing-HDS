"""Generator for Lab 3 synthetic messy data. Deterministic (seeded) so
outputs can be regenerated/verified against messy_samples.csv and
messy_sequences.fasta. See SOURCE.md."""
import random
import csv
import datetime

def gen_samples_csv(path, n=60, seed=42):
    random.seed(seed)
    names = ["Smith", "Garcia", "Lee", "Patel", "Nguyen", "Johnson", "Kim", "Brown", "Davis", "Martinez"]
    first = ["A.", "B.", "J.", "M.", "S.", "R.", "T.", "K."]
    sexes = ["M", "F", "Male", "Female", "m", "f", "U", "unknown"]
    date_formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%m.%d.%y"]
    sites = ["Site A", "site_a", "SITE-A", "Site B", "siteB", "Site  C", "Site C "]
    units = ["mg/dL", "mg/dl", "MG/DL", "mmol/L"]

    rows = [["sample_id", "patient_name", "dob", "sex", "enrollment_site",
              "glucose_value", "glucose_unit", "notes"]]
    for i in range(1, n + 1):
        sid = f"S{i:04d}" if random.random() > 0.1 else f"s-{i:04d}"
        name = f"{random.choice(first)} {random.choice(names)}"
        if random.random() < 0.05:
            name = name.upper()
        dob = datetime.date(1950, 1, 1) + datetime.timedelta(days=random.randint(0, 25000))
        dob_str = dob.strftime(random.choice(date_formats))
        sex = random.choice(sexes)
        if random.random() < 0.07:
            sex = ""
        site = random.choice(sites)
        glucose = round(random.uniform(70, 250), 1)
        unit = random.choice(units)
        notes = "re-draw requested" if random.random() < 0.08 else ""
        if random.random() < 0.05:
            glucose_str = "N/A"
        elif random.random() < 0.05:
            glucose_str = f"{glucose}*"
        else:
            glucose_str = str(glucose)
        rows.append([sid, name, dob_str, sex, site, glucose_str, unit, notes])

    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def gen_fasta(path, seed=7):
    random.seed(seed)
    bases = "ACGT"
    def seq(n):
        return "".join(random.choice(bases) for _ in range(n))

    headers = [
        ">sample_001|organism=Homo_sapiens|gene=BRCA1|len=120",
        ">Sample002 organism:Homo sapiens gene:TP53",
        ">sample-003 | Homo_sapiens | EGFR | length=150bp",
        ">SAMPLE_004;species=H.sapiens;target=BRCA1",
        ">sample005 Homo sapiens; TP53; 130 bp",
        ">seq6|Hsapiens|EGFR",
        ">Sample_007 organism=Homo_sapiens|gene=BRCA1|note:re-sequenced",
        ">sample-8 species:Homo_sapiens gene:TP53 len:NA",
    ]
    with open(path, "w") as f:
        for h in headers:
            f.write(h + "\n")
            s = seq(random.randint(100, 160))
            for i in range(0, len(s), 60):
                f.write(s[i:i + 60] + "\n")


if __name__ == "__main__":
    gen_samples_csv("messy_samples.csv")
    gen_fasta("messy_sequences.fasta")
    print("Regenerated messy_samples.csv and messy_sequences.fasta")
