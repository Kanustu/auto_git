import os
from git import Repo
from datetime import datetime
import logging

#Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)

# Get repo path from environment variable, with fallback
local_repo = os.getenv('GIT_REPO_PATH')
#Function to update the date file
def current_date():
    file_path = "date.txt"
    content = f"File updated on {datetime.now()}"
    with open(file_path, 'w') as file:
        file.write(content)
    

#Function to commit and push changes to the remote repo
def git_upload():
    try:
        #Open the local repo
        repo = Repo(local_repo)
        #Commit message
        commit_message = f"daily update completed on {datetime.now()}"
        #Check if there are changes to commit
        if repo.is_dirty():
            try:
                repo.git.add('--all')
                
            
                repo.index.commit(commit_message)
                

                origin = repo.remote(name='origin')
                origin.push()
                
            except Exception as e:
                print(f"Error during git operations: {str(e)}")
                logging.error(f"Error during git operations: {str(e)}")
        else:
            print('no changes to push')
    except Exception as e:
        print(f"Error accessing repository at {local_repo}: {str(e)}")
        logging.error(f"Error accessing repository at {local_repo}: {str(e)}")
