import graphene
from graphene_django import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

class Query(graphene.ObjectType):
    trax = graphene.List(TrackType)

    def resolve_trax(self, info):
        return Track.objects.all()