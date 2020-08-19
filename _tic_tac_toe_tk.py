import tkinter
from tkinter import messagebox


while True:

    check = 1
    representation = [
                      [1,2,3],
                      [4,5,6],
                      [7,8,9]
                     ]

    def center_screen(window_width, window_height):
        import ctypes
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        return (window_width, window_height, (screen_width - window_width) / 2, (screen_height - window_height) / 2)


    def print_message(wlist):
        if wlist[0] == True:
            message = f'\'{wlist[1]}\' WINS'
            messagebox.showinfo("", message)
            answer = messagebox.askyesno('New Game', 'Would you like to play another game?')
            if answer == 1:
                ttt_root.destroy()
            else:
                exit()

        if check == 10 and wlist[0] == False:
            message = 'DRAW'
            messagebox.showinfo("", message)
            answer = messagebox.askyesno('New Game', 'Would you like to play another game?')
            if answer == 1:
                ttt_root.destroy()
            else:
                exit()


    def win_check(ulist):
        # ---------------------- this block checks rows ------------------------
        for nestlist in ulist:
            fcheck = []
            fcheck.append(nestlist[0])
            for i in range(1,len(nestlist)):
                if nestlist[i] == fcheck[0]:
                    fcheck.append(nestlist[i])
                else:
                    pass
            if len(fcheck) == 3:
                return [True, fcheck[0]]

        # ------------- transposes ulist so we can use the same check  ------------
        tlist = [[ulist[i][j] for i in range(len(ulist))] for j in range(len(ulist[0]))]

        # -------------- using first check on the transposed list  -----------------
        for nestlist in tlist:
            fcheck = []
            fcheck.append(nestlist[0])
            for i in range(1,len(nestlist)):
                if nestlist[i] == fcheck[0]:
                    fcheck.append(nestlist[i])
                else:
                    pass
            if len(fcheck) == 3:
                return [True, fcheck[0]]

        # -------------- checks diagonals if dimensions are the same ---------------
        if len(ulist) == len(ulist[0]):
            diagonals = [
                         [ulist[i][i] for i in range(len(ulist))],
                         [ulist[i][len(ulist)-1-i] for i in range(len(ulist))]
                         ]
            for nestlist in diagonals:
                fcheck = []
                fcheck.append(nestlist[0])
                for i in range(1,len(nestlist)):
                    if nestlist[i] == fcheck[0]:
                        fcheck.append(nestlist[i])
                    else:
                        pass
                if len(fcheck) == 3:
                    return [True, fcheck[0]]

        return [False, None]










    def close_window(*args, **kwargs):
        exit()



    def button_00_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_00.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[0][0] = button_text
        print(check)
        print(representation)
        # print(win_check(representation))
        print_message(win_check(representation))


    def button_01_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_01.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[0][1] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_02_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_02.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[0][2] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_10_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_10.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[1][0] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_11_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_11.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[1][1] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_12_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_12.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[1][2] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_20_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_20.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[2][0] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_21_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_21.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[2][1] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))

    def button_22_click():
        global check
        global representation
        if check % 2 != 0:
            button_text = 'X'
        elif check % 2 == 0:
            button_text = 'O'
        button_22.config(text=button_text, font=('Helvetica', '65', 'bold'), state='disabled')
        check += 1
        representation[2][2] = button_text
        print(check)
        print(representation)
        print_message(win_check(representation))


    ttt_root = tkinter.Tk()

    ttt_root_width = 300
    ttt_root_height = 300

    ttt_root.geometry('%dx%d+%d+%d' %  center_screen(ttt_root_width, ttt_root_height))
    ttt_root.protocol('WM_DELETE_WINDOW', close_window)  # root is your root window
    ttt_root.bind("<KeyPress-Escape>", close_window)
    ttt_root.title('Tic Tac Toe Game')
    ttt_root.configure(background='lightblue')



    button_color = 'gray85'
    button_borderwidth = 2


    button_00 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_00_click)
    button_00.place(relx = 0, rely = 0, relwidth = 0.3333333, relheight = 0.3333333)

    button_01 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_01_click)
    button_01.place(relx = 0.3333334, rely = 0, relwidth = 0.3333333, relheight = 0.3333333)

    button_02 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_02_click)
    button_02.place(relx = 0.6666667, rely = 0, relwidth = 0.3333333, relheight = 0.3333333)

    button_10 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_10_click)
    button_10.place(relx = 0, rely = 0.3333333, relwidth = 0.3333333, relheight = 0.3333333)

    button_11 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_11_click)
    button_11.place(relx = 0.3333334, rely = 0.3333334, relwidth = 0.3333333, relheight = 0.3333333)

    button_12 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_12_click)
    button_12.place(relx = 0.6666667, rely = 0.3333334, relwidth = 0.3333333, relheight = 0.3333333)

    button_20 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_20_click)
    button_20.place(relx = 0, rely = 0.6666667, relwidth = 0.3333333, relheight = 0.3333333)

    button_21 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_21_click)
    button_21.place(relx = 0.3333334, rely = 0.6666667, relwidth = 0.3333333, relheight = 0.3333333)

    button_22 = tkinter.Button(borderwidth=button_borderwidth, bg=button_color, command=button_22_click)
    button_22.place(relx = 0.6666667, rely = 0.6666667, relwidth = 0.3333333, relheight = 0.3333333)



    ttt_root.mainloop()
