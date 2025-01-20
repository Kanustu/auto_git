# Import Libraries
import schedule
import time
import logging
import signal
import sys
from git_functions import current_date, git_upload

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)

# Schedule interval in hours
SCHEDULE_INTERVAL = 6


def main():
    """Main function to set up and run the automation schedule"""
    logging.info("Starting automation script...")
    

    # Schedule jobs with error handling
    schedule.every(SCHEDULE_INTERVAL).hours.do(current_date)
    schedule.every(SCHEDULE_INTERVAL).hours.do(git_upload)

    while True:
        try:
            schedule.run_pending()
            time.sleep(60)
        except Exception as e:
            logging.error(f"Error in main loop: {str(e)}")
            time.sleep(60)  # Continue running even if there's an error

if __name__ == "__main__":
    main()
