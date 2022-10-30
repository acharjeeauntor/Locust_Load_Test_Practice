from locust import HttpUser,constant,task

class MyReqres(HttpUser):
    host = "https://reqres.in"
    wait_time=constant(1)
    
    def on_start(self):
        print("Start")

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.status_code)
        # print(res.text)

    @task()
    def create_user(self):
        res = self.client.post("/api/users",data='''{"name":"morpheus","job":"leader"}''')
        print(res.status_code)
        # print(res.text)

    def on_stop(self):
        print("Stop")
    