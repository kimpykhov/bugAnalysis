import csv
from pathlib import Path
import random
from datetime import datetime

from data_generation import distributions
from time_logic import generate_closed_at, generate_created_at, closed_days

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "bugs_synthetic.csv"

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["bug_id", "created_at", "closed_at", "days_to_close", "priority", "severity", "component",
                     "assignee_id", "labels", "summary", "description"])
    now = datetime.now()
    for i in range(1, 11, 1):
        created_at = generate_created_at(now)
        closed_at = generate_closed_at(created_at)
        days = closed_days(created_at, closed_at)
        label_amount = random.randint(1, 4)

        writer.writerow([i, created_at, closed_at, days,
                         random.choices(distributions.priority, weights=distributions.weights_priority, k=1),
                         random.choices(distributions.severity, weights=distributions.weights_severity, k=1),
                         random.choice(distributions.component),
                         random.choice(distributions.users),
                         random.choices(distributions.labels, weights=distributions.weights_labels, k=label_amount),
                         "fakesummary", "interim1"])