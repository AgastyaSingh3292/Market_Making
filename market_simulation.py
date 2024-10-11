import numpy as np

class MarketEnvironment:
    def __init__(self, initial_price=100, volatility=0.02, drift=0.01):
        self.price = initial_price
        self.volatility = volatility
        self.drift = drift

    def simulate_price_movement(self, num_steps=1000):
        price_path = [self.price]
        for _ in range(num_steps):
            # Geometric Brownian Motion for price dynamics
            shock = np.random.normal(loc=self.drift, scale=self.volatility)
            self.price = self.price * (1 + shock)
            price_path.append(self.price)
        return np.array(price_path)
    
    def execute_order(self, order_size):
        # Simulate order execution at the current price
        return order_size * self.price
