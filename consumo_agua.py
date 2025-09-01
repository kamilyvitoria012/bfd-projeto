#Entrada de dados 
def sistema_de_agua():
    nome = input("Digite seu nome:")
    peso = float(input("Digite seu peso:"))
    altura = float(input("Digite sua altura:"))
    whatsapp = (input("Digite seu número de whatsapp:"))

#Processamento
    agua_ml = peso *35
    agua_l =agua_ml / 1000

#Saída de dados 
    print(f"Seu nome é: {nome}")
    print(f"Seu peso é: {peso} Kg")
    print(f"Sua altura é: {altura} m")
    print(f"Seu número de WhatsApp é: {whatsapp}")
    print(f"Você deve beber: {agua_l:.2f} litros de água por dia")


#Menu Principal
while True:
        print ("\n -------------- Sistema de consumo de água-------- ----------")
        print (" Digite 1 para calcular seu consumo de água ")
        print (" Digite 2 para sair do sistema")
        opcao = input ("Escolha uma opção:")
        
        if opcao == "1":
             sistema_de_agua()
        elif opcao == "2":
            print ("Programa finalizado com sucesso!")
            break
        else:
          print("Opção inválida, tente novamente!")
