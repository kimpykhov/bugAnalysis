from datetime import datetime, timedelta
import random

UPPER_LIMIT_SEC = 2 * 365 * 24 * 3600


# function to calculate random date 2 years ago - creation date
def generate_created_at(now: datetime) -> datetime:
    past_in_sec = random.randint(1, UPPER_LIMIT_SEC)
    return now - timedelta(seconds=past_in_sec)


# function to calculate random date 2 years ago - date when the bug was closed
def generate_closed_at(created_at: datetime) -> datetime:
    delta_sec = random.randint(1, UPPER_LIMIT_SEC)
    return created_at + timedelta(seconds=delta_sec)


# function to calculate time to close the bug
def closed_days(created_at: datetime, closed_at: datetime) -> int:
    delta = closed_at - created_at
    return delta.days