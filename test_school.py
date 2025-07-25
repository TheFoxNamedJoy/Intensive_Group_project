import questions_school

def test_school(question):
    length_question = len(question)
    scores = 0
    while length_question>2:
        splitter = question.find('&')
        splitter_end = question.find('%')
        displayed_question = question[0:splitter]
        if question[splitter+1]=='#':
            right_answer = question[splitter+2]
            answer = input(displayed_question)
            if answer==right_answer:
                scores +=1
        else:
            right_answer = question[splitter+2:splitter_end]
            answer = input(displayed_question).lower()
            if right_answer.find(answer)!=-1:
                scores +=2
        question = question[splitter_end+1:len(question)]
        length_question = len(question)
    return scores

def normal_school(score, question):
    length_question = len(question)
    scores = 0
    while length_question>2:
        splitter = question.find('&')
        splitter_end = question.find('%')
        displayed_question = question[0:splitter]
        if question[splitter+1]=='#':
            scores +=1
        else:
            scores +=2
        question = question[splitter_end+1:len(question)]
        length_question = len(question)
    return scores
