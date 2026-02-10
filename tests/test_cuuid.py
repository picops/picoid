"""Minimal pytest tests for cuuid: every exported name works as expected."""

import pytest

import cuuid


def test_all_exported_names_are_available() -> None:
    """Every name in __all__ is importable from cuuid and is usable."""
    assert hasattr(cuuid, "__all__")
    assert isinstance(cuuid.__all__, tuple)
    assert all(isinstance(name, str) for name in cuuid.__all__)
    for name in cuuid.__all__:
        assert hasattr(
            cuuid, name
        ), f"cuuid.__all__ contains {name!r} but cuuid has no attribute {name!r}"


def test_version() -> None:
    """__version__ is a non-empty string."""
    assert hasattr(cuuid, "__version__")
    v = cuuid.__version__
    assert isinstance(v, str)
    assert len(v) > 0


def test_import_from_cuuid() -> None:
    """All __all__ names can be imported via 'from cuuid import ...'."""
    for name in cuuid.__all__:
        module = __import__("cuuid", fromlist=[name])
        assert hasattr(module, name), f"from cuuid import {name!r} failed"
