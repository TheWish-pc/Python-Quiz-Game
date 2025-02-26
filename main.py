#empty list to store questions
questions = []

#allows me to easily create questions at run time because I am too lazy to hard code this. this is worth the inefficiency imo lol
def createQuestion(q : str, a : str, b : str, c : str, d : str, ans : str):
    #dictionary to help format questions
    tempDict = {
        'Question' : q,
        'A' : a,
        'B' : b,
        'C' : c,
        'D' : d,
        'Answer' : ans
    }
    questions.append(tempDict)

createQuestion('Who was the first president of the United States of America?', 'Abraham Lincoln', "Thomas Jefferson", "Donald Trump", "George Washington", "D")
createQuestion('Who assassinated Abraham Lincoln?', 'Elon Musk', 'John Wilks Booth', 'Stewart Knechtle', 'Syndney Sweeney', 'B')
createQuestion('What is the name of our home planet?', 'Saturn', 'Jupiter', 'Earth', 'Mars', 'C')
createQuestion('What is the powerhouse of the cell?', 'Mitochandria', 'Nucleus', 'Heart', 'Cytoplasm', 'A')
createQuestion('How much is a dozen?', '6', '3', '24', '12', 'D')


print('QUESTIONS: \n')

#prints out all questions in a neat manner
for i in range(len(questions)):
    print('Question ' + str(i+1) + ': ' + questions[i]['Question'])
    print('A. ' + questions[i]['A'])
    print('B. ' + questions[i]['B'])
    print('C. ' + questions[i]['C'])
    print('D. ' + questions[i]['D'])
    print('Answer: ' + questions[i]['Answer'] + '\n')

print('-------------------------------------------------------------------------------------------\n \n \n \n')

#This is where the actual game code begins

#checks to see if the game is currently in play
playing = True
#stores which question the user is on
currentQ = 0

#formats questions in a neat manner for easy printing
def displayQuestion():
    print('Question ' + str(currentQ+1) + ': ' + questions[currentQ]['Question'])
    print('A. ' + questions[currentQ]['A'])
    print('B. ' + questions[currentQ]['B'])
    print('C. ' + questions[currentQ]['C'])
    print('D. ' + questions[currentQ]['D'])

#prompts the user to answer question, and handles logic for user answers
def promptAnswer():
    global currentQ
    userAnswer = input('Answer: ')

    #increases current question by 1 if the answer is correct
    if userAnswer == questions[currentQ]['Answer']:
        print('Correct!')
        currentQ+=1
    #skips to the last question for easily testing
    elif userAnswer == 'end':
        print('Skipped to end')
        currentQ = len(questions) - 1
    #tells the user their answer is incorrect, and allows them to try again due to while loop
    else:
        print('Incorrect!')
    pass

#allows me to easily control when game ends
while playing:
    displayQuestion()
    promptAnswer()
    #game ends when current Question become greater than or equal to the length of the questions list
    if currentQ >= len(questions):
        print('\n' + 'That is the end of the quizz, thanks for playing!')
        playing = False