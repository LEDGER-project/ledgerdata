import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class Datasource(Base):
    """retrieve emissions

    Returns:
        object
    """

    def datasource(self, datasource_id=None, *args, **kwargs):
        """retrieve actor emissions

        Args:
            datasource_id (str): code for datasource

        Returns:
            DataFrame:
        """
        endpoint = "/datasource/"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        # Add query parameters
        params = {}
        if datasource_id:
            params["datasource_id"] = datasource_id

        response = requests.get(url, headers=headers, params=params).json()
        return response
