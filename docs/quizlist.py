def quizmaking():
    list_quiz = [] # 리스트화
    question_type = int(input("문제 유형을 입력하세요. 숫자만 입력하세요."))  # 문제생성1
    num_questions = int(input("문항 수를 입력하세요."))                     # 문제생성2
    print("문제와 선택지를 입력하세요.")
    for quiz in range(num_questions):        # 문항 수 만큼 
        dict_quizlist = {}                   # 딕셔너리화
        dict_quizlist["question"] = input("문항 : ")     # question, choice, answer, score 받기
        dict_quizlist["choice"] = []
        for choice in range(question_type) : 
            dict_quizlist["choice"].append(input("보기 : "))
        dict_quizlist["answer"] = input("정답 : ")
        dict_quizlist["score"] = int(input("배점 : "))
        list_quiz.append(dict_quizlist)                  
    return list_quiz

