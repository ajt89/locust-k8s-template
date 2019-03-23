from locust import TaskSet

from tasks.a_tasks import ATasks


class TaskSetA(TaskSet):

    def on_start(self):
        self.a_tasks = ATasks(self.client)

    def index(self):
        self.a_tasks.index()

    def route_a(self):
        self.a_tasks.route_a()

    def route_b(self):
        self.a_tasks.route_b()

    tasks = {
        index: 1,
        route_a: 2,
        route_b: 1,
    }
