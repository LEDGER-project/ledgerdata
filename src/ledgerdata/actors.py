import warnings

import httpx
import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class Actors(Base):
    """Provides methods to retrieve actor and actor-part data from the LEDGER API."""

    def get_all_actors(self, *args, **kwargs):
        """Retrieve all actors.

        Sends a GET request to the `/actors` endpoint and returns the response
        as a JSON dictionary.

        Returns:
            dict: A JSON response containing actor data.
        """
        endpoint = "/actor"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        # Add query parameters as a dict
        response = requests.get(url, headers=headers).json()
        # data_list = response.get("data", None)
        return response

    def parts_of_actor(self, actor_id=str, type: str | None = None, *args, **kwargs):
        """Retrieve parts (sub-actors) of a given actor.

        Sends a GET request to the `/parts_of/{actor_id}` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            type (Optional[str]): Optional filter for part type.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        endpoint = f"/actor/{actor_id}/parts"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        params = {"type": type} if type else {}
        response = requests.get(url, headers=headers, params=params).json()
        # data_list = response.get("data", None)
        return response

    def population(self, actor_id=str, *args, **kwargs):
        """Retrieve actor population

        Sends a GET request to the `/actor/{actor_id}/population` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        endpoint = f"/actor/{actor_id}/population"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response

    def gdp(self, actor_id=str, *args, **kwargs):
        """Retrieve actor population

        Sends a GET request to the `/actor/{actor_id}/gdp` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        endpoint = f"/actor/{actor_id}/gdp"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response

    def energy_consumption(self, actor_id=str, *args, **kwargs):
        """Retrieve actor population

        Sends a GET request to the `/actor/{actor_id}/energy_consumption` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        endpoint = f"/actor/{actor_id}/energy_consumption"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response

    def targets(self, actor_id=str, *args, **kwargs):
        """Retrieve actor population

        Sends a GET request to the `/actor/{actor_id}/targets` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        endpoint = f"/actor/{actor_id}/targets"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response

    def emissions(self, actor_id=str, ignore_warnings: bool = False, *args, **kwargs):
        """Retrieve actor population

        Sends a GET request to the `/actor/{actor_id}/emissions` endpoint and returns
        the response as a JSON dictionary.

        Args:
            actor_id (str): The code for the actor whose parts you want to retrieve.
            *args: Additional positional arguments (currently unused).
            **kwargs: Additional keyword arguments (currently unused).

        Returns:
            dict: A JSON response containing actor-part data.
        """
        (
            warnings.simplefilter("ignore")
            if ignore_warnings
            else warnings.simplefilter("default")
        )
        endpoint = f"/actor/{actor_id}/emissions"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
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
