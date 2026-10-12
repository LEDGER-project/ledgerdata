from pydantic.dataclasses import dataclass
from pydantic import HttpUrl

from .Base import Base

import pandas as pd
import requests
from typing import List, Union, Tuple, Optional, ClassVar
import warnings


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