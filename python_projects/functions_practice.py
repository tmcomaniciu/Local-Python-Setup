def hello():
    print("Hello!")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat my {list[0]}")
            else:
                print(f"Next I eat my {list[i]}")

hello()
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["pasta", "pad thai", "pizza"])