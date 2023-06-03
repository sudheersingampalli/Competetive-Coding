'''
Problem Description
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum total value that we can fit in the knapsack. If the maximum total value is ans, then return ⌊ans × 100⌋ , i.e., floor of (ans × 100).

NOTE:
You can break an item for maximizing the total value of the knapsack

Input Format
First argument is an integer array A of size N denoting the values on N items.
Second argument is an integer array B of size N denoting the weights on N items.
Third argument is an integer C denoting the knapsack capacity.

Output Format
Return a single integer denoting the maximum total value of A such that sum of the weights of this subset is smaller than or equal to C.

Example Input
Input 1:
 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50
Input 2:
 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10

Example Output
Output 1:
 24000
Output 2:
 2105

Example Explanation
Explanation 1:

Taking the full items with weight 10 and 20 and 2/3 of the item with weight 30 will give us 
the maximum value i.e 60 + 100 + 80 = 240. So we return 24000.
Explanation 2:

Taking 10/19 the fourth item gives us the maximum value i.e. 21.0526. So we return 2105.

Solution:: sort the arrays in descending order of value per weight. Fill the sack till remaining weight can be filled by existing weight as a whole.
Next whatever small portion of the weight needs to be filled, take that fration of weight from the existing weights.
'''

import decimal
class Solution:

    def solve(self, values, weights, C):
        items = [(val, weight, val/weight) for val, weight in zip(values, weights)]
        items.sort(key=lambda x:x[2], reverse=True)
        max_val = 0
        current_capacity = C
        for item in items:
            val, weight, ratio = item
            if weight <= current_capacity:
                max_val += val
                current_capacity -= weight
            else:
                fraction = current_capacity/weight
                max_val += val*fraction
                break
        max_val = decimal.Decimal(str(max_val))
        return int(max_val*100)
