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

def current_date():
    """
    Updates the 'date.txt' file with the current date and time.

    This function performs the following actions:
    1. Retrieves the current date and time using `datetime.now()`.
    2. Formats the retrieved date and time into a string with the prefix 'File updated on '.
    3. Opens (or creates if it doesn't exist) a file named 'date.txt' in write mode.
    4. Writes the formatted date and time string to the file, overwriting any existing content.

    Example:
        After execution, 'date.txt' might contain:
        File updated on 2023-10-05 14:30:25.123456

    Returns:
        None
    """
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


def git_upload():
        """
        Commits and pushes changes to the local Git repository.

        This function performs the following actions:
        
        1. **Access the Local Repository**:
           - Opens the Git repository located at the path specified by `local_repo`.
        
        2. **Prepare Commit Message**:
           - Generates a commit message incorporating the current date and time, e.g., 
             "daily update completed on 2023-10-05 14:30:25.123456".
        
        3. **Check for Changes**:
           - Determines if there are any uncommitted changes in the repository using `repo.is_dirty()`.
        
        4. **Commit and Push Changes** *(if changes exist)*:
           - **Stage All Changes**: Adds all modified and new files to the staging area using `repo.git.add('--all')`.
           - **Commit Changes**: Commits the staged changes with the prepared commit message.
           - **Push to Remote**: Pushes the committed changes to the remote repository named 'origin'.
        
        5. **Error Handling**:
           - Catches and handles exceptions that may occur while accessing the repository or performing Git operations.
           - Logs error messages using the `logging` module and prints error details to the console.
        
        **Exceptions Handled**:
        
        - **Repository Access Errors**:
          - Occur when the function fails to access the repository at `local_repo`. Possible reasons include an incorrect path or lack of permissions.
        
        - **Git Operation Errors**:
          - Occur during staging, committing, or pushing changes. Possible reasons include merge conflicts, authentication issues, or network problems.
        """
        try:
            # Open the local repo
            repo = Repo(local_repo)
            # Commit message
            commit_message = f"daily update completed on {datetime.now()}"
            # Check if there are changes to commit
            if repo.is_dirty():
                try:
                    repo.git.add('--all')
                    repo.index.commit(commit_message)
                    origin = repo.remote(name='origin')
                    origin.push()
                except Exception as e:
                    logging.error(f"Error during git operations: {str(e)}")
        except Exception as e:
            logging.error(f"Error accessing repository at {local_repo}: {str(e)}")
    

