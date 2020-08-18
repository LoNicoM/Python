# Fixed Rate Mortgage calculator

principal = 267000.00
annRate  = 2.71
term = 26
frequency = 12
extraPayment = 150

def period(): # first function
    if frequency == 12:
        period = "monthly"
    elif frequency == 52:
        period = "weekly"
    else:
        period = "other period"
    return period

installments = frequency * term
installRate = annRate / 100 / frequency

repaymentPart1 = installRate * principal
repaymentPart2 = 1 - ((1 + installRate) ** -installments)
repayment = repaymentPart1 / repaymentPart2

print("There are {0} installments".format(installments))
print("\nYour {1} repayment = ${0}".format(round(repayment,2), period())) # function called here

balance = principal
totalInterest = 0.0
payments = 0

print("\n| {0:4} | {1:^12} | {2:^12} | {3:^12} |".format("No.","Balance","Interest","Total Intrst"))
print("{0:->53}".format(""))


while balance > repayment:
    interest = installRate * balance
    balance = balance - repayment - extraPayment + interest
    totalInterest = totalInterest + interest
    payments += 1
    print("| {0:^4} | $ {1:10.2f} | $ {2:10.2f} | $ {3:10.2f} |".format(payments,balance,interest,totalInterest))

if balance > 0.0:
    payments += 1
    print("Total of {1} payments Final payment of ${0:0.2f}".format(balance,payments))

