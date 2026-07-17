"""
Integration tests for bootstrap module.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from ai_studio import __version__
from ai_studio.bootstrap import bootstrap, Bootstrap


class TestBootstrapIntegration:
    """Integration tests for Bootstrap functionality."""

    def test_bootstrap_function_calls_bootstrap_class(
        self,
        cleanup_cwd: Path,
    ) -> None:
        """Test that bootstrap() function properly calls Bootstrap.start()."""
        with patch.object(Bootstrap, "start") as mock_start:
            bootstrap()
            mock_start.assert_called_once()

    def test_full_bootstrap_workflow(self, cleanup_cwd: Path) -> None:
        """Test complete bootstrap workflow."""
        bootstrap()

        # Verify directories are created
        expected_dirs = ("logs", "cache", "workspace", "plugins", "settings")
        for directory in expected_dirs:
            dir_path = cleanup_cwd / directory
            assert dir_path.exists()

    def test_bootstrap_preserves_existing_directories(
        self,
        cleanup_cwd: Path,
    ) -> None:
        """Test that bootstrap doesn't delete existing directories."""
        # Create a test file in workspace directory first
        workspace = cleanup_cwd / "workspace"
        workspace.mkdir(exist_ok=True, parents=True)
        test_file = workspace / "test.txt"
        test_file.write_text("test content")

        # Run bootstrap
        bootstrap()

        # Verify file still exists
        assert test_file.exists()
        assert test_file.read_text() == "test content"

    def test_bootstrap_can_run_multiple_times(self, cleanup_cwd: Path) -> None:
        """Test that bootstrap can be run multiple times safely."""
        bootstrap()
        bootstrap()  # Should not raise
        bootstrap()  # Should not raise

        # Verify all directories still exist
        expected_dirs = ("logs", "cache", "workspace", "plugins", "settings")
        for directory in expected_dirs:
            dir_path = cleanup_cwd / directory
            assert dir_path.exists()
