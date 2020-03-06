def soma_ab (a, b):
    somar = a + b
    return somar


try:
    a = int(170)
    b = int(20)
    c = soma_ab(a, b)
    assert c == 30
    print ("Soma correta")
    print (c)
except AssertionError:
    print ('Deu erro')