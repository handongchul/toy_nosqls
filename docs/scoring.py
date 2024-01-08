def calculating(list_user_answer,list_quiz):
    list_sum = []
    for number in range(len(list_user_answer)) :  #------------------------------------------------------------------------------------list_quiz 내용만큼 숫자 받아 for구문 돌리기
        sum = 0
        for num_question in range(len(list_quiz)) :
            if list_quiz[num_question]["answer"] == list_user_answer[number]["user_answer"][num_question] :
                sum = sum + list_quiz[number]["score"]  #-------------------------------------------------------------------------------------------------한사람의 점수 합계구하기
                pass
            pass
        pass
        list_sum.append(sum) #-------------------------------------------------------------------------------------------------------list_sum에 위에서 받는 sum 값을 리스트로 배열
        pass
    return list_sum
def averazing(list_sum,list_user_answer):               
    total_score = 0
    for i in range(len(list_sum)):
        total_score = total_score + list_sum[i] #-------------------------------------------------------------------------------list_sum 내 값들을 순서대로 더해 점수 총합을 구하기
        pass
    pass
    average = total_score/len(list_user_answer)  #--------------------------------------------------------------------------------------total score를 user수 만큼 나눠 평균 구하기
    pass
    print("응시자별 채점결과:")
    for number in range(len(list_user_answer)) :
        print("{}:{}점".format(list_user_answer[number]["user_name"],list_sum[number])) #----------------------------list answer에 해당하는 순서의 참여자 이름과 참여자의 총점 구하기
    print("과목 평균 점수: {}".format(average))
    return  average



if __name__ == "__main__":
    apple = calculating(list_user_answer,list_quiz)
    averazing(apple,list_user_answer)
