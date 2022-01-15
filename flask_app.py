from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from ariadne import gql, QueryType, make_executable_schema, graphql_sync

# Define type definitions (schema) using SDL
type_defs = gql(
    """
   type Query {
       places: [Place]
   }


   type Place {
       name: String!
       description: String!
       country: String!
       }  
   """
)

# Initialize query

query = QueryType()


# Define resolvers
@query.field("places")
def places(*_):
    return [
        {"name": "Paris", "description": "The city of lights", "country": "France"},
        {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
        {
            "name": "London",
            "description": "The city of big buildings",
            "country": "United Kingdom",
        },
    ]


# Create executable schema
schema = make_executable_schema(type_defs, query)

# initialize flask app
app = Flask(__name__)


# Create a GraphQL Playground UI for the GraphQL schema
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # Playground accepts GET requests only.
    # If you wanted to support POST you'd have to
    # change the method to POST and set the content
    # type header to application/graphql
    return PLAYGROUND_HTML


# Create a GraphQL endpoint for executing GraphQL queries
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code


# Run the app
# if __name__ == "__main__":
#     app.run(debug=True)
