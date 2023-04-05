from app import cli

def test_read_trade_from_contract_valid_arg(runner, test_save_trade):
    # Given
    trade_id = 0

    # When
    test_client = runner.invoke(cli.app, [
        "read-trade", 
        "--trade-id", f"{trade_id}"]
        )

    # Then
    response = test_client.output
    
    assert test_client.exit_code == 0
    assert f"Trade ID: {trade_id}" in response
    assert f"Energy: 10.1 kWh" in response
    assert f"Price: 200.9 cents" in response
    assert f"Seller address: 5EsvfdK5ESg13GekXYD1hrpQGMBimpBRTowh9acZxbBDgyod" in response
    assert f"Buyer address: 5FX5jB7QVYfKKJac23Kcf1GADxEB5A1HSGEHYzLFqHGEU7dk" in response
    