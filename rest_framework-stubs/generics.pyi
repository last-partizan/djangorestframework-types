from collections.abc import Sequence
from typing import Any, TypeVar

from django.db.models import Manager, Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework import mixins, views
from rest_framework.filters import FilterBackendProtocol
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

_MT_co = TypeVar("_MT_co", bound=Model, covariant=True)

def get_object_or_404(
    queryset: type[_MT_co] | Manager[_MT_co] | QuerySet[_MT_co], *filter_args: Any, **filter_kwargs: Any
) -> _MT_co: ...

_D = TypeVar("_D", bound=Model)
_Q = TypeVar("_Q", bound=QuerySet[Any])

class GenericAPIView(views.APIView):
    serializer_class: type[BaseSerializer] | None = ...
    lookup_field: str = ...
    lookup_url_kwarg: str | None = ...
    filter_backends: Sequence[type[FilterBackendProtocol]] = ...
    pagination_class: type[BasePagination] | None = ...
    def get_object(self) -> Any: ...
    def get_serializer(self, *args: Any, **kwargs: Any) -> BaseSerializer: ...
    def get_serializer_class(self) -> type[BaseSerializer]: ...
    def get_serializer_context(self) -> dict[str, Any]: ...
    def filter_queryset(self, queryset: _Q) -> _Q: ...
    def paginator(self) -> BasePagination | None: ...
    def paginate_queryset(self, queryset: QuerySet[_D]) -> list[_D] | None: ...
    def get_paginated_response(self, data: Any) -> Response: ...
    def get_queryset(self) -> QuerySet[_MT_co]: ...

class CreateAPIView(mixins.CreateModelMixin, GenericAPIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class ListAPIView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class RetrieveAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class DestroyAPIView(mixins.DestroyModelMixin, GenericAPIView):
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    def put(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class ListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def post(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class RetrieveUpdateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def put(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class RetrieveDestroyAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...

class RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView
):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def put(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse: ...
