pergunta = input("qual é o melhor filme do shreK? ")
resposta_certa = str('Shrek 2')
pior_resposta = str('Shrek 4')

pergunta = pergunta.capitalize()

if pergunta == resposta_certa:
    print('Resposta certa!!!')
elif pergunta == pior_resposta:
    print('Você esta louco?')
elif    pergunta == 'Shrek 1' or pergunta == 'Shrek 3':
    print('resposta errada')
else: print('Voce digitou o nome do filme errado')