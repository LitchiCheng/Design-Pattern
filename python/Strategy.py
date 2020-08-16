class Strategy:
    def doOperation(self):
        pass

class StrategyOne(Strategy):
    def doOperation(self):
        print("i am one")

class StrategyTwo(Strategy):
    def doOperation(self):
        print("i am two")

class Content:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def run(self):
        self._strategy.doOperation()

if __name__ == "__main__":
    strategy1 = StrategyOne()
    content = Content(strategy1)
    content.run()
    print("next strategy")
    strategy2 = StrategyTwo()
    content = Content(strategy2)
    content.run()
    