"""
AlgoNova Backend Package
========================
This package contains the backend modules powering the AlgoNova hybrid dApp.

Modules:
--------
- main.py               → FastAPI server entry point
- comparison.py         → Core functionality #1: Traditional vs. Algorand transaction comparison
- transaction_flow.py   → Core functionality #2: Simulated client–freelancer USDC payment flow

Description:
------------
AlgoNova demonstrates how Algorand-based stablecoin payments (USDC on TestNet)
offer instant settlement and near-zero fees compared to traditional systems
like PayPal or Payoneer.

The backend is powered by FastAPI, making it easy to extend with REST endpoints
for wallet connections, transaction history, or real TestNet execution.
"""

__version__ = "1.0.0"
__author__ = "AlgoNova Team"
__email__ = "contact@algonova.dev"

# Optional: You can expose helper functions globally if needed
from .comparison import display_comparison
from .transaction_flow import simulate_transaction
