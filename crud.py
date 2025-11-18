animais = []

def mostrar_menu():
    
    print("\n--- Sistema de Gerenciamento de Animais ---")
    print("1. Adicionar Animal")
    print("2. Visualizar Animais")
    print("3. Editar Animal")
    print("4. Excluir Animal")
    print("0. Sair")
    return input("Escolha uma opção (0-4): ")

def adicionar_animal():
    print("\n--- Adicionar Novo Animal ---")
    
    
    nome = input("Nome: ")
    especie = input("Espécie (ex: Cachorro, Gato): ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    estado_saude = input("Estado de Saúde (ex: Saudável, Em tratamento): ")
    data_chegada = input("Data de Chegada (DD/MM/AAAA): ")
    comportamento = input("Comportamento (ex: Dócil, Arisco): ")
    
    
    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "estado_saude": estado_saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento
    }
    
    
    animais.append(animal)
    print(f"Animal '{nome}' adicionado com sucesso!")

def visualizar_animais():
    
    print("\n--- Lista de Animais Cadastrados ---")
    
    if not animais:
        print("Nenhum animal cadastrado no momento.")
        return

    
    for i, animal in enumerate(animais, start=1):
        print(f"\n--- Animal {i} ---")
        print(f"  Nome: {animal['nome']}")
        print(f"  Espécie: {animal['especie']}")
        print(f"  Raça: {animal['raca']}")
        print(f"  Idade: {animal['idade']}")
        print(f"  Estado de Saúde: {animal['estado_saude']}")
        print(f"  Data de Chegada: {animal['data_chegada']}")
        print(f"  Comportamento: {animal['comportamento']}")
        print("-" * 20)

def editar_animal():
    
    print("\n--- Editar Animal ---")
    visualizar_animais() 
    
    if not animais:
        return 

    try:
        
        indice_str = input("Digite o número do animal que deseja editar: ")
        indice = int(indice_str) - 1 

        if 0 <= indice < len(animais):
            animal = animais[indice]
            print(f"Editando '{animal['nome']}'. Pressione Enter para manter a informação atual.")

            novo_nome = input(f"Nome ({animal['nome']}): ")
            if novo_nome: animal['nome'] = novo_nome

            nova_especie = input(f"Espécie ({animal['especie']}): ")
            if nova_especie: animal['especie'] = nova_especie
            
            nova_raca = input(f"Raça ({animal['raca']}): ")
            if nova_raca: animal['raca'] = nova_raca
            
            nova_idade = input(f"Idade ({animal['idade']}): ")
            if nova_idade: animal['idade'] = nova_idade
            
            novo_estado = input(f"Estado de Saúde ({animal['estado_saude']}): ")
            if novo_estado: animal['estado_saude'] = novo_estado
            
            nova_data = input(f"Data de Chegada ({animal['data_chegada']}): ")
            if nova_data: animal['data_chegada'] = nova_data
            
            novo_comp = input(f"Comportamento ({animal['comportamento']}): ")
            if novo_comp: animal['comportamento'] = novo_comp
            
            print(f"Informações do animal '{animal['nome']}' atualizadas!")
        else:
            print("Número inválido. Nenhum animal com esse número.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def excluir_animal():
    print("\n--- Excluir Animal ---")
    visualizar_animais() 
    if not animais:
        return 

    try:
        
        indice_str = input("Digite o número do animal que deseja excluir: ")
        indice = int(indice_str) - 1 

        if 0 <= indice < len(animais):
            
            animal_removido = animais[indice]
            confirmacao = input(f"Tem certeza que deseja excluir '{animal_removido['nome']}' (s/n)? ").lower()
            
            if confirmacao == 's':
                animais.pop(indice)
                print(f"Animal '{animal_removido['nome']}' excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Número inválido. Nenhum animal com esse número.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            adicionar_animal()
        elif opcao == '2':
            visualizar_animais()
        elif opcao == '3':
            editar_animal()
        elif opcao == '4':
            excluir_animal()
        elif opcao == '0':
            with open("banco de dados dos animais.txt","w",encoding="utf-8") as f:
                dados = str(animais)
                dados_bonitos = dados.split("'")
                f.writelines(dados_bonitos)
            print("salvo com sucesso!")
            print("fim programa")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 0 a 4.")
if __name__ == "__main__":
    main()