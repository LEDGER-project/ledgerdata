import requests
from pydantic.dataclasses import dataclass

from .base import Base


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
        endpoint = "/gwp/"
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
