"""
Low-level UUID implementation for Python.

Exposes UUID (compatible with stdlib uuid.UUID), uuid4(), and randstr_16().
"""

from typing import Tuple

from .__about__ import __version__
from .cuuid import UUID, randstr_16, uuid4

__all__: Tuple[str, ...] = ("UUID", "__version__", "randstr_16", "uuid4")
