import numpy as np
import matplotlib.pyplot as plt
from market_simulation import MarketEnvironment
from market_maker import MarketMaker

if __name__ == "__main__":
    # Set up market environment and market maker
    market_env = MarketEnvironment(initial_price=100, volatility=0.02, drift=0.01)
    market_maker = MarketMaker(initial_inventory=0, risk_aversion=0.01)

    # Simulate price movements
    price_path = market_env.simulate_price_movement(num_steps=1000)
    
    # Let the market maker manage inventory and place orders
    final_cash, final_inventory = market_maker.market_decision(market_env, num_steps=1000)

    # Output final results
    print(f"Final Cash: {final_cash:.2f}")
    print(f"Final Inventory: {final_inventory}")

    # Plot the price path
    plt.plot(price_path)
    plt.title("Simulated Price Path")
    plt.xlabel("Time Steps")
    plt.ylabel("Price")
    plt.show()
