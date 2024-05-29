import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def show_message(message):
    print(message)


def ask_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def show_wrong_message(correct_answer, your_answer):
    print(f'\'{your_answer}\' is wrong answer ;(. '
          f'Correct answer was \'{correct_answer}\'.')


def show_correct_message():
    print('Correct')


def show_lose_message(name):
    print(f'Let\'s try again, {name}!')


def show_win_message(name):
    print(f'Congratulations, {name}!')
