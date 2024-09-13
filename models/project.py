from dataclasses import dataclass
from typing import List

from models.metric import Metric
from models.project_base import Project

@dataclass
class Token(Project):
    address: str # token address
    decimals: int # token decimals
    is_meme: bool = False # meme flag
    has_boost: bool = False
    url: str = None # project url
    boost_link: str = None
    prizes: bool = True # flat to ignore project in reward calculation
    possible_reward: int = 0

@dataclass
class App(Project):
    analytics_key: str # project name in tganalytics.xy
    metrics: List[Metric]
    url: str = None # project url
    token: Token = None # Token of the project
    nfts: List[str] = None # Project NFTs
    prizes: bool = True # flat to ignore project in reward calculation
    possible_reward: int = 0

@dataclass
class NFT(Project):
    address: str # token address
    url: str = None # project url


@dataclass
class DeFi(Project):
    url: str # project url
    defillama_slug: str # Defillama slug
    prizes: bool = True # flat to ignore project in reward calculation
    category: str = "dexs" # category for the project (for the Volume Leaderboard)
    chain: str = "TON" # Chain for TVL queries - allows to override default TON into TON-Staking
