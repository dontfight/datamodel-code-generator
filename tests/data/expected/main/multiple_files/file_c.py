# generated by datamodel-codegen:
#   filename:  file_c.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from . import file_b


class ModelC(BaseModel):
    firstName: Optional[str] = None
    modelB: Optional[file_b.ModelB] = None
