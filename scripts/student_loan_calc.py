from datetime import datetime
from dateutil.parser import parse
from math import floor

# get student loan amount, accomodation payments, savings amounts,
# and dates and give budget amounts for the year!
# TODO: go off arguments? as an option maybe? include --help if so
# TODO: trycatches
# TODO: let user request to make last term be the same, then output how much savings left?

# hardcoded payment dates
firstpaymentd = datetime(2024, 9, 23)
secondpaymentd = datetime(2025, 1, 13)
thirdpaymentd = datetime(2025, 5, 28)

# get student loan payments
loanpayments = [
    float(input("First loan payment: £")),
    float(input("Second loan payment: £")),
    float(input("Third loan payment: £")),
]

print()

# get savings amount
savings = input("Savings: £") 
if savings == "": savings = 0.0 # TODO: default to 0
else: float(savings)

print()

# get accomodation payments 
accompayments = [
    float(input("First accomodation payment: £")),
    float(input("Second accomodation payment: £")),
    float(input("Third accomodation payment: £")),
]

print()

# get end date, assume start to be first payment
enddate = parse(input("Date to end (dd/mm/yyyy): "), dayfirst=True)

print()

# calc!!!
def gettermamount(fromd, tod, loanamount, savingspw, accomp):
    #fromd = term start date
    #tod = term end date
    #loanamount = total amount of loan available for this term
    #savingspw = savings to be added to each week
    #accomp = accomodation payment for this term
    lengthinweeks = (((tod - fromd).days)/7)
    payment = (((loanamount - accomp) / lengthinweeks) + (savingspw * lengthinweeks))
    return floor(payment)

duration = ((enddate-firstpaymentd).days) / 7 # get amount of days, divide by 7 for weeks, for savingspw calc
savingspw = savings / duration # get amount of savings to add per week

firstterm = gettermamount(firstpaymentd, secondpaymentd, loanpayments[0], savingspw, accompayments[0])
secondterm = gettermamount(secondpaymentd, thirdpaymentd, loanpayments[1], savingspw, accompayments[1])
thirdterm = gettermamount(thirdpaymentd, enddate, loanpayments[2], savingspw, accompayments[2])

# Out
print(f"Totals per week:\nFirst term: £{firstterm}\nSecond term: £{secondterm}\nThird term: £{thirdterm}")

# issues:
# - savings assumes to be spread out evenly across year!
# - hardcoded term dates (read from file?)
# - no parent contributions; leave it like that?