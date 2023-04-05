from app import __app_name__

def test_init(test_init):
    # Given
    response = test_init.output
    
    # When
    # Then
    assert "Substrate node URL?" in response
    
    if test_init.exit_code == 0:
            assert "Deployed" in response

    if test_init.exit_code == 1:
            assert "smart contract deploy error" in response