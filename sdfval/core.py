import functools
from typing import TypeVar, Any, cast, Hashable

import pydantic

from . import sdf


class PydanticConfig:
    extra = "forbid"
    """Extra fields will fail validation."""


@functools.cache
def get_model(t: type) -> type[pydantic.BaseModel]:
    return pydantic.create_model_from_typeddict(t, __config__=PydanticConfig)


def get_model_sdf() -> type[pydantic.BaseModel]:
    return get_model(sdf.Document)


DictType = TypeVar("DictType")


def validate_type(t: type[DictType], data: Any) -> DictType:
    """Validate type with Pydantic.

    Raises
    ------
    pydantic.ValidationError

    """
    model = get_model(cast(Hashable, t))
    model(**data)
    return cast(DictType, data)


def validate_sdf(data: Any) -> sdf.Document:
    return validate_type(sdf.Document, data)
