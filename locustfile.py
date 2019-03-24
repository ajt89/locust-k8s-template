from locust import HttpLocust, TaskSet


class UserBehavior(TaskSet):

    def index(self):
        url = '/'
        name = 'index'
        catch_response = True

        response = self.client.get(
            url,
            name=name,
            catch_response=catch_response,
        )

        if 'index' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')

    def route_a(self):
        url = '/a'
        name = 'route_a'
        catch_response = True

        response = self.client.get(
            url,
            name=name,
            catch_response=catch_response,
        )

        if 'route_a' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')

    def route_b(self):
        url = '/b'
        name = 'route_b'
        catch_response = True

        response = self.client.get(
            url,
            name=name,
            catch_response=catch_response,
        )

        if 'route_b' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')

    tasks = {
        index: 1,
        route_a: 2,
        route_b: 1,
    }


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
