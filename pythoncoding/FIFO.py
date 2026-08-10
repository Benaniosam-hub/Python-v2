'''Simulate a Queue (FIFO)

Simulate a customer service queue using a list:

Add three customers ("Customer 1", "Customer 2", "Customer 3") using 
.append()

Serve (remove) customers in First-In, First-Out order using .pop(0) 
and print who is being served.'''

customer_service = []
customer_service.append("Customer 1")
customer_service.append("Customer 2")
customer_service.append("Customer 3")
new = customer_service.copy()
print (customer_service)

for i in new:
    print("We served for the : "+ customer_service.pop(0))

