# print(list_quiz)
class quest():
    def __init__(self,mongo_server_link,database_name):                                                                   # collection에 연결하는 함수 
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                 # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                   # 데이터 베이스에 연결
        self.quiz_list = self.database["quiz_list"]                                                                       # collection "quiz_list"에 연결
        self.participate = self.database["participate"]                                                                   # collection "participate"에 연결
        self.participants_scoring = self.database["participants_scoring"]                                                 # collection "participants_scoring"에 연결
    
    def upload_quiz_list(self,list):                                                                                      # 입력된 quiz list를 collection "quiz_list"에 업로드
        self.quiz_list.delete_many({})
        self.quiz_list.insert_many(list)

    def find_quiz_list(self):                                                                                            # collection "quiz_list"에서 quetion,choice,answer,score 가져오기
        quiz = self.quiz_list.find({},{"question":1,"choice":1,"answer":1,"score":1})
        list_quiz = []
        for i in quiz:
            dic_quiz = {}
            dic_quiz["question"] = i["question"]
            pass
            dic_quiz["choice"] = i["choice"]
            pass
            dic_quiz["answer"] = i["answer"]
            dic_quiz["score"] = i["score"]
            list_quiz.append(dic_quiz)
        return list_quiz
    
    def upload_participate(self,list):                                                                                   # 참가자의 이름, 답변을 collection "participate"에 업로드
        self.participate.delete_many({})
        self.participate.insert_many(list)

    def find_participate(self):                                                                                          # collection "participate"에서 id, user_name, user_answer 가져오기
        participate = self.participate.find({},{"_id": 1,"user_name":1,"user_answer":1})
        list_participate = []
        for i in participate:
            dic_participate = {}
            dic_participate["user_id"] = i["_id"]
            dic_participate["user_name"] = i["user_name"]
            dic_participate["user_answer"] = i["user_answer"]
            list_participate.append(dic_participate)
        return list_participate
    
    def find_answer(self):                                                                                               # collection "quiz_list"에서 answer 가져오기
        answer = self.quiz_list.find({},{"answer":1})
        list_answer = []
        for i in answer:
            list_answer.append(i["answer"])
        return list_answer

    def find_scoring(self):                                                                                              # collection "quiz_list"에서 score 가져오기
        scoring = self.quiz_list.find({},{"score":1})
        list_scoring = []
        for i in scoring:
            list_scoring.append(i["score"])
        return list_scoring

    def scoring_upload(self,list,list_participate):                                                                        # 참가자의 id, 이름, 점수를 collection "participate_scoring"에 업로드
        list_sum = []
        for i in range(len(list)):
            dict_sum = {}
            dict_sum["user_id"] = list_participate[i]["user_id"]
            dict_sum["user_name"] = list_participate[i]["user_name"]
            dict_sum["user_sum"] = list[i]
            list_sum.append(dict_sum)
        self.participants_scoring.delete_many({})
        self.participants_scoring.insert_many(list_sum)

list_sum = [5,5,5,5]
if __name__ == "__main__":        
    quest_database = quest("mongodb://192.168.0.164:27017","toy_nosqls")
    quest_database.quiz_list
    quest_database.upload_quiz_list(list_quiz)
    list_quizs = quest_database.find_quiz_list()
    quest_database.upload_participate(list_user_answer)
    list_participate = quest_database.find_participate()
    print(quest_database.find_answer())
    print(quest_database.find_scoring())
    quest_database.scoring_upload(list_sum,list_participate)
    
