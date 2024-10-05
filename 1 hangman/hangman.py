import tkinter as tk 
import random

window = tk.Tk()
window.config(background="#318ffc")
window.state('zoomed')
window.title('Hangman')

window_width = window.winfo_screenwidth() /100
window_height = window.winfo_screenheight() /100

myCanvas = tk.Canvas(window, width = 500, height = 500, bg = '#318ffc', highlightthickness = 0 )
myCanvas.place(x= (window_width * 40), y =(window_height * 2))
 
#words = ['hello','goodbye','tyrannosaurus']  
words = []
with open('Hangmanwords.txt') as file:
    for line in file:
        current_word = line.rstrip()
        words.append(current_word)

line1 = myCanvas.create_line(490, 10, 490, 490, width= 10, fill = '#35281d')
line2 = myCanvas.create_line(250, 480, 500, 480,  width= 10, fill = '#35281d')
line3 = myCanvas.create_line(250, 10, 500, 10, width= 10, fill = '#35281d')
line4 = myCanvas.create_line(250, 0, 250, 100, width= 10, fill = '#35281d')

line5 = myCanvas.create_oval(200, 100, 300, 200, width= 5, outline ='white')
line6 = myCanvas.create_line(250, 200, 250, 300, width= 10, fill  ='white')
line7 = myCanvas.create_line(350, 300, 250, 200, width= 10, fill  ='white')
line8 = myCanvas.create_line(150, 300, 250, 200, width= 10, fill  ='white')
line9 = myCanvas.create_line(350, 400, 250, 300, width= 10, fill  ='white')
line10 = myCanvas.create_line(150, 400, 250, 300, width= 10, fill  ='white')

canvas2 = tk.Canvas(window, width = window_width * 100, height = 50, bg = '#318ffc', highlightthickness = 0 )
canvas2.place(x = 0, y = window_height * 80)

winner_label = tk.Label(window, text = '', font = ('arial', 15), bg = '#318ffc')

win_label = tk.Label(window, text = '', font = ('arial', 25), bg = '#318ffc', fg = 'white')
loss_label = tk.Label(window, text = '', font = ('arial', 25), bg = '#318ffc', fg = 'white')
win_label.place(x = window_width * 80, y = window_height * 10)
loss_label.place(x = window_width * 80, y = window_height * 15)
won_score = 0 
lost_score = 0

winner = ''
def check_winner():
    global current_count
    global word_size
    global winner_label
    global winner
    global won_score
    global lost_score
    current_letters = 0
    if current_count >=6:
        winner = 0 
    for i in range(word_size):
        if labels[i].cget('text') != '?':
            current_letters = current_letters + 1
    if current_letters == word_size:
        winner = 1
    if winner == 1:
        winner_label.config(text = 'Win! Well Done you  won')
        winner_label.place(x = window_width * 80, y = 40)
        won_score = won_score + 1
        win_label.config(text = 'You won: ' + str(won_score) + 'times')    
    elif winner == 0 :
        winner_label.config(text = 'Oops! you lost')
        winner_label.place(x = window_width * 80, y = 40 )
        lost_score = lost_score + 1
        loss_label.config(text = 'You lost: ' + str(lost_score) + 'times') 
        for i in range(word_size):
            if labels[i].cget('text') == '?':
                labels[i].config(text = word[i].upper(), fg = '#b74f6f')

labels = []
line12 = []
def set_word():
    global labels
    global word
    global word_size
    global line12
    word = random.choice(words)
    word_size = len(word)
    position = 0
    for i in range(word_size):
        x_location = (((window_width * 45) + 10) + position) - (word_size * 42)
        line12.append(i)
        line12[i] = canvas2.create_line(x_location, 40, x_location + 90, 40, width = 20,fill = 'white')
        labels.append(i)
        labels[i] = tk.Label(window, text = '?', font = ( 'arial', 60), bg = '#318ffc', fg = 'white')
        labels[i].place(x =x_location + 25, y= window_height * 72)
        position = position + 100

current_count = 0
def create_man():
    global line5, line6, line7, line8, line9, line10, current_count

    myCanvas.delete(line5, line6, line7, line8, line9, line10)

    if current_count >= 1:    
        line5 = myCanvas.create_oval(200, 100, 300, 200, width= 20, outline ='white')
    if current_count >= 2:    
        line6 = myCanvas.create_line(250, 200, 250, 300, width= 20, fill  ='white')
    if current_count >= 3:    
        line7 = myCanvas.create_line(350, 300, 250, 200, width= 20, fill  ='white')
    if current_count >= 4:    
        line8 = myCanvas.create_line(150, 300, 250, 200, width= 20, fill  ='white')
    if current_count >= 5:    
        line9 = myCanvas.create_line(350, 400, 250, 300, width= 20, fill  ='white')
    if current_count >= 6:    
        line10 = myCanvas.create_line(150, 400, 250, 300, width= 20, fill  ='white')    
    check_winner()    

buttons = [['A','B','C','D','E','F','G'],
           ['H','I','J','K','L','M','N'],
           ['O','P','Q','R','S','T','U'],
           ['V','W','X','Y','Z']]

in_word = 1
def check_letter(row, column) :
    global word_size
    global word
    global labels
    global current_count
    global in_word
    global winner
    if winner == 1:
        return
    if current_count >=6:
        return
    for i in range(word_size):
        if buttons[row][column].cget('text') == word[i].upper():
            buttons[row][column].config(bg = '#0e131f')
            in_word = 0
            break
        else:
             buttons[row][column].config(bg = '#b74f6f')
    for i in range(word_size):
        if buttons[row][column].cget('text') == word[i].upper():
            labels[i].config(text = buttons[row][column].cget('text'))
    if in_word == 1:
        current_count = current_count + 1    
    in_word = 1
    create_man()    

x_place = 10
y_place = 10
for i in range(4) :
    for x in range(len(buttons[i])) :
        buttons[i][x] = tk.Button(window, text = buttons[i][x], font = ('arial', 30), width = 3, bg ='#318ffc', fg = 'white', \
                                  command = lambda row = i, column = x : check_letter(row, column))
        buttons[i][x].place(x= x_place, y = y_place)
        x_place = x_place + 80
    x_place = 10
    y_place = y_place + 80

set_word()    
create_man()

def retry_func():
    global winner
    global winner_label
    global current_count
    global labels
    global line12 
    global word_size
    winner = ''
    current_count = 0 
    for i in range(4):
        for x in range(len(buttons[i])):
            buttons[i][x].config(bg = '#318ffc')
        for i in range(word_size):
            labels[i].destroy()
        labels = []
        for i in range(word_size):
            canvas2.delete(line12[i])
        line12 = []
        winner_label.config(text = '')
        set_word()
        create_man()            

retry_button = tk.Button(window, text = 'Try Again', font=('arial',40), bg ='#318ffc', fg = 'white',\
                         command = lambda: retry_func())
retry_button.place(x = 100 , y = window_height * 50)

def clear_func():
    global won_score
    global lost_score
    win_label.config(text = '')
    loss_label.config(text = '')
    won_score = 0 
    lost_score = 0
   #name_label.config(text = '')


clear_button =  tk.Button(window, text = 'clear', font = ('arial',30), bg = '#318ffc', fg = 'white', \
                          command = lambda: clear_func())
clear_button.place( x = window_width * 80, y = window_height * 30)


window.mainloop() 