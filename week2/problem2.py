#!/usr/bin/env python
# encoding: utf-8

def fun(balance, annualInterestRate, min_payment):
    interest_rate = annualInterestRate/12.0
    for i in range(1,13):
        unpaid_balance = round(balance - min_payment, 2)
        balance = unpaid_balance + round(interest_rate * unpaid_balance, 2)
    return balance

def main():
    min_payment = 0
    balance = 999999
    annualInterestRate = 0.18
    min_payment = fun(balance, annualInterestRate, 8150)
#    for j in range(10, int(balance/(10* annualInterestRate)), 10):
#        if fun(balance, annualInterestRate, j) < 0:
#            min_payment = j
#            break
    print "Lowest Payment:", min_payment


if __name__ == '__main__':
    main()

