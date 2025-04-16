from collections import defaultdict

fix_messages = open('/Users/pavelshevchenko/Desktop/FIX Challenge/fix_sample.txt').read().strip().split("\n")

duplicate_errors = []
account_prices = defaultdict(list)


for i, msg in enumerate(fix_messages):
    fields = msg.split("|")
    tags = {}
    duplicates = set()
    for field in fields:
        if '=' not in field:
            continue
        tag, value = field.split("=")
        if tags.get(tag):
            duplicates.add(tag)
        tags[tag] = value

    if duplicates:
        duplicate_errors.append(f"Duplicate tag at line {i+1}: {', '.join(duplicates)}")

    
    if tags.get("35") == "D":
        account = tags.get("1")
        price = float(tags.get("44"))
        if account and price:
            account_prices[account].append(price)
    
print("Duplicate Errors:")
for error in duplicate_errors:
    print(error)
print("\nAccount Prices:")
for account, prices in account_prices.items():
    print(f"Account {account} has a minimum price of {min(prices)} and a maximum price of {max(prices)}")
        