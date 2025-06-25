import logging
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

# Scheduler setup
scheduler = BlockingScheduler()

if __name__ == "__main__":
    # Schedule job every 10 seconds
    scheduler.add_job(sample_job, 'interval', seconds=10)
    
    logging.info("Scheduler started.")
    print("Scheduler started. Press Ctrl+C to exit.")
    
    try:
        scheduler.start()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped.")
        print("\nScheduler stopped.")