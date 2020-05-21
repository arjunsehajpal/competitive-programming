class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        # get index
        index = len(self.prices) - 1
        while index >= 0 and self.prices[index] <= price:
            span = self.spans[index]
            index = index - span
        self.prices.append(price)
        span = len(self.prices) - index - 1
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)