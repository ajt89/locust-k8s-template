from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 1)

    @task
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

    @task
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

    @task
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
