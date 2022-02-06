# A Flask Web API with GraphQL

We use [Ariadne](https://ariadnegraphql.org/) + [Flask](https://flask.palletsprojects.com/) to build a Graphql API demo.

## Preparation

We use [batect](https://batect.dev/) to build development environment.

- Run this command to check this project works for you. 

```sh
$ ./batect shell
```

- Check all available tasks:

```sh
$ ./batect --list-tasks
```

## Demo

Let’s create a simple GraphQL API with Ariadne that returns a list of destinations to visit. 

Create 3 separated applications to track  the implementation steps.

### 1. Uvicorn serves a simple GraphQL API

[Uvicorn](https://www.uvicorn.org/), an ASGI server, serves a GraphQL API

```sh
$ ./batect uvicorn_app
```

### 2. Integrating Ariadne with Flask

Implement the same functionality using Flask. We need to add two routes that will be handling two functionalities, which were previously being handled by the inbuilt ASGI web server. 

This includes:
- a route to get the client request to pass it to executable schema and then return back a response to the client
- a route to serve as a Playground client to easily interact with a client (you might not need this one in production)

```sh
$ ./batect flask_app
```

### 3. Adding mutations support

Add some mutations to Step 2 implementations to allow us to modify server data set. 

```sh
$ ./batect flask_app_mutations
```