import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Welcome to Hnnu_web")
window.geometry("1200x650")
#welcome Hnnu image
canvas=tk.Canvas(window,height=354,width=1338)
image_file=tk.PhotoImage(file="E:\\computer code\\tkinter练习—登录系统\\welcome.png")
image=canvas.create_image(0,0,anchor="nw",image=image_file)
canvas.pack(side="top")

#用户名和密码的输入
tk.Label(window,text="学生账号：",font=("Arial",20)).place(x=450,y=450)
tk.Label(window,text="学生密码：",font=("Arial",20)).place(x=450,y=490)
var_user_account=tk.StringVar()
var_user_account.set("example@hunnu.com")
tk.Entry(window,textvariable=var_user_account,font=("Arial",20)).place(x=600,y=460,height=30)
var_user_password=tk.StringVar()
tk.Entry(window,textvariable=var_user_password,show="*",font=("Arial",20)).place(x=600,y=500,height=30)
user_dict={}
#登入和注册
#————————————————————————————————————————————————————————————————————————
#登入函数
def user_login():
    user_name=var_user_account.get()
    user_psd=var_user_password.get()
    if not user_name or not user_psd:
        messagebox.showerror("提示", "账号密码不能为空！")
        return
    if user_name not in user_dict:
        messagebox.showerror("提示", "账号不存在，请先注册！")
    elif user_dict[user_name] == user_psd:
        messagebox.showinfo("成功","登录成功！"+"你好"+user_name)
    else:
        messagebox.showerror("提示", "密码错误！")
#—————————————————————————————————————————————————————————————————————————
#注册函数
def user_sign_up(): 
    def sign_to_Mofan_Python():
        global user_dict
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        if np != npf:
            tk.messagebox.showerror('错误', '两次密码必须保持一致！')
        elif nn in user_dict.items():
            tk.messagebox.showerror('错误', '此用户名已经被占用!')
        else:
            user_dict[nn] = np
            tk.messagebox.showinfo('欢迎', '你已经成功注册了!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@hunnu.com')
    tk.Label(window_sign_up, text='学生账号: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='学生密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='确认密码: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)
#————————————————————————————————————————————————————————————————
#登入注册按钮
login=tk.Button(window,text="登录账号",font=("宋体",20),command=user_login)
login.place(x=460,y=550)
sign_up=tk.Button(window,text="注册账号",font=("宋体",20),command=user_sign_up)
sign_up.place(x=660,y=550)
window.mainloop()