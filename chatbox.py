print("Simple Question and Answering Program")
print("=====================================")
print(" You may ask any one of these questions")
print("Hi")
print("How are you?")
print("Are you working?")
print("What is your name?")
print("what did you do yesterday?")
print("Quit")
while True:
    question = input("Enter one question from above list:")
    question = question.lower()
    if question in ['hi']:
        print("Hello")
    elif question in ['how are you?','how do you do?']:
        print("I am fine")
    elif question in ['are you working?','are you doing any job?']:
        print("NO. I'am studying BIT in Central Campus of Technology")
    elif question in ['what is your name?']:
        print("My name is EDITH")
        name=input("What is your name.")
        print("Nice name and Nice meeting you",name)
    elif question in ['what did you do yesterday?']:
        print("I watched a movie")
    elif question in ['quit']:
        break
    else:
        print("I don't understand what you said")
        