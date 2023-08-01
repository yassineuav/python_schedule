import schedule
from datetime import time, timedelta, datetime
from schedule import every, repeat
import time as tm


@repeat(every().hour)
def task():
    print("push to github")


# schedule.every().hour.do(task)

while True:
    schedule.run_pending()
    tm.sleep(1)