# Locust Kubernetes Template

Ideally this repo should show how to setup a "perf" namespace to generate load and test the "stage" namespace all in the wonderful world of kubernetes. All work done has been done in minikube.

TODO:
1. Get locust deployment to send load at flask deployment

STRETCH GOALS:
1. Implement with minishift?

DONE:
1. ~~Create simple flask service to be tested~~
2. ~~Dockerize flask service~~
3. ~~Create simple locust test~~
4. ~~Dockerize locust test~~
5. ~~Create stage and perf k8s namespaces~~
6. ~~Create k8s deployment for the flask service~~
7. ~~Create k8s deployments for the locust test~~
8. ~~Create k8s config map for the locust test~~
9. ~~~Figure out k8s services~~