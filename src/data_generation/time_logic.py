from datetime import datetime, timedelta
import random

now = datetime.now()
upperLimit = 2 * 365 * 24 * 3600


# function to calculate random date 2 years ago - creation date
def past_date():
    past_in_sec = random.randint(1, upperLimit)
    past_date = now - timedelta(seconds=past_in_sec)
    return past_date


# function to calculate random date 2 years ago - date when the bug was closed
def future_date(past_date):
    future_date = past_date + timedelta(seconds=random.randint(1, upperLimit))
    return future_date


pd = past_date()
fd = future_date(pd)
