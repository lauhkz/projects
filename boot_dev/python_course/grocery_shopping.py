items_purchased = ['milk', 'eggs', 'cheese', 'apples', 'bananas', 'lettuce', 'cereal']
grocery_list = ['milk', 'oatmeal', 'eggs', 'cheese', 'apples', 'bananas', 'carrots', 'lettuce', 'potatoes', 'cereal', 'chicken']

def calculate_total (items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }
    purchased_items = {}
    total = 0
    unpurchased_items = {}

    for item in items_purchased:
        if item in item_prices:
            purchased_items[item] = item_prices[item]
            total += item_prices[item]

    for item in grocery_list:
        if item not in items_purchased:
            print (f"items:{item}")
            unpurchased_items[item] = grocery_list[item]


    print(purchased_items)
    print(f"items that got left to buy: {unpurchased_items}")
    print(f"this is the total {total}")



calculate_total(items_purchased, grocery_list)
