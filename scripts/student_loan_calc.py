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

# get student loan payments (note: assume first two are the same? or no?)
loanpayments = [
    float(input("First loan payment: £")),
    float(input("Second loan payment: £")),
    float(input("Third loan payment: £")),
]

print()

# get savings amount
savings = float(input("Savings: £")) # TODO: default to 0

print()

# get accomodation payments 
accompayments = [
    float(input("First accomodation payment: £")),
    float(input("Second accomodation payment: £")),
    float(input("Third accomodation payment: £")),
]

print()

# get end and start dates
#startdate = parse(input("Date to start (dd/mm/yyyy): "), dayfirst=True) #assumed to be first payment date
enddate = parse(input("Date to end (dd/mm/yyyy): "), dayfirst=True)

print()

# calc!!!
duration = ((enddate-firstpaymentd).days) / 7 # get amount of days, divide by 7 for weeks
savingspw = savings / duration # get amount of savings to add per week

firsttermd = (((secondpaymentd - firstpaymentd).days)/7) # durations of terms
secondtermd = (((thirdpaymentd - secondpaymentd).days)/7)
thirdtermd = (((enddate - thirdpaymentd).days)/7)

firstterm = (((loanpayments[0] - accompayments[0]) / firsttermd) + (firsttermd * savingspw)) # amount per week for all 3 terms
secondterm = (((loanpayments[1] - accompayments[1]) / secondtermd + (secondtermd  * savingspw)))
thirdterm = (((loanpayments[2] - accompayments[2]) / thirdtermd + (thirdtermd * savingspw)))

# Out
print(f"Totals per week:\nFirst term: £{floor(firstterm)}\nSecond term: £{floor(secondterm)}\nThird term: £{floor(thirdterm)}")

# issues:
# - savings assumes to be spread out evenly across year!
# - no way to account for weeks where money isnt needed (eg visiting parents or whatever lol)
# - hardcoded term dates (read from file if not added already?)
# - no parent contributions; leave it like that?