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



## GraphQL terms

**Query**
A prebuilt type for querying our data, more like a GET request in a REST API.

**Mutation**
A prebuilt type for manipulating our data. Every field in the Mutation type can be thought of as a POST/PUT/DELETE/PATCH request in a REST API.

**Resolver**
A function that connects schema fields and types to various backends.

**Field**
A unit of data that belongs to a type in your schema.

You can learn more about all the terms from the [official GraphQL documentation](https://graphql.org/).