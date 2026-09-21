products = {
    "P001": {"name": "Keyboard", "price": 15000, "stock": 10},
    "P002": {"name": "Mouse", "price": 8000, "stock": 25},
    "P003": {"name": "Monitor", "price": 85000, "stock": 5},
    "P004": {"name": "USB Cable", "price": 3000, "stock": 50},
}

orders = [
    {"id": 1001, "customer": "Alice", "items": [("P001", 2), ("P002", 1)]},
    {"id": 1002, "customer": "Bob", "items": [("P003", 1), ("P004", 3)]},
    {"id": 1003, "customer": "Alice", "items": [("P002", 2), ("P004", 5)]},
]
def validate_order(order, products:dict):
    for item in order["items"]:
        if item <= 0:
            return False
        if not (item[1] in products.keys()):
            return False
        elif products[item[0]]["stock"] < item[1]:
            return False
        return True

def calculate_order_total(order, products:dict):
    if validate_order(order, products):
        ls = order["items"]
        temp = []
        for i in ls:
            temp.append(products[i[0]]*i[1])
        return sum(temp)
 
def process_order(order, products):
    if validate_order(order, products):
        ls = order["items"]
        for i in ls:
            products[i[0]]["stock"] -= i[1]
        return calculate_order_total(order, products)
    else:
        raise ValueError

def customers_totals(orders, proructs):
    temp = {}
    for order in orders:
        temp[order["customer"]] += calculate_order_total(order, products)
    return temp

def most_expensive_order(orders, products):
    
    for order in orders: