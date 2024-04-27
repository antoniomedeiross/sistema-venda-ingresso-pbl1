"""
Autor: Antonio Aparecido Medeiros Santana
Componente Curricular: Algoritmos I
Concluido em: 11/04/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# Definindo e configurando as variaveis 
# Primeiro o código vai perguntar se o usuário deseja configurar os valores da venda, como valor do ingresso, meia, etc...
print('########## CONFIGURAÇÕES DE VENDA ##########')
configura = input('Voce deseja configurar os valores de venda: [S]-Configurar [N]-Usar padrões: ').upper()
while configura != 'S' and configura != 'N': # Caso o usuário informe um valor inválido, entrará em um looping e só vai sair quando informar um valor válido
  configura = input('Voce deseja configurar os valores de venda: [S]-Configurar [N]-Usar padrões: ').upper()

if configura == 'S': # Caso ele escolha editar os valores ele entrará nessa condição 
  qIngressos = input('Informe a quantidade de ingresso para o evento: ')
  if not qIngressos.isnumeric():
    qIngressos = -1
  else:
    qIngressos = int(qIngressos)
  while qIngressos < 0: # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
    print('Quantidade de ingressos INVÁLIDA!')
    qIngressos = input('Informe a quantidade de ingressos corretamente: ')
    if not qIngressos.isnumeric():
      qIngressos = -1
    else:
      qIngressos = int(qIngressos)

  valorIngresso = input('Informe o valor do ingresso: ')
  if not valorIngresso.isnumeric():
    valorIngresso = -1
  else:
    valorIngresso = int(valorIngresso)
  while valorIngresso < 0: # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
    print('Valor do ingresso é INVÁLIDO!')
    valorIngresso = input('Informe a quantidade de ingressos corretamente: ')
    if not valorIngresso.isnumeric():
      valorIngresso = -1
    else:
      valorIngresso = int(valorIngresso)

  valorMeia = input('Informe o valor da meia-estudante: ')
  if not valorMeia.isnumeric():
    valorMeia = -1
  else:
    valorMeia = int(valorMeia)
  while valorMeia < 0: # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
    print('Valor da meia-estudante é INVÁLIDO!')
    valorMeia = input('Informe a quantidade de ingressos corretamente: ')
    if not valorMeia.isnumeric():
      valorMeia = -1
    else:
      valorMeia = int(valorMeia)

  valorMeiaOutros = input('Informe o valor da meia-outros-critérios: ')
  if not valorMeiaOutros.isnumeric():
    valorMeiaOutros = -1
  else:
    valorMeiaOutros = int(valorMeiaOutros)
  while valorMeiaOutros < 0: # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
    print('Valor da meia-outros é INVÁLIDO!')
    valorMeiaOutros = input('Informe a quantidade de ingressos corretamente: ')
    if not valorMeiaOutros.isnumeric():
      valorMeiaOutros = -1
    else:
      valorMeiaOutros = int(valorMeiaOutros)

  valorEcomp = input('Informe o valor do ingresso-Ecomp: ')
  if not valorEcomp.isnumeric():
    valorEcomp = -1
  else: 
    valorEcomp = int(valorEcomp)
  while valorEcomp < 0: # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
    print('Valor do ingresso-ecomp é INVÁLIDO!')
    valorEcomp = input('Informe a quantidade de ingressos corretamente: ')
    if not valorEcomp.isnumeric():
      valorEcomp = -1
    else:
      valorEcomp = int(valorEcomp)

else: # Caso o usuário escolha os valores padrão, entrará nessa condição que seta esses valores
  qIngressos = 2000
  valorIngresso = 30
  valorMeia = 15
  valorMeiaOutros = 15
  valorEcomp = 10

# Aqui estão sendo setadas algumas variáveis que serão utilizadas ao longo do código
ingressosEmitidos = 0
ingressosNaoEmitidos = 0
meiaEntradaEstudantes = 0
meiaEntradaOutrosCriterios = 0
inteiras = 0
ingressosEcomp = 0
ingressosDaEConvidados = 0
cortesiaVendedores = 0
ingressosVendidosBio = 0
ingressosVendidosEnf = 0
mediaIdadeCompradores = 0
idadeTotal = 0


# FUNÇÕES DO CÓDIGO ##########################

# funçao que verifica a quantidade de cortesias do DA
def corteisaDA(ingressosDaEConvidados, ingressosEmitidos, qIngressos, inteiras,  meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal):
  print('#####################################################################')
  print('---------- Corterias do Diretório Acadêmico ----------')
  ingressosDaEConvidados = input('Informe quantas cortesias foram solicitadas pelo D.A: ')
  while not ingressosDaEConvidados.isnumeric():
    ingressosDaEConvidados = input('Valor inválido! Informe quantas cortesias foram solicitadas pelo D.A: ')

  ingressosDaEConvidados = int(ingressosDaEConvidados)
  while ingressosDaEConvidados > qIngressos or ingressosDaEConvidados < 0:  # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido

    print('A QUANTIDADE DE CORTESIAS NÃO PODE SER MAIOR QUE A QUANTIDADE DE INGRESSOS OU MENOR QUE 0!')
    ingressosDaEConvidados = input('Informe quantas cortesias foram solicitadas pelo D.A CORRETAMENTE: ')
    while not ingressosDaEConvidados.isnumeric():
      ingressosDaEConvidados = input('Valor inválido! Informe quantas cortesias foram solicitadas pelo D.A: ')
    ingressosDaEConvidados = int(ingressosDaEConvidados)

  qIngressos -= ingressosDaEConvidados
  ingressosEmitidos += ingressosDaEConvidados
  print('############################################')
  print('Ingressos restantes: ', qIngressos)

  # CASO TUDO ESTEJA CORRETO A FUNÇÃO INICIAR VENDAS GERAIS É ACIONADA
  iniciarVendasGerais(ingressosDaEConvidados, qIngressos, ingressosEmitidos, inteiras,  meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal)


# função que inicia as vendas gerais
def iniciarVendasGerais(ingressosDaEConvidados, qIngressos, ingressosEmitidos, inteiras, meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal):
  for i in range(0, qIngressos): # Entra em um looping no range dos ingressos restantes, cada volta do loop será a venda de 1 ingresso
    print('###############################################')
    print(f'---------- VENDA NÚMERO [{i+1}]----------')
    print('---------- Identidade do comprador ----------')
    idade = input('Informe a Sua idade:')
    while not idade.isnumeric():
      idade = input('Informe uma idade válida: ')

    idade = int(idade)
    while idade < 0 or idade > 150:  # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
      print('VOÇÊ NÃO PODE SER MENOR QUE 1 ANO OU TER MAIS DE 150 ANOS!')
      idade = input('Informe sua idade corretamente: ')
      while not idade.isnumeric():
        idade = input('Informe sua idade corretamente: ')
      idade = int(idade)

    print('CATEGORIAS DE VENDA:')
    print('INTEIRA[1] | MEIA ESTUDANTE[2] | MEIA OUTROS CRITÉRIOS[3] | ESTUDANTE DE ECOMP[4]')
    categoria = input('Escolha uma categoria de ingresso acima: ')
    while not categoria.isnumeric():
      print('INTEIRA[1] | MEIA ESTUDANTE[2] | MEIA OUTROS CRITÉRIOS[3] | ESTUDANTE DE ECOMP[4]')
      categoria = input('Escolha uma categoria válida: ')

    categoria = int(categoria)
    if idade < 60 and categoria == 3: # Se um menor de 60 anos tentar comprar a meia-idoso, não irá conseguir
      print('Meia-idosos só é válida para maiores de 60 anos!')
      categoria = 0
    while categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4:  # Entrará em looping se o valor informado for irregular e so sairá quando tiver um valor válido
      print('CATEGORIA INVÁLIDA!!')
      print('INTEIRA[1] | MEIA ESTUDANTE[2] | MEIA OUTROS CRITÉRIOS[3] | ESTUDANTE DE ECOMP[4]')
      categoria = input('Escolha uma categoria de ingresso acima: ')
      while not categoria.isnumeric():
        print('INTEIRA[1] | MEIA ESTUDANTE[2] | MEIA OUTROS CRITÉRIOS[3] | ESTUDANTE DE ECOMP[4]')
        categoria = input('Escolha uma categoria válida: ')

      categoria = int(categoria)
      if idade < 60 and categoria == 3: # Se um menor de 60 anos tentar comprar a meia-idoso, não irá conseguir
        print('Meia-idosos só é válida para maiores de 60 anos!')
        categoria = 0

    # Abaixo fica a verificação do tipo de ingresso, e contabiliza os dados nas variáveis
    if categoria == 1: 
      inteiras += 1
      ingressosEmitidos += 1
      qIngressos -= 1
      print('Compra inteira realizada')
    elif categoria == 2:
      meiaEntradaEstudantes += 1
      ingressosEmitidos += 1
      qIngressos -= 1
      print('Compra meia-estudante realizada')
    elif categoria == 3:
      meiaEntradaOutrosCriterios += 1
      ingressosEmitidos += 1
      qIngressos -= 1
      print('Compra meia-outros realizada')
    elif categoria == 4:
      ingressosEcomp += 1
      ingressosEmitidos += 1
      qIngressos -= 1
      print('Compra ingresso-ecomp realizada')
    idadeTotal += idade # Caso a compra esteja dentro dos padrões, a idade do comprador é contabilizada
    # pergunta ao usuário se as vendas acabaram:
    fimVendas = input('DESEJA FINALIZAS VENDAS: [S] [N]?').upper()
    while fimVendas != 'S' and fimVendas != 'N': # enquanto o usuário não informa um valor entre S ou N ele não avançará
      print('ESCOLHA [S] OU [N]!')
      fimVendas = input('DESEJA FINALIZAS VENDAS: [S] [N]?').upper()
      print(fimVendas)
    if fimVendas == 'S': # se o usuário digitar S as vendas acabarão, caso contrario o loop continua ate o fim dos ingressos
      fimDasVendas(ingressosDaEConvidados, qIngressos, ingressosEmitidos, inteiras, meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal )
      break
    print('#################################################')
    print('Ingressos restantes: ', qIngressos)
  if qIngressos == 0:
    # Quando o código chegar aqui quer dizer que os ingressos acabaram, ele mostra uma mensagem e chama a função de fimDasVendas
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('OS INGRESSOS FORAM ESGOTADOS!!! UHULllllL')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    fimDasVendas(ingressosDaEConvidados, qIngressos, ingressosEmitidos, inteiras, meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal)

# a função fim das vendas recebe os valores atualizados e faz a listagem para o usuário
def fimDasVendas(ingressosDaEConvidados, qIngressos, ingressosEmitidos, inteiras, meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal):

  # Antes de mostrar os valores ao usuário são feitas algumas formatações e verificações finais
  valorArrecadado = (inteiras * valorIngresso) + (meiaEntradaEstudantes * valorMeia) + (meiaEntradaOutrosCriterios * valorMeiaOutros) + (ingressosEcomp * valorEcomp)
  arrecadacaoInteira = inteiras * valorIngresso
  arrecadacaoMeia = (meiaEntradaEstudantes + meiaEntradaOutrosCriterios) * valorMeiaOutros
  arrecadacaoEcomp = ingressosEcomp * valorEcomp
  if inteiras > meiaEntradaEstudantes and inteiras > meiaEntradaOutrosCriterios and inteiras > ingressosEcomp:
    tipoIngressoMaisVendido = 'INTEIRA'
  elif meiaEntradaEstudantes > inteiras and meiaEntradaEstudantes > meiaEntradaOutrosCriterios and meiaEntradaEstudantes > ingressosEcomp:
    tipoIngressoMaisVendido = 'MEIA-ESTUDANTE'
  elif meiaEntradaOutrosCriterios > inteiras and meiaEntradaOutrosCriterios > meiaEntradaEstudantes and meiaEntradaOutrosCriterios > ingressosEcomp:
    tipoIngressoMaisVendido = 'MEIA-OUTROS CRITÉRIOS'
  else: 
    tipoIngressoMaisVendido = 'INGRESSOS-ECOMP'
  if idadeTotal == 0:
    mediaIdade = 0
  else:
    mediaIdade =  idadeTotal / (ingressosEmitidos - ingressosDaEConvidados)

  # Por fim, os valores são printados para o usuário
  print('========== As vendas foram ENCERRADAS!!! ==========')
  print('__________ O resultado das vendas são: __________')
  print('Ingressos emitidos:-----------------------', ingressosEmitidos)
  print('Ingressos não emitidos:-------------------', qIngressos)
  print('Meia entrada estudantes:------------------', meiaEntradaEstudantes)
  print('Meia entrada outros critérios:------------', meiaEntradaOutrosCriterios)
  print('Quantidade de Inteiras:-------------------', inteiras)
  print('Ingressos comprados pelos alunos Ecomp:---', ingressosEcomp)
  print('Cortesias DA e convidados:----------------', ingressosDaEConvidados)
  print('Cortesias aos vendedores:-----------------', cortesiaVenda)
  print('Ingressos vendidos por Bio:---------------', ingressosVendidosBio)
  print('Ingressos vendidos por Enf:---------------', ingressosVendidosEnf)
  print(f'Valor total arrecadado:------------------- R$ {valorArrecadado:.2f}')
  print(f'Valor arrecadado inteira:----------------- R$ {arrecadacaoInteira:.2f}')
  print(f'Valor arrecadado meias:------------------- R$ {arrecadacaoMeia:.2f}')
  print(f'Valor arrecadado ingressos ecomp:--------- R$ {arrecadacaoEcomp:.2f}')
  print('Tipo de ingresso mais vendido:------------', tipoIngressoMaisVendido)
  print(f'Media de idade dos compradores:----------- {mediaIdade:.2f}')
#################################################################

# Depois das configurações o sistema está pronto para ser usado
print('##########################################################')
print('------------- Sistema de Venda de Ingressos -------------')

# PRIMEIRO VERIFICA A QUANTIDADE DE INGRESSOS VENDIDOS PELOS ALUNOS DE BIO E ENF, CASO HAJA ALGUM ERRO O USUÁRIO PODERÁ REPETIR OS DADOS
ingressosVendidosBio = input('Para começar, primeiro informe a quantidade de ingressos vendidos pelos alunos de Bio: ')
while not ingressosVendidosBio.isnumeric():
  ingressosVendidosBio = input('Informe um valor válido: ')
ingressosVendidosBio = int(ingressosVendidosBio)
ingressosVendidosEnf = input('Agora informe a quantidade de ingressos vendidos pelos alunos de Enf: ')
while not ingressosVendidosEnf.isnumeric():
  ingressosVendidosEnf = input('Informe um valor válido: ')
ingressosVendidosEnf = int(ingressosVendidosEnf)

while (ingressosVendidosBio + ingressosVendidosEnf > qIngressos) or (ingressosVendidosBio < 0) or (ingressosVendidosEnf < 0):
  print('VOCÊ NÃO PODE VENDER MAIS INGRESSOS QUE O DISPONIVEL OU MENOS QUE 0!')
  print('REPITA OS DADOS CORRETAMENTE!')
  ingressosVendidosBio = input('Para começar, primeiro informe a quantidade de ingressos vendidos pelos alunos de Bio: ')
  while not ingressosVendidosBio.isnumeric():
    ingressosVendidosBio = input('Informe um valor válido: ')

  ingressosVendidosBio = int(ingressosVendidosBio)
  ingressosVendidosEnf = input('Agora informe a quantidade de ingressos vendidos pelos alunos de Enf: ')
  while not ingressosVendidosEnf.isnumeric():
    ingressosVendidosEnf = input('Informe um valor válido: ')

  ingressosVendidosEnf = int(ingressosVendidosEnf)

cortesiaBio = ingressosVendidosBio // 10
cortesiaEnf = ingressosVendidosEnf // 10
cortesiaVenda = cortesiaBio + cortesiaEnf # contabiliza a quantidade de cortesias que serão dadas ao alunos de bio/enf
qIngressos -= ingressosVendidosBio + ingressosVendidosEnf + cortesiaVenda # retira os ingressos vendidos por bio/enf e as cortesias da quantidade de ingressos
ingressosEmitidos += ingressosVendidosBio + ingressosVendidosEnf + cortesiaVenda # Soma os ingressos vendidos por bio/enf e as cortesias da quantidade de ingressos emitidos

# Agora os vendedores de Bio deverão dar as informaçoes necessarias para concluir a venda dos seus ingressos
print('---------- Agora informe os dados de sua venda(BIO) ----------')
valorAPagarBio = 0 # valor que bio deve pagar inicia como 0
for i in range(0, ingressosVendidosBio): # um for é feito na quantidade de ingressos vendido por bio
  print(f'---------- Venda número[{i+1}]:')
  idade = input(f'Informe a idade do comprador[{i+1}]: ')
  while not idade.isnumeric():
    idade = input(f'Informe uma idade válida! Informe a idade do comprador[{i+1}]: ')

  idade = int(idade)
  while  idade < 1 or idade > 150: # enquanto a informação não for correta entrara em loop
    print('Idade deve estar entre 1 e 150')
    idade = input('Informe a Sua idade CORRETAMENTE: ')
    while not idade.isnumeric():
      idade = input(f'Informe uma idade válida! Informe a idade do comprador[{i+1}]: ')

    idade = int(idade)

  estudaEcomp = input(f'O comprador [{i+1}] é estudante de Ecomp [S] | [N]: ').upper()
  while estudaEcomp != 'S' and estudaEcomp != 'N': # enquanto a informação não for correta entrara em loop
    print('Escolha [S] ou [N]')
    estudaEcomp = input(f'O comprador [{i+1}] é estudante de Ecomp [S] | [N]: ').upper()

  estuda = input(f'O comprador [{i+1}] é estudante [S] | [N]: ').upper()
  while estuda != 'S' and estuda != 'N': # enquanto a informação não for correta entrara em loop
    print('Escolha [S] ou [N]')
    estuda = input(f'O comprador [{i+1}] é estudante [S] | [N]: ').upper()

  idadeTotal += idade
  # nesse bloco de if elif else, o tipo de ingresso é definido e contabilizado
  if estudaEcomp == 'S': 
    ingressosEcomp += 1
    valorAPagarBio += valorEcomp
    print('Compra Ingresso-Ecomp realizada!',   qIngressos, ingressosEcomp)
  elif estuda == 'S':
    meiaEntradaEstudantes += 1
    valorAPagarBio += valorMeia
    print('Compra Meia-Estudante realizada!',   qIngressos, meiaEntradaEstudantes)
  elif idade > 60:
    meiaEntradaOutrosCriterios += 1
    valorAPagarBio += valorMeiaOutros
    print('Compra Meia-Idade realizada!',   qIngressos, meiaEntradaOutrosCriterios)
  else:
    inteiras += 1
    print('Compra Inteira realizada!')
    valorAPagarBio += valorIngresso
  # Por fim, é feito o calculo de quanto bio deve pagar em dinheiro pelos ingressos que vendeu e é printado na tela
print(f'Bio deverá pagar R${valorAPagarBio} pela quantidade de ingressos que revendeu')
print(f'#####################################################################')

# Agora os vendedores de Enf deverão dar as informaçoes necessarias para concluir a venda dos seus ingressos
print('---------- Agora informe os dados de sua venda(ENF) ----------')
valorAPagarEnf = 0  # valor que enf deve pagar inicia como 0
for i in range(0, ingressosVendidosEnf):# um for é feito na quantidade de ingressos vendido por enf
  print(f'---------- Venda número[{i+1}]:')
  idade = input(f'Informe a idade do comprador[{i+1}]: ')
  while not idade.isnumeric():
    idade = input(f'Informe uma idade válida! Informe a idade do comprador[{i+1}]: ')
    
  idade = int(idade)
  while  idade < 1 or idade > 150: # enquanto a informação não for correta entrara em loop
    print('Idade deve estar entre 1 e 150')
    idade = int(input('Informe a Sua idade CORRETAMENTE: '))

  estudaEcomp = input(f'O comprador [{i+1}] é estudante de Ecomp [S] | [N]: ').upper()
  while estudaEcomp != 'S' and estudaEcomp != 'N': # enquanto a informação não for correta entrara em loop
    print('Escolha [S] ou [N]')
    estudaEcomp = input(f'O comprador [{i+1}] é estudante de Ecomp [S] | [N]: ').upper()

  estuda = input(f'O comprador [{i+1}] é estudante [S] | [N]: ').upper()
  while estuda != 'S' and estuda != 'N': # enquanto a informação não for correta entrara em loop
    print('Escolha [S] ou [N]')
    estuda = input(f'O comprador [{i+1}] é estudante [S] | [N]: ').upper()

  idadeTotal += idade
  
  # nesse bloco de if elif else, o tipo de ingresso é definido e contabilizado
  if estudaEcomp == 'S':
    ingressosEcomp += 1
    print('Compra Ingresso-Ecomp realizada!')
    valorAPagarEnf += valorEcomp
  elif estuda == 'S':
    meiaEntradaEstudantes += 1
    valorAPagarEnf += valorMeia
    print('Compra Meia-Estudante realizada!')
  elif idade > 60:
    meiaEntradaOutrosCriterios += 1
    valorAPagarEnf += valorMeiaOutros
    print('Compra Meia-Idade realizada!')
  else:
    inteiras += 1
    print('Compra Inteira realizada!')
    valorAPagarEnf += valorIngresso
# Por fim, é feito o calculo de quanto bio deve pagar em dinheiro pelos ingressos que vendeu e é printado na tela
print(f'Enf deverá pagar R${valorAPagarEnf} pela quantidade de ingressos revendidos')
print('###########################################################################')
  
#SE OS DADOS ESTIVEREM CORRETOS, A FUNÇÃO QUE VERIFICA AS CORTESIAS DO D.A SERÁ ACIONADA
print('Ingressos restantes: ', qIngressos) 
corteisaDA(ingressosDaEConvidados, ingressosEmitidos, qIngressos, inteiras,  meiaEntradaEstudantes, meiaEntradaOutrosCriterios, ingressosEcomp, cortesiaVenda, idadeTotal )
