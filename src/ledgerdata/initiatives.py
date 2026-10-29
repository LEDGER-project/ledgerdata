import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class Initiatives(Base):
    """retrieve emissions

    Returns:
        object
    """

    def initiatives(self, initiative="us_climate_alliance", *args, **kwargs):
        """retreive actors part of an initiative

        Args:
            initiative (str): InitiativeType 

        Returns:
            DataFrame: data for selected initiative
        """
        endpoint = "/initiatives/"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        # Add query parameters
        params = {}
        if initiative:
            params["initiative"] = initiative

        response = requests.get(url, headers=headers, params=params).json()
        return response
