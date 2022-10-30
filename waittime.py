import time
from locust import User,task,constant,between,constant_pacing

class MyUser(User):

    # wait_time = constant(5)

    # @task
    # def launch(self):
    #     print("This will inject 5 seconds delay")

    # wait_time = between(2,5)

    # @task
    # def launch(self):
    #     print("This will inject 2-5 seconds delay")

    wait_time = constant_pacing(5)

    @task
    def launch(self):
        time.sleep(3)
        print("Constant Pacing Demo")