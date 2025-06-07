import importlib.metadata
from .engine import RuleEngine
from .operators import Operator
from .decoder import RuleDecoder


__version__ = importlib.metadata.version("python-rule-engine")

