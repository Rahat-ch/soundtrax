import graphene
import trax.schema

class Query(trax.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)