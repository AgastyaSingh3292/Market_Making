import numpy as np

class MarketMaker:
    def __init__(self, initial_inventory=0, risk_aversion=0.01):
        self.inventory = initial_inventory
        self.cash = 0
        self.risk_aversion = risk_aversion

    def inventory_penalty(self):
        # Quadratic inventory penalty to avoid excessive inventory risk
        return self.risk_aversion * (self.inventory ** 2)

    def optimal_bid_ask(self, market_price):
        # Calculate optimal bid and ask price based on inventory and risk aversion
        spread = self.risk_aversion * self.inventory
        bid_price = market_price - spread
        ask_price = market_price + spread
        return bid_price, ask_price

    def update_inventory(self, executed_trade):
        self.inventory += executed_trade

    def market_decision(self, market_env, num_steps=1000):
        for _ in range(num_steps):
            market_price = market_env.price
            bid_price, ask_price = self.optimal_bid_ask(market_price)
            # Simulating random trade execution
            if np.random.random() < 0.5:  # Buy executed
                executed_buy = np.random.randint(1, 10)
                self.update_inventory(executed_buy)
                self.cash -= market_env.execute_order(executed_buy)
            else:  # Sell executed
                executed_sell = np.random.randint(1, 10)
                self.update_inventory(-executed_sell)
                self.cash += market_env.execute_order(-executed_sell)

            # Risk management: apply inventory penalty
            penalty = self.inventory_penalty()
            self.cash -= penalty
            
        return self.cash, self.inventory
