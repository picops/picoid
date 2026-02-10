"""Minimal pytest tests for picoid: every exported name works as expected."""

import pytest

import picoid


def test_all_exported_names_are_available() -> None:
    """Every name in __all__ is importable from picoid and is usable."""
    assert hasattr(picoid, "__all__")
    assert isinstance(picoid.__all__, tuple)
    assert all(isinstance(name, str) for name in picoid.__all__)
    for name in picoid.__all__:
        assert hasattr(
            picoid, name
        ), f"picoid.__all__ contains {name!r} but picoid has no attribute {name!r}"


def test_version() -> None:
    """__version__ is a non-empty string."""
    assert hasattr(picoid, "__version__")
    v = picoid.__version__
    assert isinstance(v, str)
    assert len(v) > 0


def test_import_from_picoid() -> None:
    """All __all__ names can be imported via 'from picoid import ...'."""
    for name in picoid.__all__:
        module = __import__("picoid", fromlist=[name])
        assert hasattr(module, name), f"from picoid import {name!r} failed"
