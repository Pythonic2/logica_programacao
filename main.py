# numero_int = 1
# numero_flot = 1.8
# nome_str = 'Arara'
# var_lista = ['nome',12,1.0]
#
# ##### como imprimir ######
#
# # print(numero_int + numero_flot)
# # print(numero_int, numero_flot, nome_str)
# #print(f'um temxo quaquer: {var_lista}\nNome:{nome_str}\nNumero: {numero_flot}')
#
#
# ######## funções de string ######
# # print(nome_str.find('%'))# o find retorna a primeira ocorrencia da letra solicitada ou conjunto
# # print(nome_str.index('c')) # diferença no retorno, se não achar o caractere pedido, ele retonra erro, o find retorna -1
# # pla = input('Digite uma Plavra: ')
# # transformar_string = pla.lower()
# #
# # if transformar_string == transformar_string[::-1]:
# #     print('oi')
# # else:
# #     print('falhou')
#
#
# ########### dados do usuario ############
#
# # nome = input('Escreva seu nome: ')
# #
# # print(f'Olá, {nome}')
#
# # numero = float(input('digite um numero: '))
# # soma = numero + 10
# # print(f'A soma desse numero mais 10 = {soma}')
#
# # class Dinheiro:
# #     def __init__(self, valor):
# #         self.valor = valor
# #
# #     def __float__(self):
# #         return float(self.valor)
# #
# #     def soma(self):
# #         return self.valor +2
# # d = Dinheiro(10.5)
# # print(d.valor)
# # print(d.soma())
#
# class EntrarBd:
#
#     def cadastrar(self,nome: str, idade:int) -> None:
#         if self.__verificar_dados(nome, idade):
#             self.__armazenar_usuario()
#         else:
#             self.__apresentar_erro()
#
#     def __verificar_dados(self, nome: str, idade:int) -> bool:
#         if isinstance(nome, str) and isinstance(idade, int):
#             return True
#         else:
#             return False
#     def __armazenar_usuario(self) ->None:
#         print('entrando e ar,azemamdp')
#
#     def __apresentar_erro(self)->None:
#         print('dados invalidos')
#
# em = EntrarBd()
# em.cadastrar('igor',5.6)

a = '3'
b = '2'
print(a is b)