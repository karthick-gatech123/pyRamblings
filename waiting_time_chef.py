# Courtesy Leetcode - 1701 Average Waiting Time
#  similar to FCFS scheduling in OS

# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
# arrivali =  arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei = time needed to prepare the order of the ith customer
# Input: customers = [[1,2],[2,5],[4,3]]
# Output: 5.00000
# first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3
#   waiting time of the first customer is 3 - 1 = 2.
# second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8
#   waiting time = 8 - 2 = 6
# third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11
#   waiting time = 11 - 4 = 7
#   average waiting time = (2 + 6 + 7) / 3 = 5.



def averageWaitingTime(self, customers: List[List[int]]) -> float:
    next_idle_time, net_wait_time = 0, list()
    for customer in customers:
      # The next idle time for chef = arrival time of customer[i] + time for preparing that customer order
      # in case of first customer = [1,2] , next idle time for chef = 3
      # note that for next customers, we need to consider the time at which previous customer order was serviced. Hence max of these values
      next_idle_time = max(customer[0], next_idle_time) + customer[1]
      net_wait_time.append(next_idle_time - customer[0])
    average_wait_time = sum(net_wait_time) / len(customers)
    return average_wait_time
