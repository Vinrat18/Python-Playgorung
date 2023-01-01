def make_multiplier(n):
    def multiple(x):
        return n * x
    
    return multiple

times3 = make_multiplier(3)
print(times3(2))
print(times3(3))
print(times3(4))
print(times3(5))
print(times3(6))