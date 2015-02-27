#!/usr/bin/env python
# encoding: utf-8


def main():
    balance = 4213
    buf = 0
    annualInterestRate = 0.2
    interest_rate = annualInterestRate/12.0
    monthlyPaymentRate = 0.04
    min_payment = 0
    unpaid_balance = balance
    interest = 0
    for i in range(1,13):
        print "Month:", i
        min_payment = round(balance * monthlyPaymentRate, 2) # balance = 5000
        buf += min_payment
        unpaid_balance = round(balance - min_payment, 2)
        interest = round(interest_rate * unpaid_balance, 2)
        balance = unpaid_balance + interest
        print "Minimum monthly payment:", min_payment
        print "Remaining balance:", balance
    print "Total paid:", buf
    print "Remaining balance:", balance

if __name__ == '__main__':
    main()

