"""
Selection 
"""

def excessBaggagePrice(fare,weight):
    if weight <= 22:
        return "No charge"

    else:
        return f"The charge for excess baggage is {(weight-22)*(0.02*fare)}"

print(excessBaggagePrice(100,24))

def temperatureCheck(temperature):
    if temperature < 80:
        return "Warning - temperature is below normal"
    
    elif temperature < 100:
        return "Temperature in normal range"

    else:
        return "Warning. Cooling unit malfunction"

print(temperatureCheck(78))

def balanceCheck(customerBalance,withdraw):
    if customerBalance - withdraw < 0:
        return "Insufficient funds"
    
    else:
        return f"{withdraw} has been withdrawn and you have {customerBalance-withdraw} left"

print(balanceCheck(100,10))

def discount(purchasePrice):
    if purchasePrice > 10:
        return f"new price is {purchasePrice*0.9} with {purchasePrice*0.1} being discounted"

print(discount(15))

def hardwarePrice(bolt,nut,washer):
    boltPrice = 0.05
    nutPrice = 0.03
    washerPrice = 0.01
    if bolt > nut:
        return f"Check the order Price is {bolt*boltPrice+nut*nutPrice+washer*washerPrice} pence"
    else:
        return f"Order is Ok. Price is {bolt*boltPrice+nut*nutPrice+washer*washerPrice} pence"

print(hardwarePrice(3,4,5))

def deliveryPrice(costPackage,weightPackage,overnightDelivery):
    discountRate = 0.0
    weightCost = 0
    overnightCost = 0
    if costPackage > 100:
        discountRate = 0.2
    
    if weightPackage < 1:
        weightCost = 5
    elif weightPackage < 5:
        weightCost = 7.50
    else:
        weightCost = 10.00

    if overnightDelivery == True:
        overnightCost = 10

    return (f"Total cost of package is {costPackage + (overnightCost + weightCost) * ( 1 - discountRate ) }")

print(deliveryPrice(150,10,True))
       