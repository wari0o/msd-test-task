# msd-test-task
1. Create a microservice where a client will be able to retrieve the current price of Bitcoin (BTC) in both EUR and CZK
   1. the output should include both prices per 1 BTC, the currency, the client request’s time, and the server data’s time, if available;
   2. the output format will be JSON;
   3. retrieve fresh source data from here: https://api.coindesk.com/v1/bpi/currentprice.json;
   4. use any programing language you are familiar with.

2. Containerize the microservice.
3. Prepare a deployment into Kubernetes
   1. the deployment should be reproducible;
   2. the microservice should auto-start and be reachable via appropriate calls (example: curl);
   3. use any tool you want for the deployment.
4. Store all the codebase on GitHub a. and share the link for the repository.
5. Any extension to the requirements is welcome, as are any adequate code comments.
6. You can use any resource, tool, method, etc.
7. A partial solution is also fine. If not everything works 100%, we are still interested in reviewing the solution.
8. You can ask us any questions about the requirements and the expected solution.

# How to run?
Run command "kubectl apply -f .\kubernetes\" 

Service will be available at port 80.

# Service endpoints
1. / - get current BTC to EUR and CZK rates;
2. /history - request history;
3. /docs - swagger.

# Dockerhub link
https://hub.docker.com/repository/docker/wari0o/msd-test-task
