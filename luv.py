import tkinter as tk

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]
def flames():
    p1 = pe1.get()
    p1 = p1.lower()
    p1.replace(" ", "")
    p1_list = list(p1)
    p2 = pe2.get()
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)
    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left
        else:
            result = result[: len(result) - 1]
    re=tk.Label(root,text=result[0],height=3,width=30,font=('arial',15),bg='#ff6ec7').place(x=70,y=290)

root=tk.Tk()
root.title("FLAMES")
root.resizable(False,False)
root.geometry('480x400')
root.config(bg='#ffc2d1')
i=tk.PhotoImage(file="h.png")
root.iconphoto(False,i)

im=tk.PhotoImage(file="red.png")
im=im.subsample(2,4)
tk.Label(root,image=im,bg='#ffc2d1').pack(pady=30)
l=tk.Label(root,text='Test your love',height=1,width=11,font=('arial',15,'bold'),bg='#ffc2d1').place(x=170,y=50)
tk.Label(root,image=im,bg='#ffc2d1').place(x=15,y=250)
im2=tk.PhotoImage(file="red.png")
im2=im2.subsample(4,6)
tk.Label(root,image=im2,bg='#ffc2d1').place(x=350,y=200)


yn=tk.Label(root,text='Your Name',height=3,width=12,font=('arial',14),bg='#ffc2d1').place(x=20,y=100)
dob=tk.Label(root,text='Partner\'s Name',height=3,width=12,font=('arial',14),bg='#ffc2d1').place(x=30,y=150)

pe1 = tk.StringVar()
pe2 = tk.StringVar()

e1=tk.Entry(root,textvariable=pe1,width=30,bg='#ff6ec7').place(x=180,y=130)
e2=tk.Entry(root,textvariable=pe2,width=30,bg='#ff6ec7').place(x=180,y=180)

b1=tk.Button(root,text='Find Relationship',command=lambda:flames(),font=('arial',12),bg='#b892ff').place(x=160,y=230)
b2=tk.Button(root,text='Exit',command=lambda:root.withdraw(),font=('arial',12),bg='white').place(x=420,y=360)

root.mainloop()
