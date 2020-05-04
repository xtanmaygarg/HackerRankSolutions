class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        Ans = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0 and n // i  == i:
                Ans += i
            elif n % i == 0:
                Ans += i
                Ans += n // i
            else:
                pass
        return Ans
            




n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
