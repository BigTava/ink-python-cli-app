# Energy Trade Smart Contract

This folder contains the energy trade smart contract source code, written in Rust using the Ink! framework. The smart contract is responsible for managing energy trades on the Substrate blockchain.

## Building the Smart Contract

Before deploying the smart contract, you need to build it using `cargo-contract`. Make sure you have `cargo-contract` installed on your system.

1. Navigate to the `contracts` folder:

```sh
$ cd contracts
```

2. cargo contract build

3. Copy the generated files to the cli-app/assets folder:

```sh
$ cp target/ink/energytrade.contract ../cli-app/assets/
$ cp target/ink/energytrade.wasm ../cli-app/assets/
$ cp target/ink/metadata.json ../cli-app/assets/
```

## Testing the Smart Contract

1. Run tests for the smart contract:

```sh
$ cargo contract test
```
