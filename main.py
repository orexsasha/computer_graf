from tkinter import *
from config import Points, Default
from tkinter.messagebox import showwarning
from math import cos, sin, pi, radians
from copy import deepcopy

PrevPoints = deepcopy(Points)


def ShowAxis():
    canvas.create_text(oX - 10, oY + 10, text='0', fill='darkgray')
    # Y
    canvas.create_line(oX, canvasHeight, oX, 5, arrow=LAST, fill='darkgray', width=2)
    canvas.create_text(canvasWidth/2+15, 15, text='Y', fill='darkgray')

    canvas.create_line(oX - 5, oY + 100, oX + 5, oY + 100, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY + 100, text='-100', fill='darkgray')

    canvas.create_line(oX - 5, oY + 200, oX + 5, oY + 200, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY + 200, text='-200', fill='darkgray')

    canvas.create_line(oX - 5, oY + 300, oX + 5, oY + 300, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY + 300, text='-300', fill='darkgray')

    canvas.create_line(oX - 5, oY - 100, oX + 5, oY - 100, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY - 100, text='100', fill='darkgray')

    canvas.create_line(oX - 5, oY - 200, oX + 5, oY - 200, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY - 200, text='200', fill='darkgray')

    canvas.create_line(oX - 5, oY - 300, oX + 5, oY - 300, fill='darkgray', width=2)
    canvas.create_text(oX - 30, oY - 300, text='300', fill='darkgray')

    # X
    canvas.create_line(0, oY, canvasWidth-15, oY, arrow=LAST, fill='darkgray', width=2)
    canvas.create_text(canvasWidth-15, oY+15, text='X', fill='darkgray')

    canvas.create_line(oX + 100, oY - 5, oX + 100, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 100, oY + 15, text='100', fill='darkgray')

    canvas.create_line(oX + 200, oY - 5, oX + 200, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 200, oY + 15, text='200', fill='darkgray')

    canvas.create_line(oX + 300, oY - 5, oX + 300, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 300, oY + 15, text='300', fill='darkgray')

    canvas.create_line(oX + 400, oY - 5, oX + 400, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 400, oY + 15, text='400', fill='darkgray')

    canvas.create_line(oX + 500, oY - 5, oX + 500, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 500, oY + 15, text='500', fill='darkgray')

    canvas.create_line(oX + 600, oY - 5, oX + 600, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX + 600, oY + 15, text='600', fill='darkgray')

    canvas.create_line(oX - 100, oY - 5, oX - 100, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 100, oY + 15, text='-100', fill='darkgray')

    canvas.create_line(oX - 200, oY - 5, oX - 200, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 200, oY + 15, text='-200', fill='darkgray')

    canvas.create_line(oX - 300, oY - 5, oX - 300, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 300, oY + 15, text='-300', fill='darkgray')

    canvas.create_line(oX - 400, oY - 5, oX - 400, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 400, oY + 15, text='-400', fill='darkgray')

    canvas.create_line(oX - 500, oY - 5, oX - 500, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 500, oY + 15, text='-500', fill='darkgray')

    canvas.create_line(oX - 600, oY - 5, oX - 600, oY + 5, fill='darkgray', width=2)
    canvas.create_text(oX - 600, oY + 15, text='-600', fill='darkgray')
    if AxisXYVar.get() == 'OFF':
        canvas.delete('all')
    Draw()


def f(a, b, t):
    return [a*cos(t)+oX, b*sin(t)+oY]


def copyPoints():
    for i in range(len(Points)):
        for j in range(len(Points[i])):
            PrevPoints[i][j] = Points[i][j]


def Draw():
    canvas.create_polygon(Points[0], fill='', outline='black')  #Astroid
    canvas.create_polygon(Points[2], fill='', outline='black')  #Circle
    canvas.create_line(Points[3])   #left line
    canvas.create_line(Points[4])   #bot line
    canvas.create_line(Points[5])   #right line


def Move():
    copyPoints()
    try:
        x = float(entryX.get())
        y = float(entryY.get())
        for i in range(len(Points)):
            for j in range(len(Points[i])):
                if j % 2 == 0:
                    Points[i][j] += x
                else:
                    Points[i][j] -= y
            canvas.delete('all')
        if AxisXYVar.get() == 'ON':
            ShowAxis()
        else:
            Draw()
    except ValueError:
        showwarning('Некорректный ввод', 'Ввод был выполнен некорректно.')


def Rotate():
    copyPoints()
    try:
        x = float(RotateXEntry.get()) + oX
        y = float(RotateYEntry.get()) + oY
        angle = float(RotateEntryAngle.get())

        # angle = (angle / 180) * pi
        angle = -radians(angle)

        for i in range(len(Points)):
            for j in range(len(Points[i])):
                if j % 2 == 0:
                    old_x = Points[i][j]
                    Points[i][j] = x + (old_x - x) * cos(angle) - (Points[i][j+1] - y) * sin(angle)
                else:
                    old_y = Points[i][j]
                    Points[i][j] = y + (old_x - x) * sin(angle) + (old_y - y) * cos(angle)
            canvas.delete('all')

        if AxisXYVar.get() == 'ON':
            ShowAxis()
        else:
            Draw()
    except ValueError:
        showwarning('Некорректный ввод', 'Ввод был выполнен некорректно.')


def Scaling():
    copyPoints()
    try:
        xPoint = float(ScalePointXEntry.get()) + oX
        yPoint = float(ScalePointYEntry.get()) + oY
        x = float(eval(ScaleXEntry.get()))
        y = float(eval(ScaleYEntry.get()))

        if x <= 0 or y <= 0:
            raise ValueError

        for i in range(len(Points)):
            for j in range(len(Points[i])):
                if j % 2 == 0:
                    old_x = Points[i][j]
                    Points[i][j] = old_x * x + (1 - x) * xPoint
                else:
                    old_y = Points[i][j]
                    Points[i][j] = old_y * y + (1 - y) * yPoint
            canvas.delete('all')

        if AxisXYVar.get() == 'ON':
            ShowAxis()
        else:
            Draw()
    except:
        showwarning('Некорректный ввод', 'Ввод был выполнен некорректно. Коэффициенты должны быть больше(>) 0.')


def Back():
    for i in range(len(Points)):
        for j in range(len(Points[i])):
            Points[i][j] = PrevPoints[i][j]
    canvas.delete('all')
    if AxisXYVar.get() == 'ON':
        ShowAxis()
    else:
        Draw()


def ToDefault():
    for i in range(len(Points)):
        for j in range(len(Points[i])):
            Points[i][j] = Default[i][j]
    canvas.delete('all')
    if AxisXYVar.get() == 'ON':
        ShowAxis()
    else:
        Draw()


if __name__ == '__main__':
    root = Tk()
    root.title('Форматирование фигуры')
    root.geometry("1430x800")
    root.resizable(False, False)

    SettingsFrame = Frame(root)
    SettingsFrame.pack(anchor='nw', fill=X, padx=5, pady=5)

    canvasWidth = 1430
    canvasHeight = 700



    oX = canvasWidth/2
    oY = canvasHeight/2

    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)

    AxisXYVar = StringVar()
    AxisXYLabel = Label(SettingsFrame, text='Включить/Выключить\n отображение осей X, Y')
    AxisXYButton = Checkbutton(SettingsFrame, text='Вкл/Выкл', variable=AxisXYVar,
                               onvalue="ON", offvalue="OFF", command=ShowAxis)
    AxisXYLabel.grid(row=0, column=0)
    AxisXYButton.grid(row=1, column=0)

    # Move
    MoveLabel = Label(SettingsFrame, text='Переместить на')
    MoveLabel.grid(row=0, column=3)

    entryXLabel = Label(SettingsFrame, text='   X:')
    entryXLabel.grid(row=1, column=2)
    entryX = Entry(SettingsFrame, width=7)
    entryX.grid(row=1, column=3)

    entryYLabel = Label(SettingsFrame, text='   Y:')
    entryYLabel.grid(row=2, column=2)
    entryY = Entry(SettingsFrame, width=7)
    entryY.grid(row=2, column=3)

    okMove = Button(SettingsFrame, text='Ок', command=Move)
    okMove.grid(row=2, column=4)

    # Rotate
    RotateLabel = Label(SettingsFrame, text='Поворот')
    RotateLabel.grid(row=0, column=7)

    RotateLabelX = Label(SettingsFrame, text='      X:')
    RotateLabelX.grid(row=1, column=6)
    RotateXEntry = Entry(SettingsFrame, width=7)
    RotateXEntry.grid(row=1, column=7)

    RotateLabelY = Label(SettingsFrame, text='      Y:')
    RotateLabelY.grid(row=2, column=6)
    RotateYEntry = Entry(SettingsFrame, width=7)
    RotateYEntry.grid(row=2, column=7)

    RotateLabelAngle = Label(SettingsFrame, text='Угол:')
    RotateLabelAngle.grid(row=1, column=8)
    RotateEntryAngle = Entry(SettingsFrame, width=4)
    RotateEntryAngle.grid(row=1, column=9)

    okRotate = Button(SettingsFrame, text='Ок', command=Rotate)
    okRotate.grid(row=2, column=8)

    # Scale
    ScaleLabel = Label(SettingsFrame, text='Масштабировать')
    ScaleLabel.grid(row=0, column=23)

    ScalePointXLabel = Label(SettingsFrame, text='      X:')
    ScalePointXLabel.grid(row=1, column=21)
    ScalePointXEntry = Entry(SettingsFrame, width=7)
    ScalePointXEntry.grid(row=1, column=22)

    ScalePointYLabel = Label(SettingsFrame, text='      Y:')
    ScalePointYLabel.grid(row=2, column=21)
    ScalePointYEntry = Entry(SettingsFrame, width=7)
    ScalePointYEntry.grid(row=2, column=22)

    ScaleXLabel = Label(SettingsFrame, text='Масштабировать на X (коэффициент):')
    ScaleXLabel.grid(row=1, column=23)
    ScaleXEntry = Entry(SettingsFrame, width=7)
    ScaleXEntry.grid(row=1, column=24)

    ScaleYLabel = Label(SettingsFrame, text='Масштабировать на Y (коэффициент):')
    ScaleYLabel.grid(row=2, column=23)
    ScaleYEntry = Entry(SettingsFrame, width=7)
    ScaleYEntry.grid(row=2, column=24)

    okScale = Button(SettingsFrame, text='Ок', command=Scaling)
    okScale.grid(row=2, column=25)

    # TODO Undo button
    undo = Button(SettingsFrame, text='Вернуть на шаг назад', command=Back)
    undo.grid(row=0, column=31)

    returnToDefaults = Button(SettingsFrame, text='Вернуть начальные значения', command=ToDefault)
    returnToDefaults.grid(row=1, column=31)

    Draw()

    canvas.pack()

    root.mainloop()