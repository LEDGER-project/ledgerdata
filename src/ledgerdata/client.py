import asyncio
from dataclasses import dataclass

import pandas as pd

from .actors import Actors
from .base import Base
from .datasource import Datasource
from .gwp import GWP
from .sector import Sector


@dataclass
class Client(Base):
    """ledgerdata client class

    a high-level class to interact with the ledger database

    Attributes:
        version: str = API version (default "/api/v0)
        env: str = "prod" for production server or "dev" for local development  (default "prod")
    """

    # Limit concurrency to 10 requests at once, adjust as needed
    _sem = asyncio.Semaphore(10)

    def get_all_actors(
        self,
    ) -> pd.DataFrame:
        """retreive all actors

        this method is used to retriece a dataframe of all actors and their codes

        Returns:
            DataFrame: data of all actors
        """
        return pd.DataFrame(Actors(env=self.env, version=self.version).get_all_actors())

    def parts_of_actor(
        self, actor_id: str, part_type: str | None = None, *args, **kwargs
    ) -> pd.DataFrame:
        """retreive actor parts

        returns subnational, cities, companies, etc. within an actor_id

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve
            part_type (str): retrieve actors from administrative part ['planet', 'country', 'adm1', 'adm2', 'city', 'organization', 'site']

        Returns:
            DataFrame: dataframe of actors parts
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).parts_of_actor(
                actor_id=actor_id, type=part_type
            )
        )

    def gwp(
        self,
        assessment_report=None,
    ) -> pd.DataFrame:
        """retreive global warming potentials

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve

        Returns:
            DataFrame: data for GWPs
        """
        return pd.DataFrame(
            GWP(env=self.env, version=self.version).gwp(
                assessment_report=assessment_report
            )
        )

    def datasource(
        self,
        datasource_id=None,
    ) -> pd.DataFrame:
        """retrieve data sources

        Args:
            datasource_id (str|List[str]): code for datasource

        Returns:
            DataFrame: data for datasources
        """
        return pd.DataFrame(
            Datasource(env=self.env, version=self.version).datasource(
                datasource_id=datasource_id
            )
        )

    def sector(self) -> pd.DataFrame:
        """retrieve sectors

        Returns:
            DataFrame: data for sectors
        """
        return pd.DataFrame(Sector(env=self.env, version=self.version).sector())

    def emissions(
        self,
        actor_id: str,
    ) -> pd.DataFrame:
        """retreive actor emissions

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve

        Returns:
            DataFrame: data for each emissions dataset
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).emissions(actor_id=actor_id)
        )

    
    def emissions_total_sector(
        self,
        actor_id: str,
    ) -> pd.DataFrame:
        """retreive actor emissions by sector

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve

        Returns:
            DataFrame: data for each emissions dataset
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).emissions_total_sector(actor_id=actor_id)
        )

    def emissions_raw(
        self,
        actor_id: str,
    ) -> pd.DataFrame:
        """retreive actor emissions raw

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve

        Returns:
            DataFrame: data for each emissions dataset
        """
        return Actors(env=self.env, version=self.version).emissions(actor_id=actor_id)

    def targets(self, actor_id: str) -> pd.DataFrame:
        """retreive actor targets

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve

        Returns:
            DataFrame: dataframe of targets
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).targets(actor_id=actor_id)
        )

    def population(self, actor_id: str) -> pd.DataFrame:
        """retreive actor population

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve
            ignore_warnings (bool): ignore warning messages

        Returns:
            DataFrame: dataframe of population
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).population(actor_id=actor_id)
        )

    def gdp(self, actor_id: str) -> pd.DataFrame:
        """retreive actor gdp

        Args:
            actor_id (str|List[str]): code for actor your want to retrieve
            ignore_warnings (bool): ignore warning messages

        Returns:
            DataFrame: dataframe of gdp
        """
        return pd.DataFrame(
            Actors(env=self.env, version=self.version).gdp(actor_id=actor_id)
        )

    async def emissions_async(self, actor_id: str) -> pd.DataFrame:
        data = await Actors(env=self.env, version=self.version).emissions_async(
            actor_id=actor_id
        )
        return pd.DataFrame(data)

    async def _emissions_with_sem(self, actor_id: str) -> pd.DataFrame:
        async with self._sem:
            return await self.emissions_async(actor_id)

    async def emissions_many(self, actor_ids: list[str]) -> list[pd.DataFrame]:
        tasks = [self._emissions_with_sem(actor_id) for actor_id in actor_ids]
        return await asyncio.gather(*tasks)

    # sync wrappers that run the async code in an event loop
    def emissions_sync(self, actor_id: str) -> pd.DataFrame:
        return asyncio.run(self.emissions_async(actor_id))

    def emissions_many_sync(self, actor_ids: list[str]) -> list[pd.DataFrame]:
        return asyncio.run(self.emissions_many(actor_ids))
