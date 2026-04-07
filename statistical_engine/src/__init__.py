"""
Statistical Engine Package
Provides core statistical analysis and Monte Carlo simulation capabilities.
"""

from .stat_engine import StatEngine
from .monte_carlo import simulate_crashes

__all__ = ['StatEngine', 'simulate_crashes']