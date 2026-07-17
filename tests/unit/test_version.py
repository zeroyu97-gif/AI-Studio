"""
Unit tests for version module.
"""

from __future__ import annotations

import pytest

from ai_studio.version import Version, VERSION, __version__


class TestVersion:
    """Test Version dataclass."""

    def test_version_creation(self) -> None:
        """Test creating a Version instance."""
        version = Version(
            major=1,
            minor=2,
            patch=3,
            stage="alpha",
            build=5,
        )
        assert version.major == 1
        assert version.minor == 2
        assert version.patch == 3
        assert version.stage == "alpha"
        assert version.build == 5

    def test_version_default_stage(self) -> None:
        """Test Version with default stage."""
        version = Version(major=1, minor=0, patch=0)
        assert version.stage == "dev"
        assert version.build == 0

    def test_version_string_representation(self) -> None:
        """Test Version __str__ method."""
        version = Version(
            major=2,
            minor=0,
            patch=0,
            stage="dev",
            build=0,
        )
        assert str(version) == "2.0.0-dev.0"

    def test_version_string_with_different_values(self) -> None:
        """Test Version string with various values."""
        version = Version(
            major=1,
            minor=5,
            patch=2,
            stage="rc",
            build=1,
        )
        assert str(version) == "1.5.2-rc.1"

    def test_version_immutable(self) -> None:
        """Test that Version is frozen (immutable)."""
        version = Version(major=1, minor=0, patch=0)
        with pytest.raises(AttributeError):
            version.major = 2  # type: ignore

    def test_global_version(self) -> None:
        """Test global VERSION constant."""
        assert VERSION.major == 2
        assert VERSION.minor == 0
        assert VERSION.patch == 0
        assert VERSION.stage == "dev"
        assert VERSION.build == 0

    def test_version_string_export(self) -> None:
        """Test __version__ string export."""
        assert isinstance(__version__, str)
        assert __version__ == "2.0.0-dev.0"
        assert __version__ == str(VERSION)
