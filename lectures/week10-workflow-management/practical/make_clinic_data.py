"""Generate SYNTHETIC multi-site clinic data for the Week 10 practical.
Not real patient data. Seeded so everyone gets identical files."""
import random
from pathlib import Path

random.seed(1028)
out = Path("data/sites")
out.mkdir(parents=True, exist_ok=True)

for site in ["A", "B", "C", "D", "E"]:
    n = random.randint(60, 120)
    with open(out / f"{site}.tsv", "w") as f:
        f.write("patient_id\tage\tsbp\thba1c\n")
        for i in range(n):
            age = random.randint(30, 85)
            sbp = random.gauss(128, 18)
            a1c = random.gauss(6.2, 1.1)
            # sprinkle in data-entry errors the cleaning step must catch
            if random.random() < 0.04:
                age = random.choice([0, 150, 999])
            if random.random() < 0.04:
                sbp = random.choice([0, 20, 400])
            f.write(f"{site}{i:03d}\t{age}\t{sbp:.0f}\t{a1c:.1f}\n")
print("wrote 5 site files to", out)
