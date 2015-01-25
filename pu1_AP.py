#!/bin/python2.7
"This is the solution for first problem of project euler"
"Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9."
"The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."

"Thing to note here is we can count from zero and see the no. if divide by 3 or 5 then can solve the problem"
"But we can also use formulae of AP intelligently and solve the problem in much less time."

def AP(start, end, gap):
    "calculate the sum of the AP series from start to end with gap of gap"
    "sum = (start + end) * total_no / 2"
    
    while(end % gap != 0):
        end -= 1;
    
    total_no = ((end - start) / gap ) + 1
    return ((end + start) * total_no) / 2

def main():
    "Main function it calls AP for sum with 3, 5 and 15"
    sum_3 = AP(3, 999, 3)
    sum_5 = AP(5, 999, 5)
    sum_15 = AP(15, 999, 15)
    
    print sum_3 + sum_5 - sum_15

main()
