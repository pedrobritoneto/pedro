def eh_perfeito(n):
    if n == 0:
        return False
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val

    if soma == n:
        return True
    else:
        return False
