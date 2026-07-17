"""
Tests for package imports and module structure.
"""

from __future__ import annotations


class TestPackageImports:
    """Test package import structure."""

    def test_import_ai_studio(self) -> None:
        """Test importing ai_studio package."""
        import ai_studio

        assert ai_studio is not None

    def test_import_version(self) -> None:
        """Test importing version module."""
        from ai_studio import __version__

        assert __version__ is not None
        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_import_bootstrap(self) -> None:
        """Test importing bootstrap module."""
        from ai_studio.bootstrap import bootstrap

        assert callable(bootstrap)

    def test_import_version_class(self) -> None:
        """Test importing Version class."""
        from ai_studio.version import Version

        assert Version is not None

    def test_all_exports(self) -> None:
        """Test __all__ exports in ai_studio package."""
        import ai_studio

        assert hasattr(ai_studio, "__all__")
        assert "__version__" in ai_studio.__all__
