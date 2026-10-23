from enum import Enum

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


class Env(str, Enum):
    dev = "dev"
    prod = "prod"


@dataclass
class Base:
    version: str = "/api/v0"
    env: Env = Env.prod

    def __post_init__(self):
        urls = {
            Env.dev: "http://127.0.0.1:8000",
            Env.prod: "https://orca-app-5ivtt.ondigitalocean.app",
        }
        self.base_url: HttpUrl = urls[self.env]
        self.server = f"{self.base_url}{self.version}"
