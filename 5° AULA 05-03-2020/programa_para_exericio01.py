import exercio01


try:
    fahrenheit = int(60)
    temperatura_convertida = exercio01.converte_para_celsius(fahrenheit)
    assert temperatura_convertida == 15.555555555555557
    print('Deu super certo essa bagaça de conversão de temperatura')
    print("%.2f" % temperatura_convertida)
except AssertionError:
    print("Deu errado essa parada")


try:
    celsius = int(40)
    temperatura_convertida = exercio01.converte_para_fahrenheit(celsius)
    assert temperatura_convertida == 104.00
    print('Deu super certo essa bagaça de conversão de temperatura')
except AssertionError:
    print("Deu errado essa parada")
