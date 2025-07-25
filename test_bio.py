bio_question1 = '\nХлоропласты - органоиды, характерные для клеток:\n1)животных\n2)животных и растений\n3)растений\n4)человека#3'
bio_question2 = '\nКакая эра является «Веком динозавров»?\n1)мезозойская\n2)протерозйская\n3)палеозойская\n4)кайнозойская#1'
bio_question3 = '\nГен - это:\n1)материал для эволюционных процессов\n2)участок молекулы ДНК\n3)мономер белковой молекулы\n4)орган половой системы#2'
bio_question4 = '\nКакие клетки участвуют в свертывании крови?#тромбоцит'

def check_answer(q):
    parce = q.find('#')
    question = q[0:parce]
    right_a = q[parce+1]
    answer = input(question+'\nВведите ответ (только 1 правильный вариант):').lower()
    if right_a in answer:
        return 1
    else:
        return 0
def test_biology():
    score = 0
    print('\nТест по биологии:')
    score += check_answer(bio_question1)
    score += check_answer(bio_question2)
    score += check_answer(bio_question3)
    score += check_answer(bio_question4)
    print('Вы набрали', score, 'баллов из 4')
    if score == 0:
        print('\nВы провалили тест( Не быть вам биологом')
    elif score == 4:
        print('\nВашим знаниям позавидуют ученые! Поздравляем с успешным прохождением теста')
    else:
        print('\nВы немного разбираетесь, но сын маминой подруги знает биологию лучше. Возвращайтесь, когда подготовитесь.')
    return score

