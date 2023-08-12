fumante_animal = str
grupo5_oumais = str

fumante_animal = input("Você é fumante ou está com animal de estimação? Responda: Sim/Não ")
if (fumante_animal == "Sim"):
    print("Você será alocado na área externa!")
elif (fumante_animal == "Não"):
    grupo5_oumais = input("Você está em grupo de 5 ou mais? Responda: Sim/Não ")
    if (grupo5_oumais == "Sim"):
        print("Você será alocado no 1º andar!")
    else:
        print("Você será alocado no térreo!")

