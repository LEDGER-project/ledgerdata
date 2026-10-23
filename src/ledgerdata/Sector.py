from pydantic.dataclasses import dataclass
from pydantic import HttpUrl

from .Base import Base

import pandas as pd
import requests
from typing import List, Union, Tuple, Optional
import warnings
import httpx


@dataclass
class Sector(Base):
    """retrieve sectors

    Returns:
        object
    """

    def sector(self, *args, **kwargs):
        """retrieve sectors

        Returns:
            DataFrame: 
        """
        endpoint = f"/sector/"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        # Add query parameters
        params = {}
        #if datasource_id:
        #    params["datasource_id"] = datasource_id
            

        response = requests.get(url, headers=headers, params=params).json()
        return response
