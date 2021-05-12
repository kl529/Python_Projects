import random
import tkinter as tk
from tkinter import *
class Reader:
    """defines class for Input View"""
    @staticmethod
    def name(a):
        name_window = Toplevel(a)
        name_label = Label(name_window,text="이름을 적으시오")
        name_label.pack()
        name_entry = Entry(name_window)
        name_entry.pack()
        def finish():
            global name
            name = name_entry.get()
            name_window.destroy()
            name_window.quit()
        name_button = Button(name_window,text = "제출", command=finish)
        name_button.pack()
        name_window.mainloop()
        return name
    # 추후 GUI의 entry로 바꾸어야 함

    @staticmethod
    def panmoney(playermoney, computermoney,a):
        panmoney_window = Toplevel(a)
        money_label = Label(panmoney_window, text = "판돈을 적으시오\n판돈(판돈의 7배가 양측의 소지금보다 작게 해주세요.) : ")
        money_label.pack()
        money_entry = Entry(panmoney_window)
        money_entry.pack()
        def finish():
            global money
            money = money_entry.get()
            panmoney_window.destroy()
            panmoney_window.quit()
        money_button = Button(panmoney_window,text = "제출",command = finish)
        money_button.pack()
        panmoney_window.mainloop()
        return int(money)

    @staticmethod
    def init_money(a):
        init_window = Toplevel(a)
        init_label = Label(init_window,text = "처음 돈을 입력하세요")
        init_label.pack()
        init_entry = Entry(init_window)
        init_entry.pack()
        def finish():
            global money
            money = init_entry.get()
            init_window.destroy()
            init_window.quit()
        init_button = Button(init_window,text = "제출",command = finish)
        init_button.pack()
        init_window.mainloop()
        return int(money)

    @staticmethod
    def go(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="고?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b
    # 추후 GUI의 Button으로 바꾸어야 함

    @staticmethod
    def push(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="밀기 하시겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b
    # 추후 GUI의 Button으로 바꾸어야 함

    @staticmethod
    def again(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="한번더 ?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        push_window.mainloop()
        
        return b
    # 추후 GUI의 Button으로 바꾸어야 함

    @staticmethod
    def shake(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="흔들겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b
    # 추후 GUI의 Button으로 바꾸어야 함

    @staticmethod
    def choose(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="쌍피열끗 처리하시오")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b= False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "열끗",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "쌍피",command = no)
        push_no.pack()
        push_window.mainloop()
        
        return b
    # 추후 GUI의 Button으로 바꾸어야 함

    @staticmethod
    def save(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="현재상태를 저장하시겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b
    @staticmethod
    def save_num(a):
        lod_window = Toplevel(a)
        def submit():
            global z
            z = lod_entry.get()
            if ( z.isdigit() and not 1<=int(z)<=5):
                z = lod_entry.get()
            else :
                lod_window.destroy()
                lod_window.quit()

        lod_label = Label(lod_window)
        lod_label['text'] = "몇번째 슬롯에 저장하시겠습니까 (1~5) : "
        lod_label.pack()
        lod_entry = Entry(lod_window,bd=3)
        lod_entry.pack()
        lod_btn = Button(lod_window,text='제출',command=submit)
        lod_btn.pack()
        lod_window.mainloop()
        return int(z)

    @staticmethod
    def load(a):
        lod_window = Toplevel(a)
        def lo_yes():
            global b
            b = True
            lod_window.destroy()
            lod_window.quit()
        def lo_no():
            global b
            b = False
            lod_window.destroy()
            lod_window.quit()
        lod_label = Label(lod_window)
        lod_label['text'] = "저장된 상태를 불러오시겠습니까?"
        lod_label.pack()
        lod_yes = Button(lod_window,text = "yes",command = lo_yes)
        lod_yes.pack()
        lod_no = Button(lod_window,text = "no",command = lo_no)
        lod_no['command'] = lo_no
        lod_no.pack()
        lod_window.mainloop()
        return b

    @staticmethod
    def load_num(a):
        lod_window = Toplevel(a)
        def submit():
            global z
            z = lod_entry.get()
            if ( z.isdigit() and not 1<=int(z)<=5):
                z = lod_entry.get()
            else :
                lod_window.destroy()
                lod_window.quit()

        lod_label = Label(lod_window)
        lod_label['text'] = "몇번째 슬롯을 불러오시겠습니까? (1~5) : "
        lod_label.pack()
        lod_entry = Entry(lod_window,bd=3)
        lod_entry.pack()
        lod_btn = Button(lod_window,text='제출',command=submit)
        lod_btn.pack()
        lod_window.mainloop()
        return int(z)

    @staticmethod
    def re_check(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="이미 저장된 세이브 파일에 덮어쓰기됩니다.")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        push_window.mainloop()
        return b
    @staticmethod
    def cardchoose(number,a):
        cc_window = Toplevel(a)
        cc_window.geometry('400x60')
        choose_btn = ['','','','','','','','','','']
        def selectnum0():
            global b
            b = 0
            cc_window.destroy()
            cc_window.quit()
        def selectnum1():
            global b
            b = 1
            cc_window.destroy()
            cc_window.quit()
        def selectnum2():
            global b
            b = 2
            cc_window.destroy()
            cc_window.quit()
        def selectnum3():
            global b
            b = 3
            cc_window.destroy()
            cc_window.quit()
        def selectnum4():
            global b
            b = 4
            cc_window.destroy()
            cc_window.quit()
        def selectnum5():
            global b
            b = 5
            cc_window.destroy()
            cc_window.quit()
        def selectnum6():
            global b
            b = 6
            cc_window.destroy()
            cc_window.quit()
        def selectnum7():
            global b
            b = 7
            cc_window.destroy()
            cc_window.quit()
        def selectnum8():
            global b
            b = 8
            cc_window.destroy()
            cc_window.quit()
        def selectnum9():
            global b
            b = 9
            cc_window.destroy()
            cc_window.quit()
        choose_btn[0] = Button(cc_window,text = str(1)+"번째",command = selectnum0)
        choose_btn[1] = Button(cc_window,text = str(2)+"번째",command = selectnum1)
        choose_btn[2] = Button(cc_window,text = str(3)+"번째",command = selectnum2)
        choose_btn[3] = Button(cc_window,text = str(4)+"번째",command = selectnum3)
        choose_btn[4] = Button(cc_window,text = str(5)+"번째",command = selectnum4)
        choose_btn[5] = Button(cc_window,text = str(6)+"번째",command = selectnum5)
        choose_btn[6] = Button(cc_window,text = str(7)+"번째",command = selectnum6)
        choose_btn[7] = Button(cc_window,text = str(8)+"번째",command = selectnum7)
        choose_btn[8] = Button(cc_window,text = str(9)+"번째",command = selectnum8)
        choose_btn[9] = Button(cc_window,text = str(10)+"번째",command = selectnum9)
        for i in range(len(number)):
            choose_btn[i].place(x = 3 + i*35, y= 0)
        cc_window.mainloop()
        return int(b+1)
    # 추후 GUI의 Button으로 바꾸어야 함   

    @staticmethod
    def ai(a):
        ai_window = Toplevel(a)
        ai_label = Label(ai_window, text="난이도를 고르세요. Easy/Normal/Hard/Hell/Impossible : ")
        ai_label.pack()
        def easy():
            global b
            b = 'easy'
            ai_window.destroy()
            ai_window.quit()
        def normal():
            global b
            b = 'normal'
            ai_window.destroy()
            ai_window.quit()
        def hard():
            global b
            b = 'hard'
            ai_window.destroy()
            ai_window.quit()
        def hell():
            global b
            b = 'hell'
            ai_window.destroy()
            ai_window.quit()
        def impossible():
            global b
            b = 'impossible'
            ai_window.destroy()
            ai_window.quit()
        ai_button1 = Button(ai_window,text = "easy",command = easy)
        ai_button2 = Button(ai_window,text = "normal",command = normal)
        ai_button3 = Button(ai_window,text = "hard",command = hard)
        ai_button4 = Button(ai_window,text = "hell",command = hell)
        ai_button5 = Button(ai_window,text = "impossible",command = impossible)
        ai_button1.pack()
        ai_button2.pack()
        ai_button3.pack()
        ai_button4.pack()
        ai_button5.pack()
        ai_window.mainloop()
        return b
       
    @staticmethod
    def card_choose(obj):
        if obj.name=="Computer":
            return random.randrange(2)
        else :
            push_window = Toplevel()
            push_label = Label(push_window,text ="어떤것을 드시겠습니까 ?")
            push_label.pack()
            def yes():
                global b
                b = 0
                push_window.destroy()
                push_window.quit()
            def no():
                global b
                b= 1
                push_window.destroy()
                push_window.quit()
            push_yes = Button(push_window,text = "첫번째",command = yes)
            push_yes.pack()
            push_no = Button(push_window,text = "두번째",command = no)
            push_no.pack()
            push_window.mainloop()
        
            return int(b)
        
        
# 1. Easy 알고리즘
# 종류에 상관하지 않고 패의 첫번째 부터 탐색하여 맞는 카드가 있으면 무조건 냄. 없을 시 랜덤으로 아무거나(종류 상관하지 않음)
# 고/스톱 시 무조건 스톱
# 2. Normal 알고리즘
# 광 > 고도리 > (뻑) > 열끗(쌍피열끗) > 홍단 = 청단 = 초단 > 단 > 쌍피 > 피 순의 우선순위 부여. (랜덤으로 낼 때는 반대로 적용)
# 상황을 고려하지 않음. 고/스톱 시 플레이어가 2점 이상일 시 무조건 스톱. 뻑을 딸 수 있으면 바로 땀(단, 플레이어가 피가 있을 때)
# 3. Hard 알고리즘
# 플레이어와 컴퓨터의 획득한 카드를 보고 판단하여 우선순위를 일시 변경하는 능력 부여 (광은 그대로)
# 고/스톱 시 플레이어가 4점 이상일 시(단, 플레이어의 카드 고려) 스톱. 뻑을 딸 수 있어도 나중에 땀
# 4. Hell 알고리즘
# 덱을 투시하게 됨. 100퍼센트 확률로 따닥, 쪽, 자뻑, 싹쓸 가능
# 5. impossible 알고리즘
# 플레이어의 패를 투시하게 됨. 플레이어가 먹을 수 있는 카드를 우선으로 봉쇄함.