from locust import TaskSet,constant,task,HttpUser

class MyHTTPcat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")
        self.interrupt(reschedule=False)


class MySecondHttpcat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get status of 500")
        self.interrupt(reschedule=False)

class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks=[MyHTTPcat,MySecondHttpcat]
    wait_time=constant(1)
