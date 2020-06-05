class Solution:
    def twoCitySchedCost(self, costs):
        costs.sort(key = lambda x: x[0] - x[1])
        
        sum_ = 0
        for i in range(0, int(len(costs)/2)):
            sum_ += costs[i][0]
            
        for i in range(int(len(costs)/2), len(costs)):
            sum_ += costs[i][1]
            
        return sum_