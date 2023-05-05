print("Qual a Melhor Matéria? ")
usrqst0 = input("Digite sua Resposta: ")
print()

print("Cor dos PCs do laborátorio? ")
usrqst1 = input("Digite sua Resposta: ")
print()

print("Qual o Melhor Curos do CTISM? ")
usrqst2 = input("Digite sua Resposta: ")
print()

usrqst0 = usrqst0.upper()
usrqst1 = usrqst1.upper()
usrqst2 = usrqst2.upper()


rightansw = ('ALGORITMOS', 'PRETO', 'INFO')

quiz = {
'q0': '',
'q1': '',
'q2': ''
}


count = 0
if rightansw[0] == usrqst0:
    quiz['q0'] = 'Correto'
    print(quiz['q0'])
    count += 1

else:
    quiz['q0'] = 'Incorreto'
    print(quiz['q0'])


if rightansw[1] == usrqst1:
    quiz['q1'] = 'Correto'
    print(quiz['q1'])
    count += 1

else:
    quiz['q1'] = 'Incorreto'
    print(quiz['q1'])


if rightansw[2] == usrqst2:
    quiz['q2'] = 'Correto'
    print(quiz['q2'])
    count += 1

else:
    quiz['q2'] = 'Incorreto'
    print(quiz['q2'])

print(f'\n Acertos: {count} \n {quiz}')
