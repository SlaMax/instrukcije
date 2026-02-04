def decimal_u_hexadecimal(n):
    if n == 0:
        print("0")
        return
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    
    while n > 0:
        ostatak = n % 16
        hexadecimal = hex_digits[ostatak] + hexadecimal
        n = n // 16
    
    print("Heksadecimal:", hexadecimal)



def decimal_u_octal(n):
    if n == 0:
        print("0")
        return
    
    octal = ""
    while n > 0:
        ostatak = n % 8
        octal = str(ostatak) + octal  
        n = n // 8
    
    print("Oktalni:", octal)

def decimal_u_binarni(n):
    if n == 0:
        print("0")
        return
    
    binarni = ""
    while n > 0:
        ostatak = n % 2
        binarni = str(ostatak) + binarni  
        n = n // 2
    
    print("Binarni:", binarni)

decimal_u_binarni(5)  


def binarni_u_decimal(n):
    binarni_str = str(n)
    decimalni = 0
    snaga = 0
    
    for i in reversed(binarni_str):
        decimalni += int(i) * (2 ** snaga)
        snaga += 1
    
    print("Decimalni:", decimalni)
