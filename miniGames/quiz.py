def dailyQuiz():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    #display questions
    for key in questions:
        print("=========================================================================================================================")
        print(key)

        #display multchoice w/ nested 4 loop set index so multchoice matches quesion
        for i in answers[question_num-1]:
            print(i)

        
        guess = input("> ")

        #compare guess to correct answer
        guesses.append(guess)
        #sets correct guesses to increment with each correct answer
        correct_guesses += checkQuiz(questions.get(key), guess)        
        question_num += 1
    
    gradeScore(correct_guesses, guesses)


def checkQuiz(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0

def gradeScore(correct_guesses, guesses):
    print("")
    print("=======================================================================================================")
    print("GRADE: ")
    print("=======================================================================================================")
    # print("Answers: " end= "")

    for i in questions:
        print(questions.get(i), end= " ")
    print()
    for i in guesses:
        print(i, end= " ")
    print()

    finalGrade = int((correct_guesses/len(questions))*100)
    print(f"You got a {finalGrade}% on this quiz!")

    if finalGrade == 100:
        print("You got a perfect quiz! You know your stuff!")
    elif finalGrade >= 65 & finalGrade < 100:
        print("Clearly you're familiar but a little studying never hurt...")
    else:
        print("Better luck next time~")
    




#dictionary of questions and answers

questions = {
    "What did King Herod the Great build in Jerusalem?" : "1",
    "What was the capital before King David united the kingdom? " : "3",
    "Which famous Jewish scholar and philosopher was born in Jerusalem during the medieval period?" : "2",
    "After King Shlomo's reign what were the two kingdoms called when the Land of Israel split?" : "4",
    "What was the name of the IDF operation during the Six-Day War that destroyed the Egyptian Air Force?" : "1",
    "Whats the origional name for the Dome of the Rock" : "2",
    "Which great body of water sits to the west of Israel? " : "4",
}

#list of lists for answers
answers = [[
    "1. Beit Hamikdash II ",
    "2. Eternal Popcorn Stand",
    "3. A canal",
    "4. His fortress"],
    
    ["1. Tel Aviv ",
     "2. Haifa",
     "3. Chevron",
     "4. Tzfat"],
     
    ["1. Ramban",
     "2. Rambam",
     "3. Rashba",
     "4. Rabbi Yosef Cairo"],

    ["1. Acher and B'nei Yisrael",
     "2. Yeruvam and Rechavam",
     "3. Chashmoni and Tzdoki",
     "4. Yehudah and Yisrael"],

    ["1. Operation Moked",
     "2. Operation Paroh",
     "3. Operation Yam Suf",
     "4. Operation Har Sinai"],

    ["1. Kodesh Kedushim",
     "2. Har Habayit",
     "3. Kever Avot",
     "4. Bima Place"],

    ["1. The Dead Sea",
     "2. The Sea of Galil",
     "3. The Red Sea",
     "4. The Mediterranean Sea"]]


dailyQuiz()