# CLI-App

**Cli-App** is a command-line interface application built with [Typer](https://typer.tiangolo.com/) to help you interact with the EnergyTrade smart contract on a private Substrate blockchain.

## Installation

To run **CLI-App**, you need to follow these steps:

1. Create a Python virtual environment and activate it:

```sh
$ cd cli-app/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the dependencies:

```sh
(venv) $ python -m pip install -r requirements.txt
```

## Usage

Once you've run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python -m app --help
Usage: app [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  init        Initialize app and deploy the energy trade smart contract.
  read-trade  Read a trade object from the smart contract storage using its ID.
  save-trade  Save a trade object to the smart contract storage.
```

## Release History

- 0.1.0
  - Initial release
  - Features: initializing the energy trade smart contract, saving a trade and reading a trade
