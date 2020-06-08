class Solution:
    def change(self, amount, coins):
        m = len(coins)
        combinations = self.coins_combinations(coins, m, amount)
        return combinations
    
    def coins_combinations(self, coins, m, amount):
        if amount == 0:
            return 1
        if m == 0:
            return 0
        
        table = [[0 for x in range(m)] for x in range(amount+1)] 

        for i in range(m): 
            table[0][i] = 1

        # Fill rest of the table entries in bottom up manner 
        for i in range(1, amount+1): 
            for j in range(m): 

                # Count of solutions including S[j] 
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0

                # Count of solutions excluding S[j] 
                y = table[i][j-1] if j >= 1 else 0

                # total count 
                table[i][j] = x + y 

        return table[amount][m-1] 