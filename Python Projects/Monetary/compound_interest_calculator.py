# Compound Interest Calculator
# A = P(1 + r/n)^nt

p = float(input("Enter initial investment amount ($): "))
r = float(input("Enter annual interest rate (eg. 0.05): "))
n = int(input("Enter the amount of times the interest is compounded per year: "))
t = float(input("Enter the time in years: "))

a = p*(1+(r/n))**(n*t)
print("${:,.2f}".format(a))