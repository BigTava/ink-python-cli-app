import pytest
from typer.testing import CliRunner

from app import cli

@pytest.fixture(scope="session")
def runner():
    # set up
    runner = CliRunner()

    return runner