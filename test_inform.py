inform_questions = ['\nПереведите двоичное число 1100111 в десятичную систему счисления.\n1 - 104\n2 - 206\n3 - 103$s#3',
                  '\nНапишите наибольшее натуральное число x, для которого ИСТИННО высказывание "НЕ (x < 5) И (x < 6)"$t#5',
                  '\nДоступ к файлу hello.jpg, находящемуся на сервере home.info, осуществляется по протоколу ftp. Фрагменты адреса файла закодированы буквами от А до Ж. Запишите последовательность этих букв, кодирующую адрес указанного файла в сети Интернет.\nА) info\nБ) ://\nВ) home.\nГ) /\nД) hello\nЕ) ftp \nЖ) .jpg $t#ебвагдж'
                  ]

def test_inform():
    print("\nТЕСТИРОВАНИЕ ПО ИНФОРМАТИКЕ")
    input('Нажмите ENTER, чтобы начать.')
    score = 0
    for question in inform_questions:
        score += check_answer(question)
    print('\nВы набрали', score,'баллов из',len(inform_questions),'возможных.')
    return score


def check_answer(question):
    q_len = question.find('$')
    q_type = question[q_len+1]
    right_ans = question[question.find('#')+1:]
    print(question[0:q_len])
    answer = input('\nВаш ответ: ').lower()

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
