from tkinter import *
import csv


def backtomenu():
  window9.destroy()
  session()
  
def leaderboard():
 global window9
 window9 = Toplevel(window)
 window9.title("Leaderboard")
 window9.geometry("350x400")
 Label(window9,text="").pack()
 Label(window9,text="Leaderboard", font=('Arial',12), bg = '#C3C3D5', fg = '#333347',width=100,height=2).pack()
 Label(window9,text="").pack()

 with open('leaderboard.csv','r') as leaderboard:
   global listreader
   readleader = csv.reader(leaderboard)
   allrows = list(readleader)
   csvlist = allrows[1:]
   for i in range(len(csvlist)):
      csvlist[i][1]=int(csvlist[i][1])
   csvlist1= sorted(csvlist, key= lambda x: x[1],reverse = True)
   
   if len(csvlist1)<=5:
     for i in range(len(csvlist)):
       userscore = csvlist1[i]
       userleaderboard = userscore[0]
       scoreleaderboard = userscore[1]
       Label(window9,text = userleaderboard+'\t'+'\t' + str(scoreleaderboard), bg = '#C9C9C9',width=60, height=2).pack()
       Label(window9,text="", height = 1).pack()
       
   else:
     for i in range(5):
      userscore = csvlist1[i]
      userleaderboard = userscore[0]
      scoreleaderboard = userscore[1]
   
      Label(window9,text = userleaderboard+'\t'+'\t' + str(scoreleaderboard), bg = '#C9C9C9',width=60, height=2).pack()
      Label(window9,text="", height = 1).pack()
 Button(window9, text = 'Exit leaderboard', bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command = backtomenu).pack()
   
def storeleaderboard():
 leaderlist = [username,str(score)]
 with open('leaderboard.csv','r') as fileleader1:
   readfileleader = csv.reader(fileleader1)
   fileleaderlist = list(readfileleader)
   if leaderlist in fileleaderlist:
       leaderboard()
   elif leaderlist not in fileleaderlist:
    with open('leaderboard.csv', 'a+') as fileleader:
       writescore = csv.writer(fileleader)
       writescore.writerow(leaderlist)
       leaderboard()
  

def submit290s():
  window8.destroy()
  global score
  global x
  if songguess2==song:
    score = score+1
    x = x+1
    game90s()
  elif songguess2!=song:
    storeleaderboard()
    

def caps290s():
 global songguess2
 songguess2=songguess.get().upper()
 submit290s()

def guess290s():
 global window8
 window8 = Toplevel(window)
 window8.title("Guess The Song")
 window8.geometry("400x350")
 Label(window8, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window8, text="").pack()
 guess = StringVar()
 round = x+1
 with open("1990s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
       
   letterlist = " ".join(letterlist)
   guess = StringVar()
   Label(window8, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
   Label(window8, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Incorrect, one more chance!", fg = "red", font=('Arial',10)).pack()
   Label(window8, text="").pack()
   global songguess
   songguess = Entry(window8, textvariable=guess)
   songguess.pack()
   Button(window8, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps290s).pack() 

   pointslabel= Label(window8,text='Points: {}'.format(score))
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window8,text='Round: {}'.format(round))
   roundlabel.place(relx=0, rely=1.0, anchor="sw")


def submit90s():
  global score
  global x
  if songguess1==song:
    score = score+3
    x = x+1
    game90s()
  elif songguess1!=song :
    guess290s()

def caps90s():
 global songguess1
 songguess1=songguess.get().upper()
 submit90s()
   

def game90s():
 global window7
 window7 = Toplevel(window)
 window7.title("Guess The Song")
 window7.geometry("400x350")
 Label(window7, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window7, text="").pack()
 guess = StringVar()
 round = x+1
 with open("1990s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
    
   letterlist = " ".join(letterlist)
   guess = StringVar()
   if song!="end":
    Label(window7, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
    Label(window7, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="").pack()
    global songguess
    songguess = Entry(window7, textvariable=guess)
    songguess.pack()
    Button(window7, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps90s).pack() 
   elif song =="end":
     storeleaderboard()
   
   pointslabel= Label(window7,text='Points: {}'.format(score))
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window7,text='Round: {}'.format(round))
   roundlabel.place(relx=0, rely=1.0, anchor="sw")



def submit200s():
  window8.destroy()
  global score
  global x
  if songguess2==song:
    score = score+1
    x = x+1
    game00s()
  elif songguess2!=song:
    storeleaderboard()
    

def caps200s():
 global songguess2
 songguess2=songguess.get().upper()
 submit200s()

def guess200s():
 global window8
 window8 = Toplevel(window)
 window8.title("Guess The Song")
 window8.geometry("400x350")
 Label(window8, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window8, text="").pack()
 guess = StringVar()
 round = x+1
 with open("2000s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
       
   letterlist = " ".join(letterlist)
   guess = StringVar()
   Label(window8, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
   Label(window8, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Incorrect, one more chance!", fg = "red", font=('Arial',10)).pack()
   Label(window8, text="").pack()
   global songguess
   songguess = Entry(window8, textvariable=guess)
   songguess.pack()
   Button(window8, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps200s).pack() 

   pointslabel= Label(window8,text='Points: {}'.format(score))
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window8,text='Round: {}'.format(round))
   roundlabel.place(relx=0, rely=1.0, anchor="sw")


def submit00s():
  global score
  global x
  if songguess1==song:
    score = score+3
    x = x+1
    game00s()
  elif songguess1!=song :
    guess200s()


def caps00s():
 global songguess1
 songguess1=songguess.get().upper()
 submit00s()

   
def game00s():
 global window7
 window7 = Toplevel(window)
 window7.title("Guess The Song")
 window7.geometry("400x350")
 Label(window7, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window7, text="").pack()
 guess = StringVar()
 round = x+1
 with open("2000s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
    
   letterlist = " ".join(letterlist)
   guess = StringVar()
   if song!="end":
    Label(window7, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
    Label(window7, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="").pack()
    global songguess
    songguess = Entry(window7, textvariable=guess)
    songguess.pack()
    Button(window7, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps00s).pack() 
   elif song =="end":
     storeleaderboard()
   
   pointslabel= Label(window7,text='Points: {}'.format(score))
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window7,text='Round: {}'.format(round))
   roundlabel.place(relx=0, rely=1.0, anchor="sw")



def submit210s():
  window8.destroy()
  global score
  global x
  if songguess2==song:
    score = score+1
    x = x+1
    game10s()
  elif songguess2!=song:
    storeleaderboard()
    

def caps210s():
 global songguess2
 songguess2=songguess.get().upper()
 submit200s()

def guess210s():
 global window8
 window8 = Toplevel(window)
 window8.title("Guess The Song")
 window8.geometry("400x350")
 Label(window8, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window8, text="").pack()
 guess = StringVar()
 round = x+1
 with open("2010s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
       
   letterlist = " ".join(letterlist)
   guess = StringVar()
   Label(window8, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
   Label(window8, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
   Label(window8, text="Incorrect, one more chance!", fg = "red", font=('Arial',10)).pack()
   Label(window8, text="").pack()
   global songguess
   songguess = Entry(window8, textvariable=guess)
   songguess.pack()
   Button(window8, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps210s).pack() 

   pointslabel= Label(window8,text='Points: {}'.format(score))
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window8,text='Round: {}'.format(round))
   roundlabel.place(relx=0, rely=1.0, anchor="sw")


def submit10s():
  global score
  global x
  if songguess1==song:
    score = score+3
    x = x+1
    game10s()
  elif songguess1!=song :
    guess210s()
  #elif song == "end":
   # storeleaderboard()


def caps10s():
 global songguess1
 songguess1=songguess.get().upper()
 submit10s()


def game10s():
 global window7
 window7 = Toplevel(window)
 window7.title("Guess The Song")
 window7.geometry("400x350")
 Label(window7, text="Welcome to Guess The Song!", font=('Arial',11), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window7, text="").pack()
 guess = StringVar()
 round = x+1
 with open("2010s.csv", "r") as songs:
   global song
   readsongs = csv.reader(songs)
   header = next(readsongs)
   rows = list(readsongs)
   row = rows[x]
   song = row[0]
   artist = row[1]
   song1 = song.split()
   letterlist = []
     
   for word in song1:
     letter = word[0]
     letterlist.append(letter)
    
   letterlist = " ".join(letterlist)
   guess = StringVar()
   if song!="end":
    Label(window7, text="Song: {}".format(letterlist), font=('Arial',11),fg = '#333347').pack()
    Label(window7, text="Artist:{}".format(artist), font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="Guess the song!", font=('Arial',11), fg = '#333347').pack()
    Label(window7, text="").pack()
    global songguess
    songguess = Entry(window7, textvariable=guess)
    songguess.pack()
    Button(window7, text="Submit", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command = caps10s).pack() 
   elif song =="end":
     storeleaderboard()
   
   pointslabel= Label(window7,text='Points: {}'.format(score), font=('Arial',11),fg = '#333347')
   pointslabel.place(relx=1.0, rely=1.0, anchor="se")
   roundlabel = Label(window7,text='Round: {}'.format(round), font=('Arial',11),fg = '#333347')
   roundlabel.place(relx=0, rely=1.0, anchor="sw")
  
def gamepick():
  window11 = Toplevel(window)
  window11.title("Game Mode")
  window11.geometry("400x200")
  Label(window11, text ="" ).pack()
  Label(window11, text ="Please choose a game mode:",font=('Arial',11), fg = '#333347' ).pack()
  Button(window11, text ="1990's", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command= game90s ).pack()
  Button(window11, text ="2000's", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command= game00s ).pack()
  Button(window11, text ="2010's", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command= game10s ).pack()
  
def delete1():
  window6.destroy()


def rules():
  global window6
  window6 = Toplevel(window)
  window6.title("How to play")
  window6.geometry("550x400")
  Label(window6, text="RULES",width="100",height="2", font=('Arial',11), bg = '#C3C3D5', fg = '#333347').pack()
  Label(window6, text="").pack()
  Label(window6, text="").pack()
  Label(window6, text="You will be shown the first letter of each word in the title of a song and its artist",font=('Arial',10), fg = '#333347' ).pack()
  Label(window6, text="").pack()
  Label(window6, text="You will have two chances to guess the song",font=('Arial',10), fg = '#333347' ).pack()
  Label(window6, text="").pack()
  Label(window6,text="If you guess correctly the first time, you get 3 points",font=('Arial',10), fg = '#333347' ).pack()
  Label(window6, text="").pack()
  Label(window6,text="If you guess correctly the second time, you get 1 point",font=('Arial',10), fg = '#333347' ).pack()
  Label(window6, text="").pack()
  Label(window6,text="If you guess incorrectly both times, you lose",font=('Arial',10), fg = '#333347' ).pack()
  Label(window6, text="").pack()
  Button(window6, text="Start game", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command= lambda:[gamepick(),delete1()]).pack()
  Button(window6,text="Back to main menu", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command= lambda:[session(),delete1()]).pack()


def session():
  global x
  global score
  x = 0
  score = 0
  global window5
  window5 = Toplevel(window)
  window5.title("Guess The Song")
  window5.geometry("400x350")
  Label(window5, text="Welcome to Guess The Song!", width="100",height="2", font=('Arial',12), bg = '#C3C3D5', fg = '#333347').pack()
  Label(window5, text="").pack()
  Button(window5, text="Start Game", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command=gamepick).pack()
  Button(window5, text="How to play", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command=rules).pack()
  Button(window5, text= "View Leaderboard", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command =leaderboard).pack()

def loginsuccess():
  session()


def delete():
  window3.destroy()

def usernotrecognised():
  global window3
  window3 = Toplevel(window)
  window3.title("Error")
  window3.geometry("150x100")
  Label(window3, text="User Not Recognised").pack()
  Button(window3, text="Back to login", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command=delete).pack()


def loginverify():
  global username
  username = usernameverify.get()
  password = passwordverify.get()
  usernameentry.delete(0, END)
  passwordentry.delete(0, END)
  userlist = [username, password]

  with open("users.csv", "r") as file:
    reader = csv.reader(file)
    if userlist in reader:
     loginsuccess()
    else:
     usernotrecognised()


def registerinfile():
  usernameinfo = username1.get()
  passwordinfo = password1.get()
  usernameentry1.delete(0, END)
  passwordentry1.delete(0, END)
  userlist = [usernameinfo, passwordinfo]

  with open("users.csv", "a+", newline="") as file:
   writer = csv.writer(file)
   writer.writerow(userlist)

  Label(window4, text="Registration Successful", fg="green").pack()
  Button(window4,text = 'Go to login', bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command =login).pack()


def register():
  global window4
  window4 = Toplevel(window)
  window4.title("Register")
  window4.geometry("300x250")

  global username1
  global password1
  username1 = StringVar()
  password1 = StringVar()

  global usernameentry1
  global passwordentry1
  Label(window4, text="Please enter details below", font=('Arial',10), bg = '#C3C3D5', fg = '#333347',width=100).pack()
  Label(window4, text="").pack()
  Label(window4, text="Username", fg = '#333347').pack()
  usernameentry1 = Entry(window4, textvariable=username1)
  usernameentry1.pack()
  Label(window4, text="Password", fg = '#333347').pack()
  passwordentry1 = Entry(window4, textvariable=password1, show="*")
  passwordentry1.pack()
  Button(window4, text="Register", width=10, height=1, bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2', command=registerinfile).pack()

def login():
 global window2
 window2 = Toplevel(window)
 window2.title("Login")
 window2.geometry("300x250")

 Label(window2, text="Please enter details below", font=('Arial',10), bg = '#C3C3D5', fg = '#333347',width=100).pack()
 Label(window2, text="").pack()

 global usernameverify
 global passwordverify
 usernameverify = StringVar()
 passwordverify = StringVar()

 global usernameentry
 global passwordentry
 Label(window2, text="Username", fg = '#333347').pack()
 usernameentry = Entry(window2, textvariable=usernameverify)
 usernameentry.pack()


 Label(window2, text="")
 Label(window2, text="Password",fg = '#333347').pack()
 passwordentry = Entry(window2, textvariable=passwordverify, show="*")
 passwordentry.pack()
 Label(window2, text="")
 Button(window2, text="Login", width=10, height=1, bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command=loginverify).pack()


def welcome():
    global window
    window = Tk()
    window.geometry("300x250")
    window.title("Noel's Game")
    Label(text="Noel's Game", width="300",height="1", font=('Arial',12), bg = '#C3C3D5', fg = '#333347').pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="15", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="15", bg='#B1B8D3', fg = '#2A2A3C',activebackground='#CBCFE2',command=register).pack()

    window.mainloop()

welcome()