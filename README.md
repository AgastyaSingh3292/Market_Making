# Algorithmic Market Making with Inventory Management

This project implements an algorithmic market-making system that optimally manages inventory risk while maximizing profits. The system uses **stochastic control theory** and **dynamic programming** to solve the inventory management problem.

## Files
- `main.py`: Main script for simulating the market and running the market-making algorithm.
- `market_simulation.py`: Contains the market environment simulation, including price dynamics and order execution.
- `market_maker.py`: Defines the market maker's strategy for managing inventory using dynamic programming and stochastic control.
- `README.md`: Instructions for running the project.

## Requirements
- Python 3.x
- Numpy
- Matplotlib

## How to Run

1. Install the required packages:

    ```
    pip install numpy matplotlib
    ```

2. Run the market-making simulation:

    ```
    python main.py
    ```

3. View the output, which includes the final cash, final inventory, and a plot of the simulated price path.

## Explanation

- **Market Environment**: Simulates price movements using Geometric Brownian Motion, which models realistic price dynamics in financial markets.
- **Market Maker**: Adjusts bid/ask prices dynamically based on current inventory to balance profit maximization and risk minimization. A quadratic penalty is applied to the inventory to discourage holding excessive inventory.

## Future Enhancements

- Implement more sophisticated risk management strategies, such as using dynamic programming to compute optimal policies based on future price expectations.
- Explore alternative inventory penalty functions to better reflect market conditions.
- Integrate order flow prediction models to enhance market-making decisions.
