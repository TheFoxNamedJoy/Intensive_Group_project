import test_math, test_inform, test_geography

print('\nМы рады приветствовать вас в нашем приложении для проверки знаний по школьным предметам!\n')
user_name = input("Как вас зовут?\n")
user_points = 0

print('\n'+user_name+', по какому предмету вы хотите пройти тест?')
id_subj = input('1-Математика,\n2-Информатика,\n3-География,\n4-Физика,\n5-Химия,\n6-Биология,\n7-Русский язык,\n8-Литература,\n9-История,\n0-выход\n')

while id_subj != '0':

    if id_subj == '1':
        user_points += test_math.test_math()
    elif id_subj == '2':
        user_points += test_inform.test_inform()
    elif id_subj == '3':
        user_points += test_geography.test_geography()
    elif id_subj == '4':
        test_math.test_math()
    elif id_subj == '5':
        test_math.test_math()
    elif id_subj == '6':
        test_math.test_math()
    elif id_subj == '7':
        test_math.test_math()
    elif id_subj == '8':
        test_math.test_math()
    elif id_subj == '9':
        test_math.test_math()

    print('\n'+user_name+', еще тест?')
    id_subj = input('1-Математика,\n2-Информатика,\n3-География,\n4-Физика,\n5-Химия,\n6-Биология,\n7-Русский язык,\n8-Литература,\n9-История\n0-выход\n')

print('\nИмя:', user_name)
print('Количество набранных баллов по всем тестам:', user_points)
