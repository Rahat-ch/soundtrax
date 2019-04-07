import graphene
import trax.schema

class Query(trax.schema.Query, graphene.ObjectType):
    pass

class Mutation(trax.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)