# Stock Portfolio Tracker
## Project Overview
The Stock Portfolio Tracker is a beginner-friendly Python program that calculates the total investment value of selected stocks using predefined stock prices and quantities entered by the user.
## Features
- Displays available stocks and their prices.
- Accepts stock symbols and quantities from the user.
- Calculates the value of each stock and the total investment.
- Validates stock symbols and quantities.
- Handles invalid quantity input.
- Saves portfolio information to a CSV file.
## Technologies Used
- Python
- CSV module
- Dictionaries
- Functions
- Loops and conditional statements
- Exception handling
## Available Stocks
| Stock Symbol | Example Price |
| ------------ | ------------: |
| AAPL         |       $180.00 |
| TSLA         |       $250.00 |
| MSFT         |       $420.00 |
| GOOGL        |       $175.00 |

*Note: These are predefined example prices, not live market prices.*

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.

5. Run the command:
```bash
  python stock_portfolio.py
```
   If your Python file has a different name, use that filename instead.

6. Enter the stock symbols and quantities when prompted.
7. Type done to finish entering stocks.
8. View the calculated portfolio total and the generated `stock_portfolio.csv` file.
## Output
The program displays each selected stock, its quantity, price per share, individual value, and the total investment value.

The portfolio is saved in a CSV file that can be opened in spreadsheet applications such as Microsoft Excel.
## Project Purpose
This project was created as part of a Python programming internship task to practice dictionaries, user input, calculations, file handling, and exception handling.
