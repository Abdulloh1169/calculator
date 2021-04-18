# libraries
import tkinter as tk

# constants
dictlist = "1234567890"
dictlist1 = "/*!.+-"
root = tk.Tk()
root.title("calculator")
v = tk.StringVar()
w = tk.StringVar()
style = ("times new romane italic", 14)
style2 = ("elephant", 12)
# ---------------------------------------------------------------------------------
# main funtions
#   v->answer, w->input

num = ''
summ = ''
final = ''


def number(elem):
    global num
    num += elem
    w.set(summ + num)


def summa(sign):
    global summ, num
    summ += num
    num = ''
    summ += sign
    w.set(summ)


def equal():
    w.set("")
    global summ, num
    summ += num
    summ = check(summ)
    try:
        v.set(eval(summ))
        return eval(summ)
    except:
        v.set("ERROR")
    finally:
        num = ''
        summ = ''


def clear():
    global num, summ
    v.set('')
    w.set('')
    num = ''
    summ = ''


def factorial():
    a, su = equal(), 1

    if 100 > a > 0 and a % 1 == 0:
        for i in range(1, a + 1):
            su *= i
        w.set(num)
        v.set(su)
    else:
        clear()
        v.set("ERROR")

def Reverse():
    a = equal()
    clear()
    try: v.set(1/a)
    except ZeroDivisionError:v.set("ZeroDivision")


def check(some):
    if dictlist1.find(some[-1]) != -1:
        some= some[:-1]
    return some


main = lambda x: summa(x.char)
equality = lambda x: equal()
keys = lambda x: number(x.char)
factor = lambda x: factorial()

# ---------------------------------------------------------------------------------
# Abreviations
def button(show, name, work):
    return tk.Button(show, text=name, height=1, width=2,
                     command=work, bg="light grey", font=style2)


def entry(show, variable):
    return tk.Label(show, width=20, textvariable=variable, bg="white")


# frames' feature
frame1 = tk.Frame(root, height=200, width=200)
frame2 = tk.Frame(root, height=200, width=200, padx=5, pady=5)
frame3 = tk.Frame(root, height=150, width=80, pady=10)

'''  frame-1  '''
# ----------------------------------------------------------------------------------
frame1.grid(row=0, column=0, rowspan=5, columnspan=2)

# number enter
label1 = tk.Label(frame1, text="input:", font=style)
label1.grid(row=0, column=0, padx=2, pady=10, sticky='e')
text = entry(frame1, w)
text.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# answer label
anslab = tk.Label(frame1, text="answer:")
anslab.grid(row=1, column=0, sticky='e')
label2 = tk.Label(frame1, textvariable=v, font=style,
                  padx=10, pady=10)
label2.grid(row=1, column=0, columnspan=2)

'''  frame-2  '''
# ----------------------------------------------------------------------------------
frame2.grid(row=6, column=0, rowspan=10)

# buttons
but1 = button(frame2, '1', lambda: number('1'))
but1.grid(row=0, column=0, sticky='e', padx=2, pady=4)
but2 = button(frame2, '2', lambda: number('2'))
but2.grid(row=0, column=1, sticky='w' + 'e', padx=2, pady=4)
but3 = button(frame2, '3', lambda: number('3'))
but3.grid(row=0, column=2, sticky='w' + 'e', padx=2, pady=4)
but4 = button(frame2, '4', lambda: number('4'))
but4.grid(row=1, column=0, sticky='w' + 'e', padx=2, pady=4)
but5 = button(frame2, '5', lambda: number('5'))
but5.grid(row=1, column=1, sticky='w' + 'e', padx=2, pady=4)
but6 = button(frame2, '6', lambda: number('6'))
but6.grid(row=1, column=2, sticky='w' + 'e', padx=2, pady=4)
but7 = button(frame2, '7', lambda: number('7'))
but7.grid(row=2, column=0, sticky='w' + 'e', padx=2, pady=4)
but8 = button(frame2, '8', lambda: number('8'))
but8.grid(row=2, column=1, sticky='w' + 'e', padx=2, pady=4)
but9 = button(frame2, '9', lambda: number('9'))
but9.grid(row=2, column=2, sticky='w' + 'e', padx=2, pady=4)
butsign1 = button(frame2, '+', lambda: summa('+'))
butsign1.grid(row=0, column=3, sticky='w' + 'e', padx=2, pady=4)
butsign2 = button(frame2, '-', lambda: summa('-'))
butsign2.grid(row=1, column=3, sticky='w' + 'e', padx=2, pady=4)
butsign3 = button(frame2, '*', lambda: summa('*'))
butsign3.grid(row=2, column=3, sticky='w' + 'e', padx=2, pady=4)
butsign4 = button(frame2, '/', lambda: summa('/'))
butsign4.grid(row=3, column=3, sticky='w' + 'e', padx=2, pady=4)
butsign5 = button(frame2, '.', lambda: summa('.'))
butsign5.grid(row=3, column=0, sticky='w' + 'e', padx=2, pady=4)
but0 = button(frame2, '0', lambda: number('0'))
but0.grid(row=3, column=1, sticky='w' + 'e', padx=2, pady=4)
butsign7 = button(frame2, '1/x', Reverse)
butsign7.grid(row=3, column=2, sticky='w' + 'e', padx=2, pady=4)

'''   frame-3  '''
frame3.grid(row=6, column=1)

# buttons
butsign6 = button(frame3, '!', factorial)
butsign6.grid(row=0, column=0, sticky='w' + 'e', padx=2, pady=4)
but10 = tk.Button(frame3, text="c", font=style2, height=2, command=clear)
but10.grid(row=1, column=0, sticky='w' + 'e', padx=2, pady=2)
but11 = tk.Button(frame3, text="=", font=style2, height=2, command=equal)
but11.grid(row=2, column=0, sticky='w' + 'e', padx=2, pady=4)
# ----------------------------------------------------------------------------------
# bind function

root.bind_all("<Key-1>",keys)
root.bind_all("<Key-2>",keys)
root.bind_all("<Key-3>",keys)
root.bind_all("<Key-4>",keys)
root.bind_all("<Key-5>",keys)
root.bind_all("<Key-6>",keys)
root.bind_all("<Key-7>",keys)
root.bind_all("<Key-8>",keys)
root.bind_all("<Key-9>",keys)
root.bind_all("<Key-0>",keys)
root.bind_all("<Key-.>", main)
root.bind_all("<Key-+>", main)
root.bind_all("<Key-->", main)
root.bind_all("<Key-*>", main)
root.bind_all("<Key-/>", main)
root.bind_all("<Key-!>", factor)
root.bind_all("<Key-=>", equality)
root.bind_all("<Return>", equality)

root.resizable(False, False)
root.mainloop()




