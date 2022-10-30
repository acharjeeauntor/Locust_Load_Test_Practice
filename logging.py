from locust import User,task,constant
import logging

class MyFirstTest(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL")
        logging.info("This is logging info")

    @task
    def search(self):
        print("Searching")
        logging.error("If there error, this will show")
    

# Sample cmd: locust -f logging.py -u 1 -r 1 -t 10s --headless --logfile mylog.log --only-summary
# All the logging record will be store in the mylog.log file

