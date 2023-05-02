import tkinter 
from tkinter import *
#from tkinter import tkk

# colors ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
background = "#3b3b3b" # preta / black

#creating a main window
window = Tk()
window.title("")
window.geometry("260x390")
window.configure(bg=background)

# divides the windows in 2 frames
frame_top = Frame(window, width=240, height=100, bg=co1, relief="raised")
frame_top.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_bottom = Frame(window, width=240, height=300, bg=background, relief="flat")
frame_bottom.grid(row=1, column=0, sticky=NW)

#------------------
#setting frame_top
#------------------
#player 1
app_x = Label(frame_top, text="X", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_top, text="Player 1", height=1, relief="flat", anchor="center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_x.place(x=25, y=70)
app_x_points = Label(frame_top, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_x_points.place(x=80, y=20)
#separator
app_sep = Label(frame_top, text=":", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_sep.place(x=110, y=18)
#player 2
app_o = Label(frame_top, text="O", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co4)
app_o.place(x=173, y=10)
app_o = Label(frame_top, text="Player 2", height=1, relief="flat", anchor="center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_o.place(x=175, y=70)
app_o_points = Label(frame_top, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_o_points.place(x=132, y=20)


save_result = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

score_1 = 0
score_2 = 0

who_playing = "X"
next_player = ""
count = 0
count_round = 0

def Play():
    b_play.place(x=800, y=350)

    # to game control
    def Control(i):
        global who_playing
        global next_player    #ndicate who is the player of the round
        global count
        
        #print(i)
        # lin1 x col1
        if i==str(1):
            #check if the position is empty
            if b1_1["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                if who_playing == "O": color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b1_1["fg"] = color
                b1_1["text"] = who_playing
                save_result[0][0] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_player = "Player 1"
                else:
                    who_playing = "X"
                    next_player = "Player 2"   

                count +=1

        # lin1 x col2
        if i==str(2):
            #check if the position is empty
            if b1_2["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b1_2["fg"] = color
                b1_2["text"] = who_playing
                save_result[0][1] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin1 x col3
        if i==str(3):
            #check if the position is empty
            if b1_3["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b1_3["fg"] = color
                b1_3["text"] = who_playing
                save_result[0][2] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1
       
        #line2 x col1
        if i==str(4):
            #check if the position is empty
            if b2_1["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                if who_playing == "O": color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b2_1["fg"] = color
                b2_1["text"] = who_playing
                save_result[1][0] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin2 x col2
        if i==str(5):
            #check if the position is empty
            if b2_2["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b2_2["fg"] = color
                b2_2["text"] = who_playing
                save_result[1][1] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin2 x col3
        if i==str(6):
            #check if the position is empty
            if b2_3["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b2_3["fg"] = color
                b2_3["text"] = who_playing
                save_result[1][2] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin3 x col1
        if i==str(7):
            #check if the position is empty
            if b3_1["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                if who_playing == "O": color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b3_1["fg"] = color
                b3_1["text"] = who_playing
                save_result[2][0] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin3 x col2
        if i==str(8):
            #check if the position is empty
            if b3_2["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b3_2["fg"] = color
                b3_2["text"] = who_playing
                save_result[2][1] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1

        # lin3 x col3
        if i==str(9):
            #check if the position is empty
            if b3_3["text"]=="":
                #checks who the player is and thus defines the color of the symbol (X = red / O = blue)
                if who_playing == "X": color = co7
                else: color = co8
            
                #set the color of the button text and mark the position in the table with the value of the current player
                b3_3["fg"] = color
                b3_3["text"] = who_playing
                save_result[2][2] = who_playing

                #check who is who_playing to switch players
                if who_playing == "X": 
                    who_playing = "O"
                    next_play = "Player 1"
                else:
                    who_playing = "X"
                    next_play = "Player 2"   

                count +=1
       
        #if the counter is >= 5, check if there were any winners according to the following patterns within the table:
        #win lines    : [[1, 1, 1], [...], [...]] / [[...], [1, 1, 1], [...]] / [[...], [...], [1, 1, 1]]
        #win cols     : [1, 0, 0], [1, 0, 0], [1, 0, 0]] / [0, 1, 0], [0, 1, 0], [0, 1, 0]] / [0, 0, 1], [0, 0, 1], [0, 0, 1]]  
        #win diagonals: [1, ... ...], [..., 1, ...], [..., ..., 1] /  [..., ..., 1] [..., 1, ...], [1, ..., ...]
        
        if count >= 5:
            #check if ther is a winner on the lines
            if save_result[0][0] == save_result[0][1] == save_result[0][2] != "": Winner(who_playing)
            if save_result[1][0] == save_result[1][1] == save_result[1][2] != "": Winner(who_playing)
            if save_result[2][0] == save_result[2][1] == save_result[2][2] != "": Winner(who_playing)      

            #check if ther is a winner on the cols
            if save_result[0][0] == save_result[1][0] == save_result[2][0] != "": Winner(who_playing)
            if save_result[0][1] == save_result[1][1] == save_result[2][1] != "": Winner(who_playing)
            if save_result[0][2] == save_result[1][2] == save_result[2][2] != "": Winner(who_playing) 
                
            #check if ther is a winner on the diagonals
            if save_result[0][0] == save_result[1][1] == save_result[2][2] != "": Winner(who_playing)
            if save_result[0][2] == save_result[1][1] == save_result[2][0] != "": Winner(who_playing)

            #tie (no winner)
            if count >= 9: 
                Winner("Tie")

  
    def Winner(player):
        global save_result
        global score_1
        global score_2
        global count_round
        global count

        # disable buttons
        b1_1["state"] = "disable"
        b1_2["state"] = "disable"
        b1_3["state"] = "disable"
        b2_1["state"] = "disable"
        b2_2["state"] = "disable"
        b2_3["state"] = "disable"
        b3_1["state"] = "disable"
        b3_2["state"] = "disable"
        b3_3["state"] = "disable"

        app_winner = Label(frame_bottom, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_winner.place(x=39, y=238)

        if player =='X':
            score_2+=1
            app_winner['text'] = 'Player 2 won'
            app_o_points['text'] =score_2

        if player =='O':
            score_1+=1
            app_winner['text'] = 'Player 1 won'
            app_x_points['text'] =score_1

        if player=='Tie':
            app_winner['text'] = 'Tie'

        def start():
            # limpando os botoes
            b1_1["text"] = ""
            b1_2["text"] = ""
            b1_3["text"] = ""
            b2_1["text"] = ""
            b2_2["text"] = ""
            b2_3["text"] = ""
            b3_1["text"] = ""
            b3_2["text"] = ""
            b3_3["text"] = ""

            b1_1["state"] = "normal"
            b1_2["state"] = "normal"
            b1_3["state"] = "normal"
            b2_1["state"] = "normal"
            b2_2["state"] = "normal"
            b2_3["state"] = "normal"
            b3_1["state"] = "normal"
            b3_2["state"] = "normal"
            b3_3["state"] = "normal"

            app_winner.destroy()
            b_play.destroy()

        # Botao jogar
        b_play = Button(frame_bottom, command=start, text='Next round', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=background, fg=co0 )
        b_play.place(x=86, y=205)


        def GameOver():
            b_play.destroy()
            app_winner.destroy()

            Stop()  

        if count_round >= 5:
            GameOver()
        else:
            count_round+=1
            # restart table
            save_result = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            count = 0

    #finish the actual game
    def Stop():
        global save_result
        global count_round
        global score_1
        global score_2
        global count

        save_result = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        count_round = 0
        score_1 = 0
        score_2 = 0
        count = 0

        # disable buttons
        b1_1["state"] = "disable"
        b1_2["state"] = "disable"
        b1_3["state"] = "disable"
        b2_1["state"] = "disable"
        b2_2["state"] = "disable"
        b2_3["state"] = "disable"
        b3_1["state"] = "disable"
        b3_2["state"] = "disable"
        b3_3["state"] = "disable"

        app_end = Label(frame_bottom, text='The game is over', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_end.place(x=36, y=90)

        #play a new game
        def Play_Again():
            app_x_points['text'] = '0'
            app_o_points['text'] = '0'

            app_end.destroy()
            b_play.destroy()

            #call function to start the game
            Play()

        #button to play again
        b_play = Button(frame_bottom, command=Play_Again, text='Play again', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=background, fg=co0 )
        b_play.place(x=87, y=215)


    #---------------------
    #setting frame_bottom
    #---------------------
    #vertical lines
    app_lines = Label(frame_bottom, text="", height=24, relief="flat", pady=5, anchor="center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_lines.place(x=90, y=15)
    app_lines = Label(frame_bottom, text="", height=24, relief="flat", pady=5, anchor="center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_lines.place(x=157, y=15)
    #horizontal lines
    app_lines = Label(frame_bottom, text="", width=187, relief="flat", padx=2, anchor="center", font=("Ivy 1 bold"), bg=co0, fg=co0)
    app_lines.place(x=30, y=72)
    app_lines = Label(frame_bottom, text="", width=187, relief="flat", padx=2, anchor="center", font=("Ivy 1 bold"), bg=co0, fg=co0)
    app_lines.place(x=30, y=135)

    #-----------
    # buttons
    #-----------
    #line 1
    b1_1 = Button(frame_bottom, command=lambda:Control("1"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b1_1.place(x=30, y=15)
    b1_2 = Button(frame_bottom, command=lambda:Control("2"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b1_2.place(x=97, y=15)
    b1_3 = Button(frame_bottom, command=lambda:Control("3"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b1_3.place(x=164, y=15)
    #line 2
    b2_1 = Button(frame_bottom, command=lambda:Control("4"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b2_1.place(x=30, y=81)
    b2_2 = Button(frame_bottom, command=lambda:Control("5"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b2_2.place(x=97, y=81)
    b2_3 = Button(frame_bottom, command=lambda:Control("6"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b2_3.place(x=164, y=81)
    #line 3
    b3_1 = Button(frame_bottom, command=lambda:Control("7"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b3_1.place(x=30, y=144)
    b3_2 = Button(frame_bottom, command=lambda:Control("8"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b3_2.place(x=97, y=144)
    b3_3 = Button(frame_bottom, command=lambda:Control("9"), text="", width=3, height=1, font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=background, fg=co7)
    b3_3.place(x=164, y=144)

 
# who_playing
b_play = Button(frame_bottom, text="PLay", command=Play,  width=10, height=1, font=("Yvy 10 bold"), overrelief=RIDGE, relief="raised", bg=background, fg=co0)
b_play.place(x=85, y=210)

#link: https://www.youtube.com/watch?v=8qqeHip4NZQ&ab_channel=UsandoPython   (1:01:00)

window.mainloop()