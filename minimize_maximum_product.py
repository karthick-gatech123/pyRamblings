# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

# n = 7, quantities = [15,10,10]
# Output: 5
# Explanation: One optimal way is:
# - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
# - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
# - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
# The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

# all products have to be distributed but some stores need not receive any
# 
# Using a binary search approach on the output
# 
# in case of first example, n is 6 and output can be between 0 to 11? 
#   

def minimizedMaximum(self, n, quantities) -> int:
        left = 0
        right = max(quantities)

        def can_distribute(x, n) -> bool:
            # function to check if its possible to distribute the products
            # such that no store receives more than x products
            j = 0
            remaining = quantities[j]
            for i in range(n):
                if remaining <= x:
                    j += 1
                    if j == len(quantities):
                        return True
                    else:
                        remaining = quantities[j]
                else:
                    remaining = remaining - x

            return False

        while left < right:
            middle = (left + right) // 2
            if can_distribute(middle, n):
                # Try for a smaller maximum
                right = middle
            else:   
                left = middle + 1
        return left