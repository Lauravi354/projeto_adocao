import ast
import os
from datetime import datetime

animais=[]
sugestao_personalizada = []
ANIMALS_FILE = "banco de dados dos animais.txt"

def mostrar_menu():
    print("\n--- Sistema de Gerenciamento de Animais ---")
    print("1. Adicionar Animal")
    print("2. Visualizar Animais")
    print("3. Editar Animal")
    print("4. Excluir Animal")
    print("5. Módulo de cuidados e atividades")
    print("6. Sugestões personalizadas") 
    print("7. Sistema Match de Adoção")
    print("0. Sair e Salvar")
    return input("Escolha uma opção (0-7): ")

def dados_err(dado):
    if not dado:
        return True
    for char in dado:
        if char.isdigit():
            return True
    return False

def edit_dado(dado):
    if not dado:
        return False
    for char in dado:
        if char.isdigit():
            return True
    return False

def menu_animal():
    print("\n--- Adicionar Novo Animal ---")
    while True:
        nome = input("Nome: ").strip() 
        if dados_err(nome):
            print("Erro: O nome só pode conter letras e não pode ser vazio.")
        else:
            break 
            
    especie = input("Espécie (ex: Cachorro, Gato): ").strip()
    raca = input("Raça: ").strip()
    
    while True:
        idade = input("Idade (apenas números): ").strip()
        if idade.isdigit() and int(idade) >= 0:
            break
        else:
            print("Erro: A idade deve ser um número inteiro não negativo.")

    estado_saude = input("Estado de Saúde (ex: Saudável, Em tratamento): ").strip()
    data_chegada = input("Data de Chegada (DD/MM/AAAA): ").strip()
    comportamento = input("Comportamento (ex: Dócil, Arisco): ").strip()
    
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

def sugestoes():
    print("\n---Sugestões personalizadas---")
    animal = str(input("Espécie (ex: Cachorro, Gato): ")).strip().lower()
    cuidados_especiais = str(input("Estado de Saúde (ex: problema de pele, doença dentária ou saudável): ")).strip().lower()
    comportamento = str(input("Comportamento (ex: Dócil, Arisco): ")).strip().lower()

    if "cachorro" in animal:
        print("\nSugestão de atividade: caminhadas, corridas e passeios ao ar livre.")

    elif "gato" in animal:
        print("\nSugestão de atividade: Brincadeiras com varinhas, ratinhos de brinquedo, laser points.")
        
    if "problema de pele" in cuidados_especiais:
        print("Sugestão de cuidados especiais: Evitar banhos com produtos comuns, que podem irritar ainda mais a pele.")

    elif "doença dentária" in cuidados_especiais:
        print("Sugestão de cuidados especiais: oferecer brinquedos mastigáveis seguros específicos para limpeza dental ajudam a remover tártaro.")
    
    if "dócil" in comportamento:
        print("Sugestão de adotantes: Famílias com crianças, pessoas idosas, pessoas que buscam companhia e lares com outros animais.")

    elif "arisco" in comportamento:
        print("Sugestão de adotantes: lares tranquilos, sem outros animais, muito barulho ou mudanças frequentes, e com pessoas que possuam experiência com pets ariscos.")

def carregar_animais():
    if not os.path.exists(ANIMALS_FILE):
        return []
        
    try:
        with open(ANIMALS_FILE, "r", encoding="utf-8") as f:
            conteudo = "".join(f.readlines())
            return ast.literal_eval(conteudo.replace("\n", "").strip())
        
    except FileNotFoundError:
        print("Aviso: Arquivo de animais não encontrado. Começando com lista vazia.")
        return []
    
    except Exception as e:
        print(f"Aviso: Erro ao carregar dados do arquivo: {e}. Começando com lista vazia.")
        return []

animais = carregar_animais()
tarefas = []
def buscar_animal_por_nome(nome_animal):
    for animal in animais:
        if animal.get("nome", "").lower() == nome_animal.lower():
            return animal
    return None

def visualizar_animais():
    print("\n--- Lista de Animais Cadastrados ---")
    if not animais:
        print("Nenhum animal cadastrado no momento.")
        return

    for i, animal in enumerate(animais, start=1):
        print(f"\n--- Animal {i} ---")
        print(f" Nome: {animal['nome']}")
        print(f" Espécie: {animal['especie']}")
        print(f" Raça: {animal['raca']}")
        print(f" Idade: {animal['idade']}")
        print(f" Estado de Saúde: {animal['estado_saude']}")
        print(f" Data de Chegada: {animal['data_chegada']}")
        print(f" Comportamento: {animal['comportamento']}")
        print("-" * 20)
        
def cadastrar_cuidado():
    print("\n--- Cadastrar Cuidado/Atividade ---")
    nome_alvo = input("Nome do animal para registrar a tarefa: ")
    animal_encontrado = buscar_animal_por_nome(nome_alvo)

    if animal_encontrado is None:
        print("Erro: Animal não foi encontrado. Verifique o nome que você deseja.")
        return

    print(f"\nRegistrando tarefa para {animal_encontrado['nome']}") 
    descricao = input("Descrição da Tarefa: ")
    data = input("Data Prevista (DD/MM/AAAA): ")
    responsavel = input("Responsável pela Tarefa: ")
    nova_tarefa = {
        "animal_nome": animal_encontrado["nome"], 
        "descricao": descricao,
        "data_prevista": data,
        "responsavel": responsavel,
        "concluida": False 
    }
    
    tarefas.append(nova_tarefa)
    print(f"\nTarefa '{descricao}' registrada para {animal_encontrado['nome']}.")

def visualizar_tarefas():
    print("\n--- Visualizar Tarefas Pendentes ---")
    nome_alvo = input("Nome do animal para ver as tarefas: ")
    animal = buscar_animal_por_nome(nome_alvo) 
    
    if animal is None:
        print("Animal não encontrado.")
        return
    
    nome_alvo_normalizado = nome_alvo.lower()
    tarefas_pendentes = []

    for tarefa in tarefas:
        if tarefa["animal_nome"].lower() == nome_alvo_normalizado and not tarefa["concluida"]:
            tarefas_pendentes.append(tarefa)

    print(f"\n** Tarefas Pendentes para {animal['nome']} **")
    if not tarefas_pendentes:
        print(f"Nenhuma tarefa pendente para {animal['nome']}.")
        return

    for i, tarefa in enumerate(tarefas_pendentes, start=1):
        print(f" {i}. Tarefa: {tarefa['descricao']}")
        print(f" Previsto: {tarefa['data_prevista']}, Responsável: {tarefa['responsavel']}")
        
        alerta = contagem_regressiva_alertas(tarefa)
        print(" ", alerta)

def menu_cuidados():
    while True:
        print("\n** MÓDULO DE CUIDADOS E ATIVIDADES **")
        print("1. Cadastrar Cuidado")
        print("2. Visualizar Tarefas Pendentes")
        print("3. Sair do Módulo")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cuidado()
        elif opcao == '2':
            visualizar_tarefas()
        elif opcao == '3':
            print("Saindo do módulo de cuidados.")
            break
        else:
            print("Opção inválida.")

def editar_animal():
    
    print("\n--- Editar Animal ---")
    visualizar_animais() 
    
    if not animais:
        return print("não há dados de animais")

    try:
        
        indice_str = input("Digite o número do animal que deseja editar: ")
        indice = int(indice_str) - 1 

        if 0 <= indice < len(animais):
            animal = animais[indice]
            print(f"Editando '{animal['nome']}'. Pressione Enter para manter a informação atual.")
            while True:
                novo_nome = input(f"Nome ({animal['nome']}): ")
                if edit_dado(novo_nome):
                    print("Erro: O nome só pode conter letras.")
                else:
                    break 
            if novo_nome: animal['nome'] = novo_nome

            nova_especie = input(f"Espécie ({animal['especie']}): ")
            if nova_especie: animal['especie'] = nova_especie
            
            nova_raca = input(f"Raça ({animal['raca']}): ")
            if nova_raca: animal['raca'] = nova_raca
            while True:
                nova_idade = input(f"Idade ({animal['idade']}): ")
                if not nova_idade:
                    break
                if nova_idade.isdigit() and int(nova_idade) >= 0:
                    break
                else:
                    print("Erro: A idade deve ser um número inteiro não negativo.")
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

def contagem_regressiva_alertas (tarefa):
    hoje = datetime.now()
    
    try:
        data_prevista = datetime.strptime(tarefa['data_prevista'], "%d/%m/%Y")
    except:
        return "Data inválida para calcular a atividade."

    dias_faltando = (data_prevista - hoje).days

    if dias_faltando > 0:
        return f"Dias para a próxima atividade : {dias_faltando} dia(s)"
    elif dias_faltando == 0:
        return f"A atividade é hoje!"
    else:
        return f"A data da atividade já passou ({dias_faltando} dias)!"
        
def main():
    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            menu_animal()
        elif opcao == '2':
            visualizar_animais()
        elif opcao == '3':
            editar_animal()
        elif opcao == '4':
            excluir_animal()    
        elif opcao == '5':
            menu_cuidados()
        elif opcao == '6':
            sugestoes()
        elif opcao == '7':
            match_adocao(animais)
        elif opcao == '0':
            with open(ANIMALS_FILE,"w",encoding="utf8") as file:
                for animal in animais:
                    file.writelines(
                        f"nome: {animal['nome']} \n"
                        f"especie: {animal['especie']}\n"
                        f"raca: {animal['raca']}\n"
                        f"idade: {animal['idade']}\n"
                        f"estado_saude: {animal['estado_saude']}\n"
                        f"data_chegada: {animal['data_chegada']}\n"
                        f"comportamento: {animal['comportamento']}\n"
                        "\n"
                    )
                file.write("TAREFAS E CUIDADOS: \n")
                if not tarefas:
                    file.write("nenhuma tarefa registrada")
                else:
                    for tarefa in tarefas:
                        file.writelines(
                            f"animal_nome: {tarefa['animal_nome']}\n"
                            f"descricao: {tarefa['descricao']}\n"
                            f"data_prevista: {tarefa['data_prevista']}\n"
                            f"responsavel: {tarefa['responsavel']}\n"
                        )
            print("fim programa")
            break
                
        else:
            print("Opção inválida. Por favor, escolha uma opção de 0 a 7.")

def match_adocao(animais):
    print("\n--- SISTEMA DE MATCH DE ADOÇÃO ---")

    if not animais:
        print("Nenhum animal cadastrado para realizar o match.")
        return

    nome = input("Digite o nome do animal que deseja avaliar: ").strip()
    animal = buscar_animal_por_nome(nome)

    if animal is None:
        print("Animal não encontrado.")
        return

    print(f"\nAnalisando compatibilidade para o animal: {animal['nome']}")

    moradia = input("Você mora em casa ou apartamento? \n").strip().lower()
    criancas = input("Você tem crianças pequenas em casa? (ex: sim ou nao) \n").strip().lower()
    outros_pets = input("Você já tem outros animais? (ex: sim ou nao) \n").strip().lower()
    estilo = input("Seu estilo de vida é calmo ou ativo? \n").strip().lower()

    pontos = 0

    comportamento = animal["comportamento"].strip().lower()
    if comportamento == "dócil" or comportamento == "docil" and criancas == "sim":
        pontos += 40
    if comportamento == "dócil" or comportamento == "docil" and criancas == "nao":
        pontos += 30
    if comportamento == "agitado" and estilo == "ativo":
        pontos += 35
    if comportamento == "agitado" and estilo == "calmo":
        pontos += 20
    if comportamento == "arisco" and criancas == "nao" and outros_pets == "nao":
        pontos += 40
    if comportamento == "arisco" and criancas == "sim" and outros_pets == "nao":
        pontos += 10

    especie = animal["especie"].strip().lower()
    if especie == "cachorro" and moradia == "casa":
        pontos += 30
    if especie == "cachorro" and moradia == "apartamento":
        pontos += 20
    if especie == "gato" and moradia == "casa":
        pontos += 30
    if especie == "gato" and moradia == "apartamento":
        pontos += 20

    pontos += 15

    if pontos > 100:
        pontos = 100

    print("\n---RESULTADO DO MATCH---")
    print(f"Compatibilidade entre você e {animal['nome']}: {pontos}%")

    if pontos >= 80:
        print("Alta compatibilidade! Excelente opção de adoção!")
    elif pontos >= 50:
        print("Compatibilidade moderada. Pode ser uma boa opção!")
    else:
        print("Baixa compatibilidade. Talvez outro animal combine melhor com você!")


main()
    