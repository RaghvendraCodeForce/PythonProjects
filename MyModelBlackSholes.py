import math
from scipy.stats import norm


def calculate_call_option_price(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility):
    """
    Calculate the price of a European call option using the Black-Scholes model.

    :param stock_price: Current stock price (spot price)
    :param strike_price: The strike price of the option
    :param time_to_maturity: Time to maturity in years (e.g., 1 year)
    :param risk_free_rate: Risk-free interest rate (annualized, as a decimal)
    :param volatility: Volatility of the stock (annualized, as a decimal)
    :return: Price of the European call option
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (math.log(stock_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_maturity) / (
                volatility * math.sqrt(time_to_maturity))
    d2 = d1 - volatility * math.sqrt(time_to_maturity)

    # Calculate the call option price
    call_price = stock_price * norm.cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2)

    return call_price


def calculate_put_option_price(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility):
    """
    Calculate the price of a European put option using the Black-Scholes model.

    :param stock_price: Current stock price (spot price)
    :param strike_price: The strike price of the option
    :param time_to_maturity: Time to maturity in years (e.g., 1 year)
    :param risk_free_rate: Risk-free interest rate (annualized, as a decimal)
    :param volatility: Volatility of the stock (annualized, as a decimal)
    :return: Price of the European put option
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (math.log(stock_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_maturity) / (
                volatility * math.sqrt(time_to_maturity))
    d2 = d1 - volatility * math.sqrt(time_to_maturity)

    # Calculate the put option price
    put_price = strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2) - stock_price * norm.cdf(
        -d1)

    return put_price


def get_user_inputs():
    """
    Prompt the user to input values for stock price, strike price, time to maturity,
    risk-free interest rate, and volatility.

    :return: Tuple of (stock_price, strike_price, time_to_maturity, risk_free_rate, volatility)
    """
    print("Welcome to the Black-Scholes Option Pricing Calculator!\n")

    # User input for various parameters
    stock_price = float(input("Enter the current stock price (S0): "))
    strike_price = float(input("Enter the strike price (K): "))
    time_to_maturity = float(input("Enter the time to maturity in years (T): "))
    risk_free_rate = float(input("Enter the risk-free interest rate (r) in decimal (e.g., 0.05 for 5%): "))
    volatility = float(input("Enter the volatility (σ) in decimal (e.g., 0.2 for 20%): "))

    return stock_price, strike_price, time_to_maturity, risk_free_rate, volatility


def display_results(call_price, put_price):
    """
    Display the calculated call and put option prices.

    :param call_price: The price of the European call option
    :param put_price: The price of the European put option
    """
    print("\n===============================")
    print(f"European Call Option Price: ${call_price:.2f}")
    print(f"European Put Option Price: ${put_price:.2f}")
    print("===============================\n")


if __name__ == "__main__":
    # Step 1: Get user inputs
    stock_price, strike_price, time_to_maturity, risk_free_rate, volatility = get_user_inputs()

    # Step 2: Calculate the option prices
    call_option_price = calculate_call_option_price(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                                    volatility)
    put_option_price = calculate_put_option_price(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                                  volatility)

    # Step 3: Display the results
    display_results(call_option_price, put_option_price)