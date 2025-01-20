import os
from git import Repo
from datetime import datetime

# Get repo path from environment variable, with fallback
local_repo = os.getenv('GIT_REPO_PATH')
#Function to update the date file
def current_date():
    file_path = "date.txt"
    content = f"File updated on {datetime.now()}"
    with open(file_path, 'w') as file:
        file.write(content)
    print("file updated successfully")

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
                print('added')
            
                repo.index.commit(commit_message)
                print('commited changes')

                origin = repo.remote(name='origin')
                origin.push()
                print(f'changes pushed at {datetime.now()}')
            except Exception as e:
                print(f"Error during git operations: {str(e)}")
        else:
            print('no changes to push')
    except Exception as e:
        print(f"Error accessing repository at {local_repo}: {str(e)}")
