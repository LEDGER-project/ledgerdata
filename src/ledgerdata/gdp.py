import warnings
from typing import ClassVar

import pandas as pd
import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class ActorData(Base):
    endpoint: ClassVar[str]

    def fetch(
        self,
        actor_id: str,
        ignore_warnings: bool = False,
        *args,
        **kwargs,
    ):
        """Retrieve actor data for the given endpoint."""
        if ignore_warnings:
            warnings.simplefilter("ignore")
        else:
            warnings.simplefilter("default")

        url = f"{self.server}{self.endpoint}/{actor_id}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return pd.DataFrame(response)


@dataclass
class GDP(ActorData):
    endpoint: ClassVar[str] = "/gdp"
