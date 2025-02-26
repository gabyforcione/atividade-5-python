#Verificação de estado pelo cpf

def verificar_estado_cpf():
   
    cpf_input = input("Digite o número do CPF (com ou sem pontuação): ")

    
    cpf = ''.join(filter(str.isdigit, cpf_input))

    
    if len(cpf) != 11:
        print("CPF INVÁLIDO")
        return

    
    digito_estado = int(cpf[-2]) 

    
    estados = {
        0: "Distrito Federal",
        1: "São Paulo",
        2: "São Paulo",
        3: "Minas Gerais",
        4: "Rio de Janeiro",
        5: "Espírito Santo",
        6: "Bahia",
        7: "Sergipe",
        8: "São Paulo",
        9: "Paraná"
    }

    
    if digito_estado in estados:
        print(f"O CPF é do estado: {estados[digito_estado]}")
    else:
        print("Estado não identificado.")


verificar_estado_cpf()
