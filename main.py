import test_math, test_inform, test_geography, questions_school, test_school,test_bio, test_chem, physics

print('\nМы рады приветствовать вас в нашем приложении для проверки знаний по школьным предметам!\n')
user_name = input("Как вас зовут?\n")
user_points = 0

print('\n'+user_name+', по какому предмету вы хотите пройти тест?')
id_subj = input('1-Математика,\n2-Информатика,\n3-География,\n4-Физика,\n5-Химия,\n6-Биология,\n7-Русский язык,\n8-Литература,\n9-Английский язык,\n0-выход\n')

while id_subj != '0':

    if id_subj == '1':
        user_points += test_math.test_math()
    elif id_subj == '2':
        user_points += test_inform.test_inform()
    elif id_subj == '3':
        user_points += test_geography.test_geography()
    elif id_subj == '4':
        user_points +=physics.test_physics()
    elif id_subj == '5':
        user_points +=test_chem.test_chemistry()
    elif id_subj == '6':
        user_points +=test_bio.test_biology()
    elif id_subj == '7':
        local_points = test_school.test_school(questions_school.questions_russian)
        normal_points = test_school.normal_school(local_points, questions_school.questions_russian)
        print(f'\nТы набрал {local_points} баллов из {normal_points}')
        if local_points/normal_points*100>=80:
            print('Поздравляю, ты успешно прошел тестирование.\n')
        else:
            print('Нужно подтянуть знания. Возвращайся после повторения материала.\n')
        user_points+=local_points
    elif id_subj == '8':
        local_points = test_school.test_school(questions_school.questions_literature)
        normal_points = test_school.normal_school(local_points, questions_school.questions_literature)
        print(f'\nТы набрал {local_points} баллов из {normal_points}')
        if local_points/normal_points*100>=80:
            print('Поздравляю, ты успешно прошел тестирование.\n')
        else:
            print('Нужно подтянуть знания. Возвращайся после повторения материала.\n')
        user_points+=local_points
    elif id_subj == '9':
        local_points = test_school.test_school(questions_school.questions_english)
        normal_points = test_school.normal_school(local_points, questions_school.questions_english)
        print(f'\nТы набрал {local_points} баллов из {normal_points}')
        if local_points/normal_points*100>=80:
            print('Поздравляю, ты успешно прошел тестирование.\n')
        else:
            print('Нужно подтянуть знания. Возвращайся после повторения материала.\n')
        user_points+=local_points

    print('\n'+user_name+', еще тест?')
    id_subj = input('1-Математика,\n2-Информатика,\n3-География,\n4-Физика,\n5-Химия,\n6-Биология,\n7-Русский язык,\n8-Литература,\n9-Английский язык\n0-выход\n')

print('\nИмя:', user_name)
print('Количество набранных баллов по всем тестам:', user_points)
