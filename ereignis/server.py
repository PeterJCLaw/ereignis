from __future__ import annotations

from strawberry.asgi import GraphQL
from starlette.routing import Route
from starlette.applications import Starlette

from .schema import schema

graphql_app = GraphQL(schema)

routes = [
    Route("/graphql", name="graphql", endpoint=graphql_app, methods=["POST"]),
]

app = Starlette(routes=routes)
