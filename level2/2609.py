def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    
    return a

def lcm(a, b):
    return int((a*b) / gcd(a, b))

a, b = map(int, input().split())
mini = gcd(a, b)
maxi = lcm(a, b)
print(mini)
print(maxi)
