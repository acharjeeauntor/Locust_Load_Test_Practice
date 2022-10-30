from locust import HttpUser,constant,task

class MyReqres(HttpUser):
    wait_time=constant(1)


    @task
    def get_users(self):
        self.client.get("/api/users?page=2")