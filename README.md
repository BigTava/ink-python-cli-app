# !ink Python Cli App

This project provides a service that interacts with a private blockchain using smart contracts for storing and retrieving energy trades. It uses the Substrate framework for creating a private blockchain, running locally with only one node, and a smart contract written in Ink to handle the operations of read/write of the trade objects to the blockchain. The Python CLI script is used to deploy and interact with the smart contract.

## Prerequisites

- [Rust](https://rustup.rs/)
- [Python](https://www.python.org/downloads/) (version 3.10 or higher)
- [Substrate](https://docs.substrate.io/install/)

## Project Structure

- `/cli-app`: Python CLI app for interacting with the smart contract
- `/contracts`: Smart contracts written in Ink for handling read/write operations on the blockchain
- `/substrate-node`: Private Substrate node for running the blockchain

## Setup

1. Install Rust, Python, Substrate according to the provided links in the prerequisites section.
2. Clone the repository:
3. Follow the setup instructions in each subfolder:

- [cli-app Setup](/cli-app/README.md)
- [contracts Setup](/contracts/README.md)
- [substrate-node Setup](/substrate-node/README.md)

## Usage

1. Start the private Substrate node by following the instructions in the [substrate-node README](/substrate-node/README.md).
2. Deploy the smart contract by following the instructions in the [contracts README](/contracts/README.md).
3. Use the Python CLI app to interact with the smart contract. Examples can be found in the [cli-app README](/cli-app/README.md).

## License

This project is licensed under the [MIT License](LICENSE).
