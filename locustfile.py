from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    sleep_seconds = 0.05

    # @task
    # def requests_async(self):
    #     self.client.get("/requests_async", params={"seconds": self.sleep_seconds})

    # @task
    # def requests_sync(self):
    #     self.client.get("/requests_sync", params={"seconds": self.sleep_seconds})

    # @task
    # def requests_to_thread_async(self):
    #     self.client.get(
    #         "/requests_to_thread_async", params={"seconds": self.sleep_seconds}
    #     )

    @task
    def aiohttp_async(self):
        self.client.get("/aiohttp_async", params={"seconds": self.sleep_seconds})
