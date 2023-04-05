"""This module provides the cli-app."""

from typing import Optional
import typer
import math

from app import ERRORS, __app_name__, __version__, config, node

app = typer.Typer()

CONST_FLOAT_DECIMALS = 1

# ------ init -----------------------------------------------------------------------

@app.command()
def init(
    node_url: str = typer.Option(
        node.DEFAULT_NODE_RPC_URL,
        "--substrate-url",
        "-url",
        prompt="Substrate node URL?"
    ),
) -> None:
    """Initialize the energy trade smart contract."""

    # initializes config file and checks node connection
    app_init_error = config.init_app(node_url)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # deploys contract
    substrate = node.get_node_connection(node_url)
    try:
        substrate.get_chain_head()
    except:
        return ERRORS[5]
    
    contract_address = node.deploy_contract()
    config.set_contract_address(contract_address)
    typer.secho(
        f'✅ Deployed @ {contract_address}',
        fg=typer.colors.GREEN
    )

# /----- init -----------------------------------------------------------------------

# ------ save_trade -----------------------------------------------------------------
@app.command()
def save_trade(
    energy: float = typer.Option(..., help="Energy (float, in kWh)"),
    price: float = typer.Option(..., help="Price (float, in cents)"),
    seller_address: str = typer.Option(..., help="Address of the seller on chain"),
    buyer_address: str = typer.Option(..., help="Address of the buyer on chain"),
) -> None:
    """Save a trade object to the blockchain contract storas."""

    # Save the trade
    energy_int = int(energy * 10**(CONST_FLOAT_DECIMALS))
    price_int = int(price * 10**(CONST_FLOAT_DECIMALS))

    trade_id = node.save_trade_to_contract(energy_int, price_int, seller_address, buyer_address)

    # Check if the trade was saved successfully and display the result
    if trade_id is not None:
        typer.secho(f"✅ Trade saved successfully. Trade ID: {trade_id}", fg=typer.colors.GREEN)
    else:
        typer.secho()

# /----- save_trade -----------------------------------------------------------------

# ------ read_trade -----------------------------------------------------------------
@app.command()
def read_trade(
    trade_id: int = typer.Option(..., help="Energy Trade ID"),
) -> None:
    """Read a trade object from the blockchain contract storage using its ID."""

    # Read the trade
    trade = node.read_trade_from_contract(trade_id)

    energy = int(str(trade['energy']))/(10**(CONST_FLOAT_DECIMALS))
    price = int(str(trade['price']))/(10**(CONST_FLOAT_DECIMALS))

    # Display the result
    if trade:
        typer.echo(f"Trade ID: {trade_id}")
        typer.echo(f"Energy: {energy} kWh")
        typer.echo(f"Price: {price} cents")
        typer.echo(f"Seller address: {trade['seller']}")
        typer.echo(f"Buyer address: {trade['buyer']}")
    else:
        typer.echo(f"No trade found with ID {trade_id}")

# /----- read_trade -----------------------------------------------------------------

# ------ version --------------------------------------------------------------------

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

# /----- version --------------------------------------------------------------------