from datetime import date, timedelta

def from_to():
    to = date.today()
    from_ = to - timedelta(days=7)
    return from_, to
