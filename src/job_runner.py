import logging
import shutil
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# Configure logging
logging.basicConfig(
    filename='logs/job_runner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Sample job function
def sample_job():
    print("Running sample job...")
    try:
        result = "Success"
    except Exception as e:
        result = f"Failed: {str(e)}"
    
    logging.info(f"Job executed at {datetime.now()} — Result: {result}")
    print(f"Job executed at {datetime.now()} — Result: {result}")

# Check disk usage job
def check_disk_usage():
    print("Running disk usage check...")
    try:
        total, used, free = shutil.disk_usage("/")
        usage_percent = (used/total) * 100
        message = f"Disk usage: {usage_percent:.2f}% used | Total: {total//(2**30)} GB"
        logging.info(message)
        print(message)
    except Exception as e:
        error_msg = f"Disk usage check failed: {str(e)}"
        logging.error(error_msg)
        print(error_msg)

# Scheduler setup
scheduler = BlockingScheduler()

if __name__ == "__main__":
    # Schedule job every 7 seconds
    scheduler.add_job(sample_job, 'interval', seconds=7)
    scheduler.add_job(check_disk_usage, 'interval', minutes=1)
    
    logging.info("Scheduler started.")
    print("Scheduler started. Press Ctrl+C to exit.")
    
    try:
        scheduler.start()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped.")
        print("\nScheduler stopped.")