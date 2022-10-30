from locust import HttpUser,constant,task

class MyReqres(HttpUser):
    wait_time=constant(1)
    
    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host


    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2",name=self.hostname)
        print(res.status_code)
        # print(res.text)
    