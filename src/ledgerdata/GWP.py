from pydantic.dataclasses import dataclass
from pydantic import HttpUrl

from .Base import Base

import pandas as pd
import requests
from typing import List, Union, Tuple, Optional
import warnings
import httpx


@dataclass
class GWP(Base):
    """retrieve emissions

    Returns:
        object
    """

    def gwp(self, assessment_report=None, *args, **kwargs):
        """retreive actor emissions

        Args:
            actor_id (str): code for actor your want to retrieve
            ignore_warnings (bool): ignore warning messages

        Returns:
            DataFrame: data for each emissions dataset
        """
        endpoint = f"/gwp/"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

            # Add query parameters
        params = {}
        if assessment_report:
            params["assessment_report"] = assessment_report
            

        response = requests.get(url, headers=headers, params=params).json()
        return response
