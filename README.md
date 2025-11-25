                        -----PROJETO DE ADOÇÃO-----
                                    grupo 4
                                    
INTEGRANTES:
Karollyne Santos Barbosa
Guilherme Lindemberg de Lima Beltrão                              
Pedro José Oliveira Silva
Luísa Feitosa Magalhães
Matheus Guerra Britto       
                              
--O projeto de adoção feito para a atividade complementar de notas da cadeira de FP é um programa 
elaborado em python que engloba diversas funcionalidades práticas que garantem o bem estar dos pets.

O QUE O PROJETO CONSEGUE FAZER?		   

-- O usuário pode cadastrar inúmeros animais e suas informações, além de editá-los, visualizá-los
ou removê-los quando necessário.

-- Também é possível registrar as atividades e os cuidados que serão realizados com o pet, bem como
a data de entrada no estabelecimento e a data de entrega, respectivamente. Além disso, o usuário
pode visualizar as tarefas e os cuidados atribuídos ao seu animal, assim como o tempo, em dias, que
falta para a data prevista ou quantos dias já se passaram.

-- A pessoa responsável pelo animal pode receber sugestões personalizadas de diferentes atividades
para realizar com seu pet, de acordo com as necessidades identificadas.

-- O usuário pode avaliar a sua compatibilidade com os animais cadastrados no programa
através do sistema match de adoção, que auxilia de maneira eficaz a escolha do pet ideal!

                          COMO USAR A FERRAMENTA?
 
-- Inicialmente, o programa possui 7 opções de input. Se a entrada solicitada pelo usuário não for nenhum
dos números abaixo o painel de opções irá aparecer novamente até um valor válido ser inserido.

                          (--MENU INICIAL--)

                          1. Adicionar Animal
                          2. Visualizar Animais
                          3. Editar Animal
                          4. Excluir Animal
                          5. Módulo de cuidados e atividades
                          6. Sugestões personalizadas
                          7. Sistema Match de Adoção
                          0. Sair e Salvar
                          Escolha uma opção (0-7):
PASSO 1
-- Ao inserir o "1" no terminal, será solicitado ao usuário a resposta de cada um dos quesitos abaixo respectivamente
(apenas se a resposta for válida).

                            -Espécie:
                            -Raça:
                            -Idade: (apenas números positivos e inteiros)
                            -Idade:
                            -Estado de Saúde: 
                            -Data de Chegada:

(Após informar corretamente cada uma das informações o animal será armazenado no banco de dados e o menu inicial será reapresentado)


PASSO 2
-- Ao inserir o "2" no terminal, será exibido ao usuário todos os animais cadastrados e suas respectivas informações, da seguinte forma:

                            --- Animal 1 ---
                            informações animal 1...
                            
                            --- Animal X ---
                            informações animal x...
                            
(Caso não haja animais cadastrados o programa irá informar e exibir o menu inicial)
(Após informar corretamente cada uma das informações o menu inicial será reapresentado)


PASSO 3
-- Ao inserir o "3" no terminal o programa irá solicitar qual número corresponde ao animal que o usuário deseja EDITAR.
Após informar o número correto o programa irá fazer os seguintes inputs em ordem:
(Se o número for inválido o programa irá informar e exibir o menu inicial)

(SE O USUÁRIO QUISER MANTER ALGUMA INFORMAÇÃO DEVE APENAS APERTAR ENTER!)

                            -Nome (NOME INICIAL):
                            -Espécie (ESPÉCIE INICIAL): 
                            -Raça (RAÇA INICIAL): 
                            -Idade (IDADE INICIAL): 
                            -Estado de Saúde (ESTADO INICIAL): 
                            -Data de Chegada (DATA INICIAL): 
                            --Comportamento (COMPORTAMENTO INICIAL):

(Caso não haja animais cadastrados o programa irá informar e reexibir o menu inicial)


PASSO 4 
-- Ao inserir o "4" no terminal o programa irá solicitar qual número corresponde ao animal que o usuário deseja EXCLUIR.
Após informar o número correto o programa perguntará se o usuário tem certeza dessa decisão com apenas duas alternativas(s/n)
(Após informar corretamente cada uma das informações o menu inicial será reapresentado)

                            "s" exclui.
                            "n" cancela a exclusão.

(Se o input for diferente do requisitado o programa irá cancelar a exclusão automaticamente)
(Caso não haja animais cadastrados o programa irá informar e exibir o menu inicial)


PASSO 5
-- Ao inserir o "5" no terminal o programa irá executar o seguinte:

                            ** MÓDULO DE CUIDADOS E ATIVIDADES **           
                            1. Cadastrar Cuidado                              
                            2. Visualizar Tarefas Pendentes
                            3. Sair do Módulo
                            Escolha uma opção:
PASSO 5.1
-- Ao escolher a opção "1" no MÓDULO DE CUIDADOS E ATIVIDADES o programa irá solicitar o... 



                            -Nome do animal:...
                            (se o nome digitado não for correspondente ao nome de um animal cadastrado o programa irá apresentar
                            erro e exibirá o menu do MÓDULO DE CUIDADOS E ATIVIDADES)
                            
                            -Descrição da tarefa/cuidado:...
                            
                            -Data prevista para a realização da tarefa/cuidado:...
                            
                            -Responsável por essa atividade:...



(Após informar os seguintes dados corretamente, as informações da tarefa/cuidado serão armazenadas no banco de dados e o menu de 
MÓDULO DE CUIDADO DE ATIVIDADES será exibido)                            

PASSO 5.2
-- Ao escolher a opção "2" no MÓDULO DE CUIDADOS E ATIVIDADES o programa irá socilitar o...

                            nome do animal o qual deseja visualizar as tarefas:
                            
-- Caso o nome digitado(e as suas atividades/cuidados) estiverem cadastrados o programa irá exibir qual a atividade, quem é responsável por ela
e quantos dias faltam ou já se passaram da data prevista para a sua realização .

(Se o nome digitado não estiver cadastrado o programa irá informar e retornar o menu de MÓDULO DE CUIDADOS E ATIVIDADES)
(Se o nome digitado estiver cadastrado mas NÃO tiver nenhuma atividade armazenada o programa também irá informar e retornar o menu do módulo)

PASSO 5.3
-- Ao escolher a opção "3" no MÓDULO DE CUIDADOS E ATIVIDADES o programa irá...

Apenas sair do módulo e irá reexibir o menu inicial



PASSO 6
-- Ao inserir o "6" no terminal quando o menu inicial estiver sendo exibido o programa irá solicitar...

                            Espécie: (INSERIR A ESPÉCIE DO ANIMAL)ex: cachorro, gato...
                            Estado de Saúde: (INSERIR ESTADO DO ANIMAL)ex: saudável, em tratamento...
                            Comportamento: (INSERIR COMPORTAMENTO DO ANIMAL)ex: dócil, arisco...
                            
-- Após inserir cada entrada acima CORRETAMENTE, o programa irá, com base nas respostas do usuário,
elaborar Sugestões de atividades para serem feitas com o pet,sugestões de cuidados especiais e sugestões de
adotantes.

O programa irá exibir:
                       
                            Sugestão de atividade:... 
                            Sugestão de cuidados especiais:...
                            Sugestão de adotantes:...
                            
(Após informar corretamente cada uma das informações o menu inicial será reapresentado)

PASSO 7
-- Por último mas não menos importante... o Match de adoção!

-- Ao inserir o "7" no terminal do menu inicial, será solicitado o nome do animal desejado para avaliar
a compatibilidade.

-- Uma vez que o nome já tenha sido cadastrado anteriormente, o programa fará uma série de perguntas.

                            Você mora em casa ou apartamento?...
                            
                            Você tem crianças pequenas em casa? (ex: sim ou nao)...
                            
                            Você já tem outros animais? (ex: sim ou nao)...
                            
                            Seu estilo de vida é calmo ou ativo?...

                            exemplo de output:
                            Compatibilidade entre você e cachorro salsicha: 40%
                            Baixa compatibilidade. Talvez outro animal combine melhor com você!

                            (retorna para o menu inicial!)
                                            
(Se as respostas não forem condizentes com as perguntas o programa irá continuar mas não vai comtabilizar pontos
para a porcentagem de compatibilidade!)

(caso o nome digitado não tiver sido cadastrado o programa irá informar e reexibir o menu inicial)

PASSO 8
-- Ao inserir o "0" no terminal do menu inicial o programa se ENCERRA! :)






