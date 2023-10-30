# from pprint import pprint

# for (key1,value1), (key2, value2) in zip(A.items(),B.items()):
#     # print(f"{key1=}, {value1=}, {key2=}, {value2=}")
#     if value1> value2:
#         Z[key1] = value1
#     elif value2 > value1:
#         Z[key1] = value2

Z = {}


def union(A, B):
    for x in A and B:
        Z[x] = max(A[x], B[x])
    return Z


def intersection(A, B):
    for x in A and B:
        Z[x] = min(A[x], B[x])
    return Z


def compliment(X):
    for x in X:
        Z[x] = round(1 - X[x],2)
    return Z


A = {}
B = {}

no_items = int(input("Enter the numbers: "))
for _ in range(no_items):
    key = input("Enter the crispy set elements: ")
    value = float(input("Enter the Membership value for Set 1: "))
    A[key] = value    
    value = float(input("Enter the Membership value for Set 2: "))
    B[key] = value


print(f"{A=} UNION {B=} Is {union(A,B)}")
print(f"{A=} Intersection {B=} Is {intersection(A,B)}")
print(f"COMPLIMENT OF {A=} IS {compliment(A)}")
print(f"COMPLIMENT OF {B=} IS {compliment(B)}")