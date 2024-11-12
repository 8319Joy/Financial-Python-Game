#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Define initial variables
balance = 10000  # Starting balance
stocks = {"TechCorp": 100, "HealthInc": 200, "AutoMotive": 50}  # Initial stock prices
portfolio = {"TechCorp": 0, "HealthInc": 0, "AutoMotive": 0}  # Empty portfolio
days = 0  # Track game days

# Function to display current status
def display_status():
    print("\nDay:", days)
    print("Balance:", balance)
    print("Stock Prices:", stocks)
    print("Your Portfolio:", portfolio)

# Function to simulate price changes
def update_stock_prices():
    for stock in stocks:
        change = random.uniform(-0.05, 0.05)  # Price change between -5% to 5%
        stocks[stock] = round(stocks[stock] * (1 + change), 2)

# Function to buy stocks
def buy_stock(stock, amount):
    global balance
    cost = stocks[stock] * amount
    if cost <= balance:
        balance -= cost
        portfolio[stock] += amount
        print(f"Bought {amount} shares of {stock} at {stocks[stock]} each.")
    else:
        print("Insufficient balance to buy that many shares.")

# Function to sell stocks
def sell_stock(stock, amount):
    global balance
    if amount <= portfolio[stock]:
        portfolio[stock] -= amount
        earnings = stocks[stock] * amount
        balance += earnings
        print(f"Sold {amount} shares of {stock} at {stocks[stock]} each.")
    else:
        print("You don't own that many shares.")

# Main game loop
print("Welcome to the Financial Analysis Game!")
while days < 10:  # Play for 10 days
    days += 1
    update_stock_prices()
    display_status()

    # Ask player for action
    action = input("Choose an action (buy/sell/hold/exit): ").strip().lower()

    if action == "buy":
        stock = input("Enter the stock to buy (TechCorp, HealthInc, AutoMotive): ").strip()
        amount = int(input("Enter the number of shares: "))
        if stock in stocks:
            buy_stock(stock, amount)
        else:
            print("Invalid stock choice.")
    
    elif action == "sell":
        stock = input("Enter the stock to sell (TechCorp, HealthInc, AutoMotive): ").strip()
        amount = int(input("Enter the number of shares: "))
        if stock in stocks:
            sell_stock(stock, amount)
        else:
            print("Invalid stock choice.")
    
    elif action == "hold":
        print("You chose to hold your investments.")
    
    elif action == "exit":
        break
    
    else:
        print("Invalid action. Choose buy, sell, hold, or exit.")

# Final report
print("\nGame Over!")
print("Final Balance:", balance)
for stock, qty in portfolio.items():
    value = qty * stocks[stock]
    print(f"{stock}: {qty} shares, Current Value: ${value:.2f}")
print("Thanks for playing!")


# In[ ]:




