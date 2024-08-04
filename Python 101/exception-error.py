try:
    f = open("abc.txt")
except FileNotFoundError:
    print("File not found error")    
except Exception as e:
    print(e)
finally:
    print("Finally ")

n = 10
if n == 0:
    raise Exception("n can't be zero")
if type(n) is not int:
    raise Exception("n must be int!")

print(1/n)



