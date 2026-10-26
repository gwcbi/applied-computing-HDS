"""Generate a small SYNTHETIC mutation dataset (6 samples) for the Week 10 demo.
Not real patient data. Seeded so everyone gets identical files."""
import random
from pathlib import Path

random.seed(2026)
GENES = ["KRAS", "EGFR", "TP53", "STK11", "KEAP1", "BRAF", "PTEN", "ALK"]
CLASSES = ["Missense", "Nonsense", "Frameshift", "Silent"]
out = Path("data/raw")
out.mkdir(parents=True, exist_ok=True)

for i in range(1, 7):
    sample = f"S{i:02d}"
    with open(out / f"{sample}.tsv", "w") as f:
        f.write("gene\tvariant_class\tvaf\n")
        for _ in range(random.randint(25, 40)):
            f.write(f"{random.choice(GENES)}\t{random.choice(CLASSES)}\t{random.random():.3f}\n")
print("wrote 6 files to", out)
