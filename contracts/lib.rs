#![cfg_attr(not(feature = "std"), no_std)]

#[ink::contract]
mod energytrade {

    // Importing required storage components
    use ink::storage::Mapping;

    // Defining trade struct which will be used to store the energy trade info
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode)]
    #[cfg_attr(
        feature = "std",
        derive(ink::storage::traits::StorageLayout, scale_info::TypeInfo)
    )]
    pub struct Trade {
        energy: i32,
        price: i32,
        seller: AccountId,
        buyer: AccountId,
    }

    pub type TradeId = u32;

    #[ink(event)]
    pub struct NewTrade {
        #[ink(topic)]
        trade_id: TradeId,
    }

    // Defining the contract storage and implementation
    #[ink(storage)]
    #[derive(Default)]
    pub struct EnergyTrade {
        trades: Mapping<TradeId, Trade>,
        next_trade_id: TradeId,
    }

    impl EnergyTrade {
        // Constructor function which initializes the storage
        #[ink(constructor)]
        pub fn new() -> Self {
            Default::default()
        }

        // Saves the trade object to the contract storage
        #[ink(message)]
        pub fn save_trade(
            &mut self,
            energy: i32,
            price: i32,
            seller: AccountId,
            buyer: AccountId,
        ) -> TradeId {
            // Creating a new trade object
            let trade: Trade = Trade {
                energy,
                price,
                seller,
                buyer,
            };
            let id: TradeId = self.get_next_trade_id();
            self.trades.insert(&id, &trade);

            // Emit the event
            self.env().emit_event(NewTrade { trade_id: id });

            return id;
        }

        // A message which retrieves the trade object from the contract storage
        #[ink(message)]
        pub fn read_trade(&self, trade_id: TradeId) -> Option<Trade> {
            // Looking up the trade object based on the unique identifier
            self.trades.get(&trade_id)
        }

        fn get_next_trade_id(&mut self) -> TradeId {
            let id: TradeId = self.next_trade_id;
            self.next_trade_id += 1;
            id
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn test_save_trade() {
            // Given
            let mut energy_trade: EnergyTrade = EnergyTrade::new();
            let energy: i32 = 10;
            let price: i32 = 5;
            let seller: AccountId = AccountId::from([0x1; 32]);
            let buyer: AccountId = AccountId::from([0x0; 32]);

            // When
            let trade_id: TradeId = energy_trade.save_trade(energy, price, seller, buyer);

            // Then
            let expected_trade: Trade = Trade {
                energy,
                price,
                seller,
                buyer,
            };
            assert_eq!(energy_trade.trades.get(&trade_id).unwrap(), expected_trade);
        }

        #[ink::test]
        fn test_read_trade() {
            // Given
            let mut energy_trade: EnergyTrade = EnergyTrade::new();
            let energy: i32 = 10;
            let price: i32 = 5;
            let seller: AccountId = AccountId::from([0x1; 32]);
            let buyer: AccountId = AccountId::from([0x0; 32]);
            let trade: Trade = Trade {
                energy,
                price,
                seller,
                buyer,
            };

            let trade_id: TradeId = 1;

            // When
            energy_trade.trades.insert(&trade_id, &trade);
            let result: Option<Trade> = energy_trade.read_trade(trade_id);

            // Then
            assert_eq!(result, Some(trade));
        }
    }
}
