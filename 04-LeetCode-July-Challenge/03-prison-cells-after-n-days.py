class Solution:
    def prisonAfterNDays(self, cells, N):
        # initialize a dictionary
        dict_ = {}
        self.cells = cells
        for i in range(N):
            # converting the cell formation to string, so it can be used as a key
            s = str(self.cells)
            
            # checking if s is in dict.
            # if it is there, we know that loop is completed ..
            # .. and all the formations will repeat from now onwards
            if s in dict_:
                loop_length = i - dict_[s]
                remaining_days = (N-i)%loop_length
                
                # shorten the number of remaining days
                return self.prisonAfterNDays(self.cells, remaining_days) 
            
            else:
                # creating the key-value pair
                dict_[s] = i
                prev = self.cells[0]
                for j in range(1, 7):
                    curr, next_ = self.cells[j], self.cells[j+1]
                    
                    # subtracting XOR of prev and next from 1
                    self.cells[j] = 1 - (prev ^ next_)
                    prev = curr
                    
            self.cells[0] = 0
            self.cells[7] = 0
        return self.cells