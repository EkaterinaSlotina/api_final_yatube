from rest_framework import mixins, viewsets


class ListCreateBasicViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass
