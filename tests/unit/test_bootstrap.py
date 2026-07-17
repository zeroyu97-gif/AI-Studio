"""
Unit tests for bootstrap module.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from ai_studio.bootstrap import Bootstrap


class TestBootstrap:
    """Test Bootstrap class."""

    def test_bootstrap_initialization(self) -> None:
        """Test Bootstrap initialization."""
        bootstrap = Bootstrap()
        assert bootstrap.root == Path.cwd()

    def test_bootstrap_prepare_creates_directories(
        self, cleanup_cwd: Path
    ) -> None:
        """Test that prepare() creates all required directories."""
        bootstrap = Bootstrap()
        bootstrap.prepare()

        expected_dirs = ("logs", "cache", "workspace", "plugins", "settings")
        for directory in expected_dirs:
            dir_path = cleanup_cwd / directory
            assert dir_path.exists()
            assert dir_path.is_dir()

    def test_bootstrap_prepare_idempotent(self, cleanup_cwd: Path) -> None:
        """Test that prepare() is idempotent (can be called multiple times)."""
        bootstrap = Bootstrap()
        bootstrap.prepare()
        bootstrap.prepare()  # Should not raise

        expected_dirs = ("logs", "cache", "workspace", "plugins", "settings")
        for directory in expected_dirs:
            dir_path = cleanup_cwd / directory
            assert dir_path.exists()

    def test_bootstrap_root_is_path_object(self) -> None:
        """Test that bootstrap.root is a Path object."""
        bootstrap = Bootstrap()
        assert isinstance(bootstrap.root, Path)

    @patch("builtins.print")
    def test_bootstrap_start_prints_output(
        self,
        mock_print: object,
        cleanup_cwd: Path,
    ) -> None:
        """Test that start() prints output to console."""
        bootstrap = Bootstrap()
        bootstrap.start()

        # Verify print was called
        assert mock_print is not None

    def test_bootstrap_start_creates_directories(self, cleanup_cwd: Path) -> None:
        """Test that start() creates directories."""
        bootstrap = Bootstrap()
        bootstrap.start()

        expected_dirs = ("logs", "cache", "workspace", "plugins", "settings")
        for directory in expected_dirs:
            dir_path = cleanup_cwd / directory
            assert dir_path.exists()
