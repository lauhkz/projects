purchase_orders = [{'price': 10.0, 'money_available': 125.0},
                   {'price': 5.0, 'money_available': 2.0},
                   {'price': 20.01, 'money_available': 5.2},
                   {'price': 1.04, 'money_available': 254.0},
                   {'price': 40.2, 'money_available': 6.0},
                   {'price': 16.0, 'money_available': 235.01},
                   {'price': 10.7, 'money_available': 10.7},
                   {'price': 12.0, 'money_available': 2.3}]

def process_transactions(purchase_orders):
    # this was my approuch to the problem
    leftovers = []
    for order in purchase_orders:
        try:
            leftovers.append(purchase_item(order['price'], order['gold_available']))
        except Exception as e:
            print(e)
    print(leftovers)

    """
    This is the solution given in the exercise:

    def process_transactions(purchase_orders):
        leftovers = []
        for order in purchase_orders:
            try:
                price = order["price"]
                money = order["gold_available"]
                leftover = purchase_item(price, money)
                leftovers.append(leftover)

            except Exception as e:
                print(e)
        return leftovers

        thoughts: Good idea to put the values of the orders in variables to use in the purchase_item function,
        makes the code more "clean" and more easier to read.
    """
# Don't edit below this line


def main():
    print("processing transactions...")
    leftovers = process_transactions(
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 2.00},
            {"price": 20.01, "money_available": 5.20},
            {"price": 1.04, "money_available": 254.00},
            {"price": 40.20, "money_available": 6.00},
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 10.70},
            {"price": 12.00, "money_available": 2.30},
        ]
    )
    print("Purchases complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase_item(price, money_available):
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price


main()

