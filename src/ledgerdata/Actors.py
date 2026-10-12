from pydantic.dataclasses import dataclass
from pydantic import HttpUrl

from .Base import Base

import pandas as pd
import requests
from typing import List, Union, Tuple, Optional
import warnings


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
        endpoint = f"/actors"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        # Add query parameters as a dict
        response = requests.get(url, headers=headers).json()
        # data_list = response.get("data", None)
        return response

    def parts_of_actor(self, actor_id=str, type: str = None, *args, **kwargs):
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
        endpoint = f"/parts_of/{actor_id}"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        params = {"type": type} if type else {}
        response = requests.get(url, headers=headers, params=params).json()
        # data_list = response.get("data", None)
        return response
