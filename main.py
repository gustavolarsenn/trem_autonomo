import Trem

try:
    trem = Trem.Trem()

    trem.atual = str(input("Movimento: ESQUERDA, DIREITA ou SAIR\n")).upper()

    if (trem.atual != "ESQUERDA" and trem.atual != "DIREITA" and trem.atual != "SAIR"):
        print(f"Movimento inválido!: {trem.atual}\nEsperados: ESQUERDA, DIREITA ou SAIR")
        raise Exception("Movimento inválido!")
    while trem.atual != "SAIR":
        if (trem.atual != "ESQUERDA" and trem.atual != "DIREITA" and trem.atual != "SAIR"):
            print(f"Movimento inválido!: {trem.atual}\nEsperados: ESQUERDA, DIREITA ou SAIR")
            break
        if trem.maxRepetido():
            print("Número máximo de movimentos repetidos atingido: 20!")
            break
        if trem.maxMovido():
            print("Número máximo de movimentos atingido: 50!")
            break
        
        trem.salvarPosicao()

        if trem.atual == "ESQUERDA":
            trem.irEsquerda()
        elif trem.atual == "DIREITA":
            trem.irDireita()

        if trem.isRepetido():
            trem.repetidoAdd()
        else:
            trem.repetidoReset()

        trem.ultimo = trem.atual
        trem.movidoAdd()
        trem.atual = str(input("Movimento: ESQUERDA, DIREITA ou SAIR\n")).upper()

    trem.salvarPosicao()
    print("Posição final do trem:", trem.posicao)
    print("Posições percorridas:", trem.posicoes)
except Exception as e:
    print(f"Erro na execução: {e}")