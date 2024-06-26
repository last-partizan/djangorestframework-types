from typing import Any

from django.db.models import Model
from rest_framework.fields import Field
from rest_framework.views import APIView

def is_list_view(path: str, method: str, view: APIView) -> bool: ...
def get_pk_description(model: Model, model_field: Field[Any, Any, Any, Any]) -> str: ...
