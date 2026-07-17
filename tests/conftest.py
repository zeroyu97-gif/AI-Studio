"""
Pytest configuration and shared fixtures.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_workspace() -> Path:
    """
    Create a temporary workspace directory for testing.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_config() -> dict:
    """
    Provide sample configuration for tests.
    """
    return {
        "app_name": "AI Studio",
        "app_env": "testing",
        "debug": True,
        "log_level": "DEBUG",
    }


@pytest.fixture
def cleanup_cwd(tmp_path: Path, monkeypatch) -> Path:
    """
    Create a temporary working directory and change to it.
    """
    monkeypatch.chdir(tmp_path)
    return tmp_path
