from datetime import datetime
from dateutil.relativedelta import relativedelta

# pip install python-dateutil
if __name__ == "__main__":
    d1 = datetime.utcnow()
    d2 = datetime.utcnow().replace(day=10)
    d = d1 - relativedelta(days=2)
    print(d)
