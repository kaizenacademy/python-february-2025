limit=int(input("Enter the number: "))

first=0
second=1
print(first)
print(second)
next = first + second

while next < limit:
    print(next)
    first=second
    second=next
    next=first+second

# 0 1 1 2 3 5

# first= 0
# second= 1
# next = 1


# first=1
# second=1
# next=2

# first=1
# second=2
# next=3

# first=2
# second=3
# next=5
