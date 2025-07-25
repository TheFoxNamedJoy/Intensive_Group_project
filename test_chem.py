chem_question1 = '\nНапишите кол-во электронов на внешнем слое у натрия.#1'
chem_question2 = '\nВыберите среди атомов галоген\n1)Сu\n2)F\n3)Na\n4)H#f'

chem_question3 = '\nНапишите правильный химический знак свинца.#pb'
chem_question4 = '\nВыберите молекулу с ковалентной полярной связью из списка:\n1)CuCl2\n2)HCl\n3)NaCl\n4)CaO#2'
chem_question5 = 'Какой тип кристаллической решетки у льда?\n1)Атомный\n2)Ионный\n3)Молекулярный\n4)Металлический#3'

def check_answer(q):
    parce = q.find('#')
    question = q[0:parce]
    right_a = q[parce+1]
    answer = input(question+'\nВведите ответ (только 1 правильный вариант):').lower()
    if right_a in answer:
        return 1
    else:
        return 0
def test_chemistry():
    score = 0
    print('\nТест по химии:')
    score += check_answer(chem_question1)
    score += check_answer(chem_question2)
    score += check_answer(chem_question3)
    score += check_answer(chem_question4)
    score += check_answer(chem_question5)
    print('Вы набрали', score, 'баллов из 5')
    if score == 0:
        print('\nВы провалили тест( Не быть вам химиком')
    elif score == 5:
        print('\nВашим знаниям позавидуют ученые! Поздравляем с успешным прохождением теста')
    else:
        print('\nВы немного разбираетесь, но сын маминой подруги знает химию лучше. Возвращайтесь, когда подготовитесь.')
