import strawberry


# TODO: this should be a mutation input
@strawberry.input
class Event:
    id: strawberry.ID


@strawberry.type
class Query:
    @strawberry.field
    def events(self, events: list[Event]) -> None:
        pass


schema = strawberry.Schema(query=Query)
