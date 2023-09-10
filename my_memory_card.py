#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

from random import shuffle, randint

#show result of your answer
questions_ans_sets = [
    ['Question1', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3'],
    ['Question2', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3'],
    ['Question3', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3']
]

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

#Set window's size
window.setFixedHeight(320)
window.setFixedWidth(640)

#Question
label = QLabel('Which nationality does not exist?', alignment=Qt.AlignCenter)
layout.addWidget(label)

#Box of options
option_box = QGroupBox('Answer options')
#Create options
opt1 = QRadioButton()
opt2 = QRadioButton()
opt3 = QRadioButton()
opt4 = QRadioButton()
options = [opt1, opt2, opt3, opt4]
answers = options
column_opts = QHBoxLayout() #store row of options
row_opts1 = QVBoxLayout() #store options as a row
row_opts2 = QVBoxLayout()
row_opts1.addWidget(options[0])
row_opts1.addWidget(options[1])
row_opts2.addWidget(options[2])
row_opts2.addWidget(options[3])

column_opts.addLayout(row_opts1)
column_opts.addLayout(row_opts2)
option_box.setLayout(column_opts)
layout.addWidget(option_box)

#Answer box
answer_box = QGroupBox('Test result')
true_false = QLabel('True/False')
correct_ans = QLabel('Correct answer', alignment=Qt.AlignCenter)
ans_row = QVBoxLayout() #Create rows to store the labels
ans_row.addWidget(true_false)
ans_row.addWidget(correct_ans)
answer_box.setLayout(ans_row)

#Add the box to layout
layout.addWidget(answer_box)
option_box.hide()
answer_box.hide()

label.setText('Memory Cards')
#Answer button
button = QPushButton('Start')
layout.addWidget(button)

#reset choices
def reset():
    button_group = QButtonGroup()
    button_group.addButton(options[0])
    button_group.addButton(options[1])
    button_group.addButton(options[2])
    button_group.addButton(options[3])

    button_group.setExclusive(False)
    opt1.setChecked(False)
    opt2.setChecked(False)
    opt3.setChecked(False)
    opt4.setChecked(False)
    button_group.setExclusive(True)


def ask(quest_ans_set):
    label.setText(quest_ans_set[0])
    shuffle(options)
    options[0].setText(quest_ans_set[1])
    options[1].setText(quest_ans_set[2])
    options[2].setText(quest_ans_set[3])
    options[3].setText(quest_ans_set[4])

def show_question():
    answer_box.hide()
    option_box.show()
    button.setText('Answer')
    reset()

def show_result():
    global score
    option_box.hide()
    answer_box.show()
    button.setText('Next question')
    if len(questions_ans_sets) == 0:
        button.setText('Result')        

def start_test():
    if button.text() == 'Answer':
        show_result()
    elif button.text() == 'Result':
        option_box.hide()
        answer_box.hide()
        button.setText('End') #Set a flag not to check answer anymomre
        button.hide()
        label.setText('Your score: ' + str(score)) 
    else:
        quest_num = randint(0, len(questions_ans_sets) - 1)
        ask(questions_ans_sets[quest_num])
        show_question()
        del questions_ans_sets[quest_num]
              

score = 0        
def check_answer():
    global score
    start_test()  
    if button.text() != 'End': #Flag to check answer
        print(options[0].text(), options[0].isChecked())       
        if options[0].isChecked():
            true_false.setText('Correct answer')
            score += 1
        else:
            true_false.setText('Incorrect answer')
            correct_ans.setText(options[0].text())


button.clicked.connect(check_answer)

window.setLayout(layout)
window.setWindowTitle('Memory Card')
window.show()
app.exec_()