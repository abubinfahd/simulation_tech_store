from mobile_tech import Mobile
from laptop_tech import Laptop
from tech_product import Tech
from sales_person import SalesPerson
from datetime import date


phone_1 = Mobile('iphone_11', 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile('iphone_12', 70000, 500, 'Silver', '1920-1080', 12)
phone_3 = Mobile('iphone_11', 80000, 500, 'Sky-blue', '1920-1080', 13)


laptop_1 = Laptop('Asus g14', 130000, 1.6, 'Black',
                  16, 'rayzen', 1000)
laptop_2 = Laptop('Macbook pro', 130000, 1.7,
                  'Black', 8, 'intel', 1000)
laptop_3 = Laptop('Dell xps', 140000, 1.4, 'Black',
                  16, 'intel core i3', 1000)

# Test Method
print(phone_1)
print(laptop_1)

# Applying the discount cupon
phone_1.apply_discount()
print(phone_1.price)

# Total num of products
print(Tech.get_total_products())

# Shipping Cost
print(laptop_3.calcuilate_shipping_cost(10))

# Setting the double price for the first laptop
print(laptop_1)
laptop_1.set_double_price()
print(laptop_1.price)

# Changing Speces for laptop_3
print(laptop_3)
laptop_3.change_speces(32, 1000)
print(laptop_3)

sales_person_1 = SalesPerson(
    'Majed',
    'Ali',
    40000,
    date(2021, 1, 5),
)

# Adding the products
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(laptop_1)
sales_person_1.sell_product(laptop_2)

# Total products sold
print(sales_person_1.total_products_sold())

# Product sold
sales_person_1.display_sales()

# Calculate Commission
print(sales_person_1.calculate_commission(0.2))

# Sort the sold product
sales_person_1.sort_by_price()
