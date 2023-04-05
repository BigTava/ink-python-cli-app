from app import cli

def test_save_trade_to_contract_valid_args(runner, test_init, test_save_trade):

    # Given
    response = test_save_trade.output

    # When
    # Then
    assert test_save_trade.exit_code == 0
    assert "Trade saved successfully" in response