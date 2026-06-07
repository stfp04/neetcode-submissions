class MyCalendar:
    
    def __init__(self):
        self.start = self.end = None
        self.left = self.right = None
        
    def book(self, startTime: int, endTime: int) -> bool:

        if not (self.start or self.end):
            self.start = startTime
            self.end = endTime
            return True
        
        if startTime >= self.end:
            if self.right:
                return self.right.book(startTime, endTime)
            self.right = MyCalendar()
            self.right.start = startTime
            self.right.end = endTime
        elif endTime <= self.start:
            if self.left:
                return self.left.book(startTime, endTime)
            self.left = MyCalendar()
            self.left.start = startTime
            self.left.end = endTime
        else:
            return False

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)