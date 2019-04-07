import graphene
import trax.schema
import users.schema

class Query(users.schema.Query, trax.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, trax.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)