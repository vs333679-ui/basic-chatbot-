from datetime import datetime, timedelta

print("---✨WELCOME TO THE CHATBOT✨---")

def get_username():
    return input("😊 MAY I ASK YOUR NAME: ")

name = get_username()
print("Nice to meet you", name)

def ask_question():
    while True:

        question = input("HOW ARE YOU TODAY? 💬 : ")

        if question.lower() == "done":
            print("Goodbye 👋", name, "Have a nice day!")
            break

        elif question.lower() == "fine":
            print("❤️ Nice to hear this...❤️")

        elif question.lower() == "not good":
            print("Sad to hear this. You can share your thoughts here. 🤍")

        elif question.lower() == "time":
            current_time = (datetime.now() + timedelta(hours=5, minutes=30)).strftime("%I:%M %p")
            print("CURRENT TIME IS:", current_time)

        elif question.lower() == "date":
            current_date = (datetime.now() + timedelta(hours=5, minutes=30)).strftime("%d-%m-%Y")
            print("TODAY'S DATE IS:", current_date)

        else:
            print("🌸 Thanks for sharing! 🌸")

ask_question()