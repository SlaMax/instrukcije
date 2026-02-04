
def countEven(arr):
    x= 0
    for i in arr:
        if i%2==0:
            x+=1
    return x


def faktorijel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorijel(n - 1)
    

def findMax(arr):
    if len(arr) == 0:
        return None
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value


def zamijeni_neparne(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = 0
    print("Nova lista:", arr)

def broj_samoglasnika(rijec):
    samoglasnici = "aeiouAEIOU"
    brojac = 0
    for slovo in rijec:
        if slovo in samoglasnici:
            brojac += 1
    print("Samoglasnika:", brojac)

def prva_rijec(s):
    rijec = ""
    i = 0
    while i < len(s):
        if s[i] == " ":
            break
        rijec += s[i]
        i += 1
    print("Prva riječ:", rijec)

