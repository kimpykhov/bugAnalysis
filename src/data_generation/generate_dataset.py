import csv
from pathlib import Path
import random
from datetime import datetime

import distibutions
from time_logic import past_date, future_date

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "bugs_synthetic.csv"

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["bug_id", "created_at", "closed_at", "priority", "severity", "component", "assignee_id", "labels",
                     "summary", "description"])
    now = datetime.now()
    for i in range(1, 11, 1):
        created_at = past_date()
        closed_at = future_date(created_at)
        writer.writerow([i, created_at, closed_at, random.choice(distibutions.priority),
                         random.choice(distibutions.severity), random.choice(distibutions.component),
                         random.choice(distibutions.users), random.choice(distibutions.labels),
                         "fakesummary", "interim"])