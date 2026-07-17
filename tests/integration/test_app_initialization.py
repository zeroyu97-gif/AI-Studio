"""
Integration tests for application initialization.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_studio import __version__
from ai_studio.version import VERSION


class TestAppInitialization:
    """Test application initialization."""

    def test_version_is_available(self) -> None:
        """Test that __version__ is accessible from ai_studio package."""
        assert __version__ is not None
        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_version_format(self) -> None:
        """Test that version follows semantic versioning."""
        parts = __version__.split("-")
        assert len(parts) == 2
        version_part, stage_part = parts
        major, minor, patch = version_part.split(".")
        assert major.isdigit()
        assert minor.isdigit()
        assert patch.isdigit()

    def test_version_consistency(self) -> None:
        """Test that VERSION constant matches __version__ export."""
        assert str(VERSION) == __version__

    def test_ai_studio_imports(self) -> None:
        """Test that main ai_studio module imports correctly."""
        import ai_studio

        assert hasattr(ai_studio, "__version__")
        assert ai_studio.__version__ == __version__

    def test_bootstrap_module_available(self) -> None:
        """Test that bootstrap module is available."""
        from ai_studio.bootstrap import bootstrap, Bootstrap

        assert callable(bootstrap)
        assert Bootstrap is not None
