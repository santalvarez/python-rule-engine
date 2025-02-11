import importlib.metadata
from .engine import RuleEngine
from .operators import Operator
from .models.rule import Rule


__version__ = importlib.metadata.version("python-rule-engine")

