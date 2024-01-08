
# 사용자의 답안을 기록하는 함수
def answermaking(list_quiz):  
    # 사용자의 답안을 저장할 리스트 초기화
    list_user_answer = []  

    while True:  # 무한 루프 시작
        # 각 사용자의 답안을 저장할 리스트 초기화
        list_answer = []  
        str_username = input("응시자의 이름을 입력하세요: ")  # 사용자 이름 입력
        
        # 문제 리스트의 길이만큼 반복
        for i in range(len(list_quiz)):  
            quizs = list_quiz[i]["question"]  # 문제를 추출
            print("문항{}: {}".format(i+1, quizs))  # 문제 번호와 문제 출력
            choices = list_quiz[i]["choice"]  # 선택지 추출
            print("선택지")  # "선택지" 출력
            for j in range(len(choices)):  # 선택지의 갯수만큼 반복
                print("{}. {}".format(j+1, choices[j]))  # 선택지 번호와 선택지 출력
            user_answer = input("답: ")  # 사용자 답안 입력
            list_answer.append(user_answer)  # 사용자 답안을 리스트에 추가
            print("--------------") 

        # 사용자의 이름과 답안을 저장할 딕셔너리 초기화    
        dic_user = {}  
        # 사용자 이름 딕셔너리에 저장
        dic_user['user_name'] = str_username  
        # 사용자 답안 딕셔너리에 저장
        dic_user['user_answer'] = list_answer  
        
        # 사용자 이름과 답안이 저장된 딕셔너리를 리스트에 추가
        list_user_answer.append(dic_user)  
        quit_input = input("다음 응시자가 있나요? (계속: c, 종료: x): ").lower()
        if quit_input == 'x':                  # 'x'를 입력하면
            print("프로그램이 종료되었습니다.")  # 종료 메시지 출력 후
            return list_user_answer            # 사용자 답안 리스트 반환
        elif quit_input == 'c':  # 'c'를 입력하면
            continue  # 다음 사용자를 위해 루프 계속

