import tkinter

jendela = tkinter.Tk()

LabelAnggurr = tkinter.Label (jendela, text = "Anggur", fg = "white", bg = "violet")
LabelApel = tkinter.Label (jendela, text = "Apel", fg = "white", bg = "red")
LabelMelon = tkinter.Label (jendela, text = "Melon", fg = "white", bg = "green")


LabelAnggurr.pack()
LabelApel.pack(ipadx = 20, ipady = 10)
LabelMelon.pack()

jendela.mainloop()