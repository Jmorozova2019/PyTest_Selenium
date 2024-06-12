import datetime

class CalcFib():
    @staticmethod
    def getCurrentDayPlusOne():
        dt = datetime.datetime.now()
        return int(dt.day) + 1

    @staticmethod
    def getFibonacciNumber():
        n = CalcFib.getCurrentDayPlusOne()

        prev = 0
        current = 1
        for i in range(2, n):
            next = prev + current
            prev = current
            current = next
        return current