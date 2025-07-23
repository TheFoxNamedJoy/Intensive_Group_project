geography_questions = ['\nПусть две параллельные прямые пересечены третьей. Какие углы не будут равны?\n1 - накрестлежащие\n2 - внутренние односторонние\n3 - соответственные$s#2',
                  '\nЦентральный угол окружности опирается на дугу 78 градусов. Чему равна градусная мера вписанного угла, опирающегося на ту же дугу?$t#39'
                  ]

def test_geography():
    print("\nТЕСТИРОВАНИЕ ПО ГЕОГРАФИИ")
    input('Нажмите ENTER, чтобы начать.')
    score = 0
    for question in geography_questions:
        score += check_answer(question)
    print('Вы набрали', score,'баллов из',len(geography_questions),'возможных.')
    return score


def check_answer(question):
    q_len = question.find('$')
    q_type = question[q_len+1]
    right_ans = question[question.find('#')+1:]
    print(question[0:q_len])
    answer = input('\nВаш ответ: ')

    if q_type =='s':
        if answer == right_ans:
            return(1)
        else:
            return(0)
    
    elif q_type =='t':
        right_ans = right_ans.split('/')
        if answer in right_ans:
            return(1)
        else:
            return(0)            

