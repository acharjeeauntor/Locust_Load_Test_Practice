import random
from locust import TaskSet,constant,task,HttpUser

class MyHTTPcat(TaskSet):

    def on_start(self):
        print("start")
    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")

    def on_stop(self):
        print("stop")

    @task
    def get_random_status(self):
        status_codes=[100,101,102,405]
        random_url="/"+str(random.choice(status_codes))
        self.client.get(random_url)
        print("Random Http Status")

class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks=[MyHTTPcat]
    wait_time=constant(1)
