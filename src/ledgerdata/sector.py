import requests
from pydantic.dataclasses import dataclass

from .base import Base


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
        endpoint = "/sector/"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        # Add query parameters
        params = {}
        # if datasource_id:
        #    params["datasource_id"] = datasource_id

        response = requests.get(url, headers=headers, params=params).json()
        return response
