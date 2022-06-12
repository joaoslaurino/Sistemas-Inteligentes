import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#Variaveis
#Idade do imovel, área, distancia do centro, valor_condominioo do condominio

idade_do_imovelInput = 0
areaInput = 0
distancia_centroInput = 0
#valor_condominio = 0

#Definindo as variaveis de entrada e saida do sistema fuzzy
idade_do_imovel = ctrl.Antecedent(np.arange(0, 80, 1), 'idade_do_imovel')
area =  ctrl.Antecedent(np.arange(12, 200, 1), 'area')
distancia_centro = ctrl.Antecedent(np.arange(0, 20, 1), 'distancia_centro')
valor = ctrl.Consequent(np.arange(25000, 500000, 2500), 'valor')

#Popula as variaveis com as funções de membership
idade_do_imovel.automf(3, 'idade_do_imovel', ['low', 'mid', 'high'])
area.automf(3, 'area', ['low', 'mid', 'high'])
distancia_centro.automf(3, 'distancia_centro', ['low', 'mid', 'high'])
valor.automf(3, 'valor', ['low', 'mid', 'high'])

#Definindo as variaveis de entrada do usuario
while True:
    idade_do_imovelInput = int(input('Digite um valor entre 0 e 80 para a idade do imovel: '))
    if idade_do_imovelInput < 0 or idade_do_imovelInput > 80:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break

while True:
    areaInput = int(input('Digite um valor entre 12 e 200 para a area do imovel: '))
    if areaInput < 12 or areaInput > 200:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break

while True:
    distancia_centroInput = int(input('Digite um valor entre 2 e 20 para a distancia do centro: '))
    if distancia_centroInput < 2 or distancia_centroInput > 20:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break


#Regras
rules = []
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['low'], valor['high']))


valorCtrl = ctrl.ControlSystem(rules)
valorTotal = ctrl.ControlSystemSimulation(valorCtrl)


valorTotal.input['idade_do_imovel'] = idade_do_imovelInput
valorTotal.input['area'] = areaInput
valorTotal.input['distancia_centro'] = distancia_centroInput

valorTotal.compute()

def PrintValor(val):
    print('\nValor do imovel: R$', val, '\n')

PrintValor(valorTotal.output['valor'])
valor.view(sim=valorTotal)
plt.show()