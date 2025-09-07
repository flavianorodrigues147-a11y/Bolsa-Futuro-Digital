A=[] #criando a lista vazia
B=[]
#A=[1,2,3,4,5,6,7,8,9,10]
#B=[11,12,13,14,15,16,17,18,19,20]
for i in range(10): #para criar 2 listas a e b cada com 10 numeros inseridos
  num=int(input('um número inteiro:'))
  num2=int(input('um outro número inteiro:'))
  A.append(num)
  B.append(num2)
C=[] #lista completa
C=A.copy()
for i in range(len(B)):
  C.insert(i+i+1,B[i]) #lista.insert(posição,elemento)
print(C)

