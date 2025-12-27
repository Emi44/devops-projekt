import os
import csv
import json
from datetime import datetime

OUT_DIR = "/seed_output"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    users = [
        {"id": 1, "name": "Emilia"},
        {"id": 2, "name": "Kornelia"},
        {"id": 3, "name": "Liliana"},
        {"id": 4, "name": "Rozalia"},
        {"id": 5, "name": "Beata"},
    ]
    with open(os.path.join(OUT_DIR, "seed.log"), "w", encoding="utf-8") as f:
        f.write(f"Seed gotowy: {datetime.utcnow().isoformat()}Z\n")
        f.write(f"Generuj uzytk.: {len(users)}\n")
    with open(os.path.join(OUT_DIR, "users.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name"])
        for u in users:
            w.writerow([u["id"], u["name"]])
    with open(os.path.join(OUT_DIR, "data.json"), "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
