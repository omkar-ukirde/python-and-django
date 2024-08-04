a = input()
print(a)

while True:
    test = input("Enter IP Address: ")
    print(">> {}".format(test))
    if test == 'quit':
        break
    else:
        print("Exploiting ... {}".format(test))