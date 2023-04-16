from collections.abc import Callable
from typing import Any, overload

from django.core.cache.backends.base import BaseCache
from rest_framework.request import Request
from rest_framework.views import APIView

class BaseThrottle:
    def allow_request(self, request: Any, view: APIView) -> bool: ...
    def get_ident(self, request: Any) -> str: ...
    def wait(self) -> float | None: ...

class SimpleRateThrottle(BaseThrottle):
    cache: BaseCache = ...
    cache_format: str = ...
    history: list[Any]
    key: str | None = ...
    now: float
    rate: str | None
    scope: str | None = ...
    THROTTLE_RATES: dict[str, str | None] = ...
    timer: Callable[..., float] = ...
    def __init__(self) -> None: ...
    def get_cache_key(self, request: Request, view: APIView) -> str | None: ...
    def get_rate(self) -> str | None: ...
    @overload
    def parse_rate(self, rate: str) -> tuple[int, int]: ...
    @overload
    def parse_rate(self, rate: None) -> tuple[None, None]: ...
    def throttle_failure(self) -> bool: ...
    def throttle_success(self) -> bool: ...

class AnonRateThrottle(SimpleRateThrottle): ...
class UserRateThrottle(SimpleRateThrottle): ...

class ScopedRateThrottle(SimpleRateThrottle):
    scope_attr: str = ...
