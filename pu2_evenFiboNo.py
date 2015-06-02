#!/bin/python2.7
"This is the solution for second problem of project euler"
"Problem 2: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:"

"1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..."

"By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."

"Point to note here is we have to only add every third term in the series to get the sum"

def fibo_sum(limit):
    sum = 0
    f = 1
    s = 1
    t = f + s
    while t < limit:
        sum += t
        f = s + t
        s = t + f
        t = f + s

    print sum

def main():
    "Main function "
    fibo_sum(4000000)

main()