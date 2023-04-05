import pytest

from app import cli


@pytest.fixture(scope="session")
def test_init(runner):
    test_client = runner.invoke(cli.app, ["init"], input="\n")
     
    if "Unable to connect to the Substrate node" in test_client.output:
           pytest.skip("Substrate node is not active. Skipping integration tests.")
    
    if "DuplicateContract" in test_client.output:
           pytest.skip("Please restart the node.")

    return test_client


@pytest.fixture(scope="session")
def test_save_trade(runner, test_init):
    test_client = runner.invoke(cli.app, [
        "save-trade", 
        "--energy", "10.12", 
        "--price", "200.98",
        "--seller-address", "0x7c7c1f37d0c07ecb8d1f25c25f73a257dcfc7f9289e99e3c360616266f1d09c1",
        "--buyer-address", "0x98d2b45d31a5277e5ed5cb730db5b2ff5c14d86b4f4b4c3d5bc42da5e04f08f9"]
        )

    return test_client