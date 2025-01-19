#Import Libraries
import schedule
import time
from git_functions import current_date, git_upload

schedule.every().hour.do(current_date)
schedule.every().hour.do(git_upload)

while True:
    schedule.run_pending()
    time.sleep(60)
