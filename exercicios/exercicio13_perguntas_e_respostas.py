# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def introduction():
    print(10*'-' + ' Welcome to the Quiz! ' + 10*'-')

def questions():
    for pergunta in perguntas:
        print(pergunta['Pergunta'])

        for i, option in enumerate(pergunta['Opções']):
            print(f"{i + 1}) {option}")

        while True:
            answer = input('Type the number of your answer: ')
            if answer.isdigit() and 1 <= int(answer) <= len(pergunta['Opções']):
                    selected_option = pergunta['Opções'][int(answer) - 1]
                    if selected_option == pergunta['Resposta']:
                        print('Correct!')
                        score += 1
                    else:
                        print('Wrong!')
                    break    
            else:
                print('Invalid input. Please enter a number corresponding to the options.')

def main():
    introduction()
    
    questions()
    score = 0
    print(f'Your final score is: {score}/{len(perguntas)}')

main()
