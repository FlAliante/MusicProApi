from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def get_tipo_productos(self):
        self.client.get('/api/get_productos?tipo_producto=1')


    @task
    def get_productos(self):
        self.client.get('/api/get_productos')


    @task
    def exchange_rate(self):
        self.client.get('/api/exchange_rate')
