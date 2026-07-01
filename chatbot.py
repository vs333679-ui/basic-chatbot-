print("--.✦ ݁˖WELCOME TO THE CHATBOT.✦ ݁˖T---")
def get_username():
    return input("-👀 MAY I ASK YOUR NAME-👀:")
name=get_username()
print("nice to meet you ",name)

def ask_question():
    while True:
       question=input("HOW ARE YOU TODAY.💬:")
       
       
       if question.lower()=="done":
        print("goodbye..👋",name,"have a nice day")
        break
    
       elif question.lower()=="fine":
         print("💙...nice to hear this...💙")
         
       elif question.lower()=="not good":
         print("sad to hear this u can share your thoughts here..👍")
         
         
       else:
        print(".🍀THANKS FOR SHARING🍀.")
ask_question()
