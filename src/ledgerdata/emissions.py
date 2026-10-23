import warnings

import httpx
import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class Emissions(Base):
    """retrieve emissions

    Returns:
        object
    """

    def emissions(self, actor_id: str, ignore_warnings: bool = False, *args, **kwargs):
        """retreive actor emissions

        Args:
            actor_id (str): code for actor your want to retrieve
            ignore_warnings (bool): ignore warning messages

        Returns:
            DataFrame: data for each emissions dataset
        """
        (
            warnings.simplefilter("ignore")
            if ignore_warnings
            else warnings.simplefilter("default")
        )
        endpoint = f"/actor/{actor_id}/emissions"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        response = requests.get(url, headers=headers).json()
        # data_list = response.get("data", None)
        # df = pd.DataFrame(response).sort_values(by=["year"])
        return response

    async def emissions_async(
        self, actor_id: str, ignore_warnings: bool = False, *args, **kwargs
    ):
        """Retrieve actor emissions asynchronously."""
        if ignore_warnings:
            warnings.simplefilter("ignore")
        else:
            warnings.simplefilter("default")

        endpoint = f"/actor/{actor_id}/emissions"
        url = f"{self.server}{endpoint}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "python-httpx/1.0",
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
