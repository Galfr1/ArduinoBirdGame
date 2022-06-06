import tkinter as tk
import serial
import time
import random
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
    ser.flush()
    ser1 = serial.Serial('/dev/ttyUSB1',9600, timeout=1)
    ser1.flush()
questions = ["?תירוזחמה הלבטה יהמ","?רתויב ןטקה קיקלחה והמ","?םוטאה ןיערגב שי המ","?יבויח ןוי והמ","?ילילש ןוי והמ","?ימוטא רפסמ והמ","?הלבוהה תכרעמ לש הדיקפת והמ","?םיאתל םדה ילכ ןיב עצבתמ ךילהת הזיא","?םירמוחה ףוליח עצבתמ ןכיה","?בלה לש ודיקפת והמ","?םירמוחה ףוליחב םילבקמ םיאתה המ","?םירמוחה ףוליחב םיטלופ םיאתה המ","?הריבצה יבצמ םהמ","?ךילומל רמוח ךפוה המ","?תוסיסמ יהמ"]
correctAnswers = [1,2,4,2,3,1,1,2,3,4,4,1,3,1,2,1]
options1 = ["םהלש םימוטאה לש ימיכה למסהו ימוטאה רפסמה יפל תודוסיה לכ תא הגיצמש הלבט","ןוטורפ","םינורטקלאו םינורטוינ","םינורטקלאה רפסממ ןטק םינוטורפה רפסמ ובש םוטא","תונוכנ תובושתה לכ","םיוסמ םוטא לש ןיערגב םיאצמנה םינוטורפה רפסמ","םדה תועצמאב םהלש םויקה יכרוצ לכ תא ףוגב םיאתה לכל קפסל","םירכוס ףוליח","בלל םדה ילכ ןיב","תומודא םד תוירודכ םדל סינכהל","םינימטיו","םהל םישורד םניאש םירמוחו תלוספ","לזונו זג קצומ","םיישפוח םינורטקלא","רחא רמוח לש םיקיקלח םע תולוקלומ םירצוי רמוחה יקיקלח"]
options2 = ["םהלש הסמה יפל םירמוחה יגוס לכ תא הגיצמש הלבט","ןורטקלא","םינורטוינ","םינוטורפה רפסממ ןטק םינורטקלאה רפסמ ובש םוטא","םינוטורפה רפסממ ןטק םינורטקלאה רפסמ ובש םוטא","םיוסמ םוטא לש ןיערגב םיאצמנה םינורטקלאה רפסמ","ןצמח םיאתל קפסל","םירמוח ףוליח","םדה ילכ ןיב","חומל םד ריבעהל","זוקולג","ינצמח וד ןמחפ","קוצימו החיתר ןואפיק","םיישפוח םינוטורפ","רחא רמוח לש םיקיקלח םע בברעתהל םילוכי רמוחה יקיקלח"]
options3 = ["םהיתונוכת יפל תולוקלומה יגוס לכ תא הגיצמש הלבט","ןורטוינ","םינורטקלאו םינוטורפ","םינורטקלאה רפממ לודג םינורטוינה רפסמ ובש םוטא","םינורטקלאה רפסממ ןטק םינוטורפה רפסמ ובש םוטא","םיוסמ םוטא לש ןיערגב םיאצמנה םינורטוינה רפסמ","םיאתהמ םיישומיש אל םירמוחו תלוספ תונפל","םימזינגרוא ףוליח","םיאתל םדה ילכ ןיב","םדל ןצמח סינכהל","ןילוסניא","םילער","לזונו זג קצומ המזלפ","םיישפוח םינורטוינ","רחא רמוח לש םיקיקלח םע םיבברעתמ רמוחה יקיקלח"]
options4 = ["םהלש ימוטאה רפסמה יפל תודוסיה לכ תא הגיצמש הלבט","םוטא","םינורטוינו םינוטורפ","םינורטוינה רפממ לודג םינורטקלאה רפסמ ובש םוטא","םינורטוינה רפממ לודג םינורטקלאה רפסמ ובש םוטא","תירוזחמה הלבטב דוסיה לש ומוקימ גציימה רפסמ","םירמוח ףוליח עצבל","הזטניסוטופ","אתה תומקר ןיב","תונשנו תורזוח תויוצווכתה ךות םדה תא םירזהל","םיפסונ םירמוחו רכוס ןצמח","םירכוס","םידאו ילזונ השק","םיפדוע םינורטקלא","רחא רמוחב ףוצל םילוכי רמוחה יקיקלח"]
frame = tk.Tk() 
frame.title("Bird ScoreBoard") 
frame.geometry('500x600')
title = tk.Label(frame, text = "Bird!", font = ("ariel", 44))
title.pack()
title1 = tk.Label(frame, text = "Controller 1:", font = ("ariel", 12))
title1.pack()
inputtxt = tk.Text(frame, height = 1, width = 40) 
inputtxt.pack()
title2 = tk.Label(frame, text = "Controller 2:", font = ("ariel", 12))
title2.pack()
inputtxt1 = tk.Text(frame, height = 1, width = 40) 
inputtxt1.pack()
scoreList = tk.Label(frame, text = "", font = ("ariel", 18))
def printInput():
    randomQuestionNum = random.randint(0,14)
    popup = tk.Tk()
    def answer1():
        popup.destroy()
        if correctAnswers[randomQuestionNum] == 1:
            ser.write(b"start\n")
            ser1.write(b"start\n")
            time.sleep(120)
            ser.write(b"end\n")
            ser1.write(b"end\n")
            time.sleep(1)
            if ser.in_waiting > 0:
                line = int(ser.readline().decode('utf-8').rstrip())
                line1 = int(ser1.readline().decode('utf-8').rstrip())
                if line > line1:
                    inp = inputtxt.get(1.0, "end-1c")
                    List = scoreList.cget("text")
                    scoreList.config(text = List + " \n " + inp + "    |    " + str(line))
                if line < line1:
                    inp1 = inputtxt1.get(1.0, "end-1c")
                    List1 = scoreList.cget("text")
                    scoreList.config(text = List1 + " \n " + inp1 + "    |    " + str(line1))
                if line == line1:
                    inp2 = inputtxt.get(1.0, "end-1c")
                    inp3 = inputtxt1.get(1.0, "end-1c")
                    List2 = scoreList.cget("text")
                    scoreList.config(text = List2 + " \n " + inp2 + " and " + inp3 + "    |    " + str(line))
    def answer2():
        popup.destroy()
        if correctAnswers[randomQuestionNum] == 2:
            ser.write(b"start\n")
            ser1.write(b"start\n")
            time.sleep(120)
            ser.write(b"end\n")
            ser1.write(b"end\n")
            time.sleep(1)
            if ser.in_waiting > 0:
                line = int(ser.readline().decode('utf-8').rstrip())
                line1 = int(ser1.readline().decode('utf-8').rstrip())
                if line > line1:
                    inp = inputtxt.get(1.0, "end-1c")
                    List = scoreList.cget("text")
                    scoreList.config(text = List + " \n " + inp + "    |    " + str(line))
                if line < line1:
                    inp1 = inputtxt1.get(1.0, "end-1c")
                    List1 = scoreList.cget("text")
                    scoreList.config(text = List1 + " \n " + inp1 + "    |    " + str(line1))
                if line == line1:
                    inp2 = inputtxt.get(1.0, "end-1c")
                    inp3 = inputtxt1.get(1.0, "end-1c")
                    List2 = scoreList.cget("text")
                    scoreList.config(text = List2 + " \n " + inp2 + " and " + inp3 + "    |    " + str(line))
    def answer3():
        popup.destroy()
        if correctAnswers[randomQuestionNum] == 3:
            ser.write(b"start\n")
            ser1.write(b"start\n")
            time.sleep(120)
            ser.write(b"end\n")
            ser1.write(b"end\n")
            time.sleep(1)
            if ser.in_waiting > 0:
                line = int(ser.readline().decode('utf-8').rstrip())
                line1 = int(ser1.readline().decode('utf-8').rstrip())
                if line > line1:
                    inp = inputtxt.get(1.0, "end-1c")
                    List = scoreList.cget("text")
                    scoreList.config(text = List + " \n " + inp + "    |    " + str(line))
                if line < line1:
                    inp1 = inputtxt1.get(1.0, "end-1c")
                    List1 = scoreList.cget("text")
                    scoreList.config(text = List1 + " \n " + inp1 + "    |    " + str(line1))
                if line == line1:
                    inp2 = inputtxt.get(1.0, "end-1c")
                    inp3 = inputtxt1.get(1.0, "end-1c")
                    List2 = scoreList.cget("text")
                    scoreList.config(text = List2 + " \n " + inp2 + " and " + inp3 + "    |    " + str(line))
    def answer4():
        popup.destroy()
        if correctAnswers[randomQuestionNum] == 4:
            ser.write(b"start\n")
            ser1.write(b"start\n")
            time.sleep(120)
            ser.write(b"end\n")
            ser1.write(b"end\n")
            time.sleep(1)
            if ser.in_waiting > 0:
                line = int(ser.readline().decode('utf-8').rstrip())
                line1 = int(ser1.readline().decode('utf-8').rstrip())
                if line > line1:
                    inp = inputtxt.get(1.0, "end-1c")
                    List = scoreList.cget("text")
                    scoreList.config(text = List + " \n " + inp + "    |    " + str(line))
                if line < line1:
                    inp1 = inputtxt1.get(1.0, "end-1c")
                    List1 = scoreList.cget("text")
                    scoreList.config(text = List1 + " \n " + inp1 + "    |    " + str(line1))
                if line == line1:
                    inp2 = inputtxt.get(1.0, "end-1c")
                    inp3 = inputtxt1.get(1.0, "end-1c")
                    List2 = scoreList.cget("text")
                    scoreList.config(text = List2 + " \n " + inp2 + " and " + inp3 + "    |    " + str(line))
    popup.title("Question!")
    popup.geometry('700x700')
    label = tk.Label(popup, text = questions[randomQuestionNum], font = ("ariel", 12))
    ans1 = tk.Button(popup, text = options1[randomQuestionNum], command = answer1)
    ans2 = tk.Button(popup, text = options2[randomQuestionNum], command = answer2)
    ans3 = tk.Button(popup, text = options3[randomQuestionNum], command = answer3)
    ans4 = tk.Button(popup, text = options4[randomQuestionNum], command = answer4)
    label.pack()
    ans1.pack()
    ans2.pack()
    ans3.pack()
    ans4.pack()
    popup.mainloop()

printButton = tk.Button(frame, text = "Start Game",  command = printInput) 
printButton.pack()
subtitle = tk.Label(frame, text = "ScoreBoard:", font = ("ariel", 24))
subtitle.pack()
scoreList.pack()
winnerLabel = tk.Label(frame, text = "", font = ("ariel", 14))
def end():
    lList = scoreList.cget("text")
    data = lList.split(" \n ")
    del data[0]
    dataLen = len(data)
    i = 0
    names = []
    scores = []
    while i < dataLen:
        d1 = data[i].split("    |    ")
        names.append(d1[0])
        scores.append(d1[1])
        i = i + 1
    intScores = []
    l = 0
    scoresLen = len(scores)
    while l < scoresLen:
        intScores.append(int(scores[l]))
        l = l + 1
    sortScores = max(intScores)
    winnerScore = sortScores
    winnerIndex = scores.index(str(winnerScore))
    winnerName = names[winnerIndex]
    winnerLabel.config(text = "The winner is: " + winnerName)
endButton = tk.Button(frame, text = "End Compatition",  command = end) 
endButton.pack()
winnerLabel.pack()
frame.mainloop()