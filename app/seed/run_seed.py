import os
import csv
import json
from datetime import datetime

from src.app import create_app
from src.extensions import db
from src.models import User

OUT_DIR = "/seed_output"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    app = create_app()

    with app.app_context():
        names = ["Emilia", "Kornelia", "Liliana", "Rozalia", "Beata"]
        existing = {u.name for u in User.query.all()}

        for n in names:
            if n not in existing:
                db.session.add(User(name=n))
        db.session.commit()

        users = User.query.order_by(User.id).all()

        with open(os.path.join(OUT_DIR, "seed.log"), "w", encoding="utf-8") as f:
            f.write(f"Seed gotowy: {datetime.utcnow().isoformat()}Z\n")
            f.write(f"Uzytkownicy: {len(users)}\n")

        with open(os.path.join(OUT_DIR, "users.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id", "name"])
            for u in users:
                w.writerow([u.id, u.name])

        with open(os.path.join(OUT_DIR, "data.json"), "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in users], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()