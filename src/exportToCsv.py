import csv
from orders import generate_list_of_orders

def export_list_of_orders_to_csv(): 
    generatedList = generate_list_of_orders();
    orderList = generatedList[0];
    customerList = generatedList[1];

    order_csv = open('orders.csv', 'w')
    product_csv = open('products.csv', 'w')
    customer_csv = open('customers.csv', 'w')
    csv_order_writer = csv.writer(order_csv)
    csv_product_writer = csv.writer(product_csv)
    csv_customer_writer = csv.writer(customer_csv)

    customerCount = 0;
    orderCount = 0;

    for customer in customerList:
        if customerCount == 0:
            customerHeader = ['postalCode', 'city', 'customerId']
            csv_customer_writer.writerow(customerHeader)
            customerCount += 1;

        csv_customer_writer.writerow(customer.values())
        
    for order in orderList: 
        if orderCount == 0:
            #write header
            orderHeader = order.keys()
            productHeader = ['designType', 'price', 'size']
            csv_product_writer.writerow(productHeader)
            csv_order_writer.writerow(orderHeader)
            orderCount += 1
            
        csv_order_writer.writerow(order.values())
        productRow = [order['designType'], order['subtotal'], order['size']]
        csv_product_writer.writerow(productRow)

    order_csv.close()