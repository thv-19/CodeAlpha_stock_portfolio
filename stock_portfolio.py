import csv
stock_prices={"AAPL": 180.00,
              "TSLA":250.00,
              "MSFT": 420.00,
              "GOOGL": 175.00
              } 
# Predefined stock prices
def display_stock():
    print("\nAvailable Stocks")
    print("-"* 35)
    for symbol,price in stock_prices.items():
        print(f"{symbol}: ${price:.2f} per sahre")
       
       
def calculate_portfolio():
    portfolio={}
    display_stock()
    print("\nEnter the stock symbol and quantity.")
    print("Type 'done' when you fnish.\n")
    while True:
        symbol= input("Stock symbol: ").strip().upper()
        if symbol== "DONE":
            break
        if symbol not in stock_prices:
            print("Invalid symbol. Please choose an available stock.")
            continue
        try:
            quantity=int(input("Quantity: "))
            if quantity<=0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid whole numbers.")
            continue
        portfolio[symbol]= portfolio.get(symbol, 0)+ quantity
        print(f"Added{quantity} shares of {symbol}.")
    if not portfolio :
        print("\nNo stocks were added.")
        return
    print("\n" + "=" * 45)
    print("STOCK PORTFOLIO SUMMARY")
    print("=" * 45)
    total_investment = 0
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value=price * quantity
        total_investment +=value
        print(
            f"{symbol:<10}"
            f"Quantity: {quantity:<5}"
            f"Price: ${price:>8.2f}  "
            f"Value: ${value:>10.2f}"
              )
    print("-"*45)
    print(f"Total Investment: ${total_investment:.2f}")
    save_portfolio(portfolio,total_investment)
def save_portfolio(portfolio, total):
    filename= "stock_portfolio.csv"

    try:
        with open (filename, "w", newline="") as file:
            writer= csv.writer(file)
            writer.writerow(["Stock Symbol",
                "Quantity",
                "Price Per Share",
                "Total Value"
            ])
            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                value = price * quantity
                writer.writerow([
                    symbol,quantity,price,value
                ])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])
        print(f"\nPortfolio saved successfuly to {filename}.")
    except OSError as error:
        print(f"COULD NOT SAVE THE FILE: {error}")
def main():
    print("="* 40)
    print("STOCK PORTFOLIO TRACKER")
    print("="* 40)
    while True:
        calculate_portfolio()
        choice = input(
            "\nWould you like to create another portfolio? (yes/no): "
        ).strip().lower()

        if choice not in ("yes", "y"):
            print("\nThank you for using Stock Portfolio Tracker!")
            break
if __name__=="__main__":
    main()