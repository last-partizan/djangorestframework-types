from collections.abc import Iterator, Mapping, Sequence
from contextlib import AbstractContextManager, contextmanager
from types import TracebackType
from typing import (
    Any,
    BinaryIO,
    NoReturn,
    Union,
)

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.base import SessionBase
from django.contrib.sites.models import Site
from django.core.files import uploadedfile, uploadhandler
from django.http import HttpRequest, QueryDict
from django.http.request import HttpHeaders
from django.urls import ResolverMatch
from django.utils.datastructures import ImmutableList, MultiValueDict
from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.parsers import BaseParser
from rest_framework.versioning import BaseVersioning
from rest_framework.views import APIView

_UploadHandlerList = Union[list[uploadhandler.FileUploadHandler], ImmutableList[uploadhandler.FileUploadHandler]]

def is_form_media_type(media_type: str) -> bool: ...

class override_method(AbstractContextManager["Request"]):
    def __init__(self, view: APIView, request: Request, method: str): ...
    def __enter__(self) -> Request: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None: ...

class WrappedAttributeError(Exception): ...

@contextmanager
def wrap_attributeerrors() -> Iterator[None]: ...

class Empty: ...

def clone_request(request: Request, method: str) -> Request: ...

class ForcedAuthentication:
    force_user: AnonymousUser | AbstractBaseUser | None = ...
    force_token: str | None = ...
    def __init__(self, force_user: AnonymousUser | AbstractBaseUser | None, force_token: str | None) -> None: ...
    def authenticate(self, request: Request) -> tuple[AnonymousUser | AbstractBaseUser | None, Any | None]: ...

class Request(HttpRequest):
    parsers: Sequence[BaseParser] | None = ...
    authenticators: Sequence[BaseAuthentication | ForcedAuthentication] | None = ...
    negotiator: BaseContentNegotiation | None = ...
    parser_context: dict[str, Any] | None = ...
    version: str | None
    versioning_scheme: BaseVersioning | None
    _request: HttpRequest
    GET: QueryDict = ...
    COOKIES: dict[str, str] = ...
    META: dict[str, Any] = ...
    path: str = ...
    path_info: str = ...
    method: str | None = ...
    resolver_match: ResolverMatch = ...
    content_params: dict[str, str] | None = ...
    site: Site
    session: SessionBase
    encoding: str | None = ...
    upload_handlers: _UploadHandlerList = ...
    def __init__(
        self,
        request: HttpRequest,
        parsers: Sequence[BaseParser] | None = ...,
        authenticators: Sequence[BaseAuthentication] | None = ...,
        negotiator: BaseContentNegotiation | None = ...,
        parser_context: dict[str, Any] | None = ...,
    ) -> None: ...
    def get_host(self) -> str: ...
    def get_port(self) -> str: ...
    def get_full_path(self, force_append_slash: bool = ...) -> str: ...
    def get_full_path_info(self, force_append_slash: bool = ...) -> str: ...
    def get_signed_cookie(
        self, key: str, default: Any = ..., salt: str = ..., max_age: int | None = ...
    ) -> str | None: ...
    def get_raw_uri(self) -> str: ...
    def build_absolute_uri(self, location: str | None = ...) -> str: ...
    @property
    def scheme(self) -> str | None: ...
    def is_secure(self) -> bool: ...
    def is_ajax(self) -> bool: ...
    def parse_file_upload(
        self, META: Mapping[str, Any], post_data: BinaryIO
    ) -> tuple[QueryDict, MultiValueDict[str, uploadedfile.UploadedFile]]: ...
    @property
    def headers(self) -> HttpHeaders: ...
    @property
    def body(self) -> bytes: ...
    def _load_post_and_files(self) -> None: ...
    def content_type(self) -> str: ...  # type: ignore[override]
    @property
    def stream(self) -> Any: ...
    @property
    def query_params(self) -> QueryDict: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property  # type: ignore[override]
    def user(self) -> AbstractBaseUser | AnonymousUser: ...
    @user.setter
    def user(self, value: AbstractBaseUser | AnonymousUser) -> None: ...
    @property
    def auth(self) -> Token | Any: ...
    @auth.setter
    def auth(self, value: Token | Any) -> None: ...
    @property
    def successful_authenticator(self) -> BaseAuthentication | ForcedAuthentication | None: ...
    @property
    def DATA(self) -> None: ...
    @property
    def POST(self) -> QueryDict: ...  # type: ignore[override]
    @property
    def FILES(self) -> MultiValueDict[str, uploadedfile.UploadedFile]: ...  # type: ignore [override]
    @property
    def QUERY_PARAMS(self) -> NoReturn: ...
    def force_plaintext_errors(self, value: Any) -> None: ...
