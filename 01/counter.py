class Counter:
    def __init__(self):
        self.value = None
    
    def get_value(self):
        return self.value
    
    def click(self):
        self.value += 1

    def undo(self):
        self.value -= 1

        if self.value < 0:
            self.reset()

    def reset(self):
        self.value = 0
    
tally = Counter() #None
tally.reset() #0

tally.click()
tally.click()
tally.click()

total = tally.get_value()
print(total)#3

tally.undo()
tally.undo()
tally.undo()
tally.undo()

total = tally.get_value()
print(total) #0
