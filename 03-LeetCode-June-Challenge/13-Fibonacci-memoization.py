class Solution:
    dict_ = {}
    def fib(self, N):
        if N<2:
            return N
        else:
            if N in self.dict_:
                return self.dict_[N]
            else:
                self.dict_[N] = self.fib(N-1) + self.fib(N-2)
                return self.dict_[N]
        