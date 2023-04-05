from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface.exceptions import ExtrinsicFailedException
from pathlib import Path
import typer

from app import SUCCESS, ERRORS, config

DEFAULT_NODE_RPC_URL = "ws://127.0.0.1:9944"

def deploy_contract() -> str:
    substrate = get_node_connection()
    keypair = Keypair.create_from_uri('//Alice')

    try:
        code = ContractCode.create_from_contract_files(
            metadata_file=(Path(__file__).parent / "../assets/metadata.json"),
            wasm_file=(Path(__file__).parent / "../assets/energytrade.wasm"),
            substrate=substrate
        )

        contract = code.deploy(
            keypair=keypair,
            endowment=0,
            gas_limit=1000000000000,
            constructor="new",
            upload_code=True
        )

        return contract.contract_address

    except ExtrinsicFailedException:
        typer.secho(
            f'Deploying contract failed with "{ERRORS[3]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


def save_trade_to_contract(energy: float, price: float, seller_address: str, buyer_address: str) -> int:
    """Save a trade to the blockchain."""
    args = {"energy": int(energy), "price": int(price), "seller": seller_address, "buyer": buyer_address}
    keypair = Keypair.create_from_uri('//Bob')
    
    contract = _get_contract_instance()
    gas_predit_result = contract.read(keypair, 'save_trade', args)
    contract_receipt = contract.exec(keypair, 'save_trade', 
                                     args=args, 
                                     gas_limit=gas_predit_result.gas_required)

    trade_id = None
    for event in contract_receipt.contract_events:
        if event.value["name"] == "NewTrade":
            for arg in event.value["args"]:
                if arg["label"] == "trade_id":
                    trade_id = arg["value"]
                    break

    if contract_receipt.is_success:
        return trade_id
    else:
        typer.secho(
            f'Saving trade failed with "{ERRORS[5]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


def read_trade_from_contract(trade_id: str) -> dict:
    """Read a trade from the smart contract using its ID."""
    keypair = Keypair.create_from_uri('//Bob')

    contract = _get_contract_instance()
    result = contract.read(keypair, 'read_trade', args={"trade_id": trade_id})
    
    if "Ok" in result.contract_result_data:
        return result.contract_result_data[1]
    else:
        return None
    

def get_node_connection(rpc_url: str = config.get_rpc_url()) -> SubstrateInterface:
    """Return a connection to the blockchain using the settings in the configuration file."""
    try:
        substrate = SubstrateInterface(rpc_url, type_registry_preset='canvas')
    except Exception:
        typer.secho(
            f"Unable to connect to the Substrate node. Please check if the node is running and try again.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    return substrate


def _get_contract_instance():
    substrate = get_node_connection()
    contract_address = config.get_contract_address()
    
    contract_info = substrate.query("Contracts", "ContractInfoOf", [contract_address])

    if contract_info.value:
        # Create contract instance from deterministic address
        contract = ContractInstance.create_from_address(
            contract_address=contract_address,
            metadata_file=(Path(__file__).parent / "../assets/metadata.json"),
            substrate=substrate
        )
        return contract