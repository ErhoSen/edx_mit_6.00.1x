#!/usr/bin/env python
# encoding: utf-8

def fun(balance, interest_rate, min_payment):
    for i in range(1,13):
        unpaid_balance = round(balance - min_payment, 2)
        balance = unpaid_balance + round(interest_rate * unpaid_balance, 2)
    return balance

def main():
    balance = 999999
    annualInterestRate = 0.18
    interest_rate = annualInterestRate/12.0
    lower_bound = balance/12
    #print "l", lower_bound
    upper_bound = round((balance * ((1 + interest_rate)**12))/12.0, 2)
    #print "u", upper_bound
    min_payment = lower_bound + (upper_bound - lower_bound)/2
    #print min_payment
    ans = fun(balance, interest_rate, min_payment)
    counter = 1
    while abs(ans) >= 10 and counter<30:
        #print "result fun", ans
        if ans < 0:
            upper_bound = min_payment
        else:
            lower_bound = min_payment
        #print "Up", upper_bound, "Down", lower_bound
        counter+=1
        min_payment = lower_bound + (upper_bound - lower_bound)/2
        #print "minimum payment", min_payment
        ans = fun(balance, interest_rate, min_payment)
        #print "result fun", ans
        #print "*"*12
    print "Lowest Payment:", round(min_payment,2)
    #print counter

    #monthlyPaymentRate = 0.04
#    min_payment = 0
#    unpaid_balance = balance
#    interest = 0
#    for i in range(1,13):
#        print "Month:", i
#        min_payment = round(balance * monthlyPaymentRate, 2) # balance = 5000
#        buf += min_payment
#        unpaid_balance = round(balance - min_payment, 2)
#        interest = round(interest_rate * unpaid_balance, 2)
#        balance = unpaid_balance + interest
#        print "Minimum monthly payment:", min_payment
#        print "Remaining balance:", balance
#    print "Total paid:", buf
#    print "Remaining balance:", balance


if __name__ == '__main__':
    main()

