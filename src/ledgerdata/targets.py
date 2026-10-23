import warnings

import requests
from pydantic.dataclasses import dataclass

from .base import Base


@dataclass
class Targets(Base):
    """retrieve emission targets

    Returns:
        object
    """

    def targets(self, actor_id: str, ignore_warnings: bool = False, *args, **kwargs):
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
        endpoint = f"/targets/{actor_id}"
        url = f"{self.server}{endpoint}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response
