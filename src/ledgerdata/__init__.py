"""
Set up module access for the base package
"""

from .Client import Client
from .Actors import Actors
from .Emissions import Emissions
from .Population import Population
from .Targets import Targets
from .GDP import GDP
from .Datasource import Datasource
from .Sector import Sector

__all__ = ["Client", "Actors", "Emissions", "Population", "Targets", "GDP", "Datasource", "Sector"]