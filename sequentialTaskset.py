from locust import SequentialTaskSet,constant,task,HttpUser

class MyHTTPcat(SequentialTaskSet):

    def on_start(self):
        print("start")

    def on_stop(self):
        print("stop")

    @task
    def get_200_status(self):
        self.client.get("/200")
        print("Get status of 200")


    @task
    def get_400_status(self):
        self.client.get("/400")
        print("Get status of 400")

class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks=[MyHTTPcat]
    wait_time=constant(1)
