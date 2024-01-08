import quizlist, database, participate,scoring

quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")            # "toy_nosqlis"에 접속
pass
list_quiz=quizlist.quizmaking()                                                          # 입력 받은 list를 list_quiz로 지정  
pass
quest_database.upload_quiz_list(list_quiz)                                               # collection "quiz_list"에 list_quiz 업로드
pass
list_quiz = quest_database.find_quiz_list()                                              # collection "quiz_list"에서 list_quiz를 추출
pass
list_user_answer = participate.answermaking(list_quiz)                                   # 참여자의 이름과 답안지를 입력받아 list_user_answer 작성
pass
quest_database.upload_participate(list_user_answer)                                      # collection "participate"에 list_user_answer 업로드              
pass
list_participate = quest_database.find_participate()                                     # collection "participate"에서 id, user_name, user_answer 가져오기
pass
list_sum = scoring.calculating(list_user_answer,list_quiz)                               # 참여자의 점수를 list_sum에 작성
pass
scoring.averazing(list_sum,list_user_answer)                                             # 참여자의 점수와 과목 평균 출력
pass
quest_database.scoring_upload(list_sum,list_participate)                                 # 참여자의 id, user_name, 점수를 collection "participate_socoring"에 업로드