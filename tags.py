from locust import User,task,constant,tag

class MyFirstTest(User):
    wait_time = constant(1)

    @task
    @tag('app','text')
    def launch(self):
        print("Launching the URL")


    @task
    @tag('first','text')
    def search(self):
        print("Searching")
    
    @task
    @tag('second','text')
    def launch2(self):
        print("Launching the URL - 2")

    @task
    @tag('app','text')
    def search2(self):
        print("Searching - 2")


