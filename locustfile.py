from locust import HttpLocust

from task_sets.task_set_a import TaskSetA


class WebsiteUserA(HttpLocust):
    task_set = TaskSetA
    min_wait = 1000
    max_wait = 1000
