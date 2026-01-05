"""
Stock Buy And Sell

Problem Statement: You are given an array of prices where prices[i] is the price 
of a given stock on an ith day. You want to maximize your profit by choosing a 
single day to buy one stock and choosing a different day in the future to sell 
that stock. Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Approach: Track minimum price seen so far and calculate profit at each step.
"""

prices = [7,6,4,3,4,1]

def max_profit(arr):
    pro = 0
    num = +1000
    for i in arr:
        if i < num:
            num = i
        curr_pro = i - num
        if curr_pro > pro:
            pro = curr_pro
    return pro

print(max_profit(prices))
