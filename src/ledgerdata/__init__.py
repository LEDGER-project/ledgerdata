"""
Set up module access for the base package
"""

from .actors import Actors
from .client import Client
from .datasource import Datasource
from .emissions import Emissions
from .gdp import GDP
from .initiatives import Initiatives
from .population import Population
from .sector import Sector
from .targets import Targets

__all__ = ["GDP", "Actors", "Client", "Datasource", "Emissions", "Initiatives", "Population", "Sector", "Targets"]
