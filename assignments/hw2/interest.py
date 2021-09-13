"""

Name: Derek Kai Oriee
interest.py

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""


def main():

    monthlyintrest = eval(input("What is your monthly interest?: "))
    billcycle = 31
    netbal = eval(input("What is your net balance?: "))
    netpay = eval(input("How much did you pay?: "))
    daysbeforeapay = eval(input("How many days did you pay for your bills ahead of time?: "))

    totalnetbal = netbal * billcycle  # multiply the net balance by the number of days in tne billing cycle
    totalpay = netpay * daysbeforeapay  # multiply the net payment received by the amount of days the user payed
    # before the due date

    total = totalnetbal - totalpay  # Find the total between the total net balance and the total amount paid
    overallfee = total / billcycle  # find the over all fee by dividing the total by the number of days in the
    # billing cycle
    yearlyintrest = (monthlyintrest / 12) / 100  # simplify the yearly interest
    totalintrest = overallfee * yearlyintrest  # find the total yearly interest rate

    print("Your monthly interest rate is $", round(totalintrest, 2))
