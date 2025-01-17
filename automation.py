from git import Repo
from datetime import datetime
import schedule
import time

local_repo = "/Users/jordankanius/automation/automated_update"
commit_message = f"daily update completed on {datetime.now()}"

def current_date():
    file_path = "date.txt"
    content = f"File updated on {datetime.now()}"
    with open(file_path, 'w') as file:
        file.write(content)
    print("file updated successfully")


def git_upload():
    repo = Repo(local_repo)
    if repo.is_dirty():
        repo.git.add('--all')
        print('added')
    
        repo.index.commit(commit_message)
        print('commited changes')

        origin = repo.remote(name='origin')
        origin.push()
        print(f'changes pushed at {datetime.now()}')
    else:
        print('no changes to push')
       
schedule.every().day.at("13:22").do(current_date)
schedule.every().day.at("13:22").do(git_upload)

while True:
    schedule.run_pending()
    #time.sleep(3600)
