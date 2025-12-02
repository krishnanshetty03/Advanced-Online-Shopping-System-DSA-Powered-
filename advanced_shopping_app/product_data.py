# PRODUCT STORAGE USING ARRAY + HASH TABLE

# Array of products
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 50000},
    {"id": 2, "name": "Mouse", "category": "Accessories", "price": 500},
    {"id": 3, "name": "Keyboard", "category": "Accessories", "price": 1200},
    {"id": 4, "name": "Headphones", "category": "Electronics", "price": 1500},
    {"id": 5, "name": "USB Cable", "category": "Accessories", "price": 200},
    {"id": 6, "name": "iPhone", "category": "Mobile", "price": 80000},
]

# Hash Table for O(1) product search
product_hash = {}

def build_hash_table():
    for product in products:
        product_hash[product["name"].lower()] = product
