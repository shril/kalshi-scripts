from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from classes.environment import Environment


class Distribution(Enum):
    LINEAR = 1


@dataclass
class MarketProfile:
    market_ticker: str
    instant_liquidity_cents: int
    max_exposure_cents: int
    price_stickyness: int
    spread: int
    depth: int
    max_yes_price: Optional[int]
    min_yes_price: Optional[int]
    clear_time: Optional[str]
    distribution: Distribution


@dataclass
class StrategyProfile:
    env: Environment
    markets: List[MarketProfile]