import re
from collections import Counter

def main():
    # Read the CSV file with the product orders
    with open('/Users/leonthies/Desktop/Studium/3.Semester/DataModeling/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expressions for each data type

    # Extract order numbers (e.g., "12345")
    order_number_regex = r'Order #(\d+)'
    order_numbers = re.findall(order_number_regex, text)

    # Extract product names (e.g., "Laptop", "Headphones")
    product_name_regex = r'Product: ([A-Za-z\s]+),'
    product_names = re.findall(product_name_regex, text)

    # Extract prices (e.g., "$899.99")
    price_regex = r'Price: \$(\d+\.\d{2})'
    prices = re.findall(price_regex, text)

    # Extract order dates (e.g., "2023-09-15")
    date_regex = r'Date: (\d{4}-\d{2}-\d{2})'
    dates = re.findall(date_regex, text)

    # Find orders with prices over $500
    expensive_orders = [(order_numbers[i], product_names[i], prices[i], dates[i]) 
                        for i in range(len(prices)) if float(prices[i]) > 500]

    # Change the date format to DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]

    # Extract product names that have more than 6 characters
    long_product_names = [product for product in product_names if len(product) > 6]

    # Count the occurrence of each product
    product_count = Counter(product_names)

    # Extract orders with prices ending in .99
    orders_ending_in_99 = [(order_numbers[i], product_names[i], prices[i], dates[i]) 
                           for i in range(len(prices)) if prices[i].endswith('.99')]

    # Find the cheapest product (min price)
    min_price_index = prices.index(min(prices, key=lambda x: float(x)))
    cheapest_product = (order_numbers[min_price_index], product_names[min_price_index], prices[min_price_index], dates[min_price_index])

    # Print the results
    print("Order Numbers:", order_numbers)
    print("Product Names:", product_names)
    print("Prices:", prices)
    print("Order Dates:", dates)
    print("Orders with prices over $500:", expensive_orders)
    print("Formatted Dates (DD/MM/YYYY):", formatted_dates)
    print("Product Names (more than 6 characters):", long_product_names)
    print("Product Counts:", product_count)
    print("Orders with prices ending in .99:", orders_ending_in_99)
    print("Cheapest Product:", cheapest_product)

if __name__ == '__main__':
    main()
