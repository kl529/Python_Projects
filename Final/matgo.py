from matgohand import *
from matgoai import *
from matgocard import *
from matgoview import *
from matgofield import *
from matgoturn import *
from matgoscore import *
from tkinter import *
import tkinter as tk
import random
import time
class MatgoController:
    def __init__(self, name, ai, nagari, playermoney, computermoney):
        self.__ai=AI(ai)
        self.__player = got(name)
        self.__computer = got("Computer")
        self.__deck = Deck()
        self.__mulitple = 1 # 배율
        self.__field=[[], [], [], [], [], [], [], [], [], [], [], []]
        self.__first=random.randrange(2) # 0=플레이어 선공, 1=컴퓨터 선공
        self.__was_playerscore=0
        self.__was_computerscore=0
        self.__nagari=nagari
        self.__playermoney=playermoney
        self.__computermoney=computermoney
        #   1 2 3 4
        # 9 10 덱 11 12
        #   5 6 7 8
    def nagari(self):
        self.__nagari+=1
    def play(self,a): # 판돈*score, 누가 이겼는지 return
        if self.__nagari==0:
            self.__panmoney=Reader.panmoney(self.__playermoney, self.__computermoney,root)
        self.__panmoney=self.__panmoney*2**(self.__nagari)
        deck = self.__deck
        play_window = Toplevel(a)
        new_label = Label(play_window,text = "새로운 게임을 시작합니다.")
        new_label.pack()
        def finish():
            play_window.destroy()
            play_window.quit()
        new_quitbut = Button(play_window,text= "종료", command =finish)
        if self.__first==0:
            firstattack = Label(play_window, text = "플레이어가 선공합니다.")
            firstattack.pack()
        if self.__first==1:
            firstattack = Label(play_window, text = "컴퓨터가 선공합니다.")
            firstattack.pack()
        new_quitbut.pack()
        play_window.mainloop()

        player = self.__player
        computer = self.__computer
        player_4cards=False
        computer_4cards=False
        for _ in range(5):
            player.get(deck.next())
        for _ in range(5):
            computer.get(deck.next(open=False))
        for _ in range(5):
            player.get(deck.next())
        for _ in range(5):
            computer.get(deck.next(open=False))

        player.hand_set(player.sequence_arrange())
        computer.hand_set(computer.sequence_arrange())

        for i in range(8):
            self.__field[i].append(deck.next())
        
        for i in range(8):
            for k in range(8):
                if i!=k and self.__field[i]!=[] and self.__field[k]!=[] and self.__field[i][0].month==self.__field[k][0].month:
                    self.__field[i].append(self.__field[k].pop())
        
        #self.printscreen()

        # 총통인 경우
        for i in range(12): # 총통인 4개의 카드를 GUI로 출력해야 함
            if len(player.month_arrange()[i])==4:
                player_4cards=True
            if len(computer.month_arrange()[i])==4:
                computer_4cards=True
        for i in range(8): # 필드에 총통
            if len(self.__field[i])==4:
                if self.__first==0:
                    if computer_4cards == 'True':
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "양쪽총통!")
                        chongtong_label.pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop
                        return ["double"]
                    else:
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
                        chongtong_label.pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop
                        return ["player", 10*self.__panmoney]
                else:
                    if player_4cards:
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "양측 총통!")
                        chongtong_label.pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop
                        return ["double"]
                    else:
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
                        chongtong_label.pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop
                        return ["computer", 10*self.__panmoney]
        if player_4cards and not computer_4cards:
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
            chongtong_label.pack()
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop
            return ["player", 10*self.__panmoney]
        elif not player_4cards and computer_4cards:
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
            chongtong_label.pack()
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop
            return ["computer", 10*self.__panmoney]
        elif player_4cards and computer_4cards:
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "양측 총통!")
            chongtong_label.pack()
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop
            return ["double"]
        else: # 게임 시작
            img_field = PhotoImage(file = "./img_matgo/Field.png")
            x = Label(image = img_field)
            x.place(x =0, y=0)
            ph =[]
            ch =[]
            plhand_img = []
            comhand_img = []
            for i in range(len(player.hand)):
                print(i)
                plhand_img.append(PhotoImage(file = "./img_matgo/"+player.hand[i].img()))
                ph.append(Label(image = plhand_img[i]))
                ph[i].place(x=3+(i)*40,y=391)
                comhand_img.append(PhotoImage(file = "./img_matgo/"+"뒤집은거.png"))
                ch.append(Label(image = comhand_img[i]))
                ch[i].place(x=3+(i)*40,y=5)
                    
                    
            fd =[[],[],[],[],[],[],[],[],[],[],[],[]]
            fdhand_img = [[],[],[],[],[],[],[],[],[],[],[],[]]
            cnt= 0
            a_cnt=0
            for i in self.__field:
                for j in range(len(i)):
                    fdhand_img[cnt].append(PhotoImage(file = "./img_matgo/"+i[j].img()))
                    fd[cnt].append(Label(image = fdhand_img[cnt][j]))                
                    fd[cnt][j].place(x= 15+cnt*45+5*j -a_cnt*45, y=170+5*j)
                cnt+=1
            for _ in range(10):

                if self.__first==0: # 플레이어 선공
                    # time.sleep(1)
                    self.__field = Turn.playerturn(player, computer, self.__field, self.__deck,a)
                    #self.printscreen()
                    if player.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="플레이어 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["player", 10*self.__panmoney]
                    if len(player.hand)==0:
                        if player.score>=7 and player_score_last < player.score:
                            self.__multiple=Score(player).multiple(computer)
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="플레이어 승리 !")
                            win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    check = Turn.player_go_stop(player,root)
                    # check = Turn.computer_go_stop(player, computer, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(player).multiple(computer)
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="플레이어 승리 !")
                        win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    time.sleep(1)
                    
                    self.__field = Turn.computerturn(player, computer, self.__field, self.__deck, self.__ai)
                    img_field = PhotoImage(file = "./img_matgo/Field.png")
                    x = Label(image = img_field)
                    x.place(x =0, y=0)
                    ph =[]
                    ch =[]
                    plhand_img = []
                    comhand_img = []
                    for i in range(len(player.hand)):
                        print(i)
                        plhand_img.append(PhotoImage(file = "./img_matgo/"+player.hand[i].img()))
                        ph.append(Label(image = plhand_img[i]))
                        ph[i].place(x=3+(i)*40,y=391)
                        comhand_img.append(PhotoImage(file = "./img_matgo/"+"뒤집은거.png"))
                        ch.append(Label(image = comhand_img[i]))
                        ch[i].place(x=3+(i)*40,y=5)
                    
                    
                    fd =[[],[],[],[],[],[],[],[],[],[],[],[]]
                    fdhand_img = [[],[],[],[],[],[],[],[],[],[],[],[]]
                    cnt= 0
                    a_cnt=0
                    for i in self.__field:
                        for j in range(len(i)):
                            fdhand_img[cnt].append(PhotoImage(file = "./img_matgo/"+i[j].img()))
                            fd[cnt].append(Label(image = fdhand_img[cnt][j]))                
                            fd[cnt][j].place(x= 15+cnt*45+5*j -a_cnt*45, y=170+5*j)
                        cnt+=1
                    gotgwang_img = []
                    gotgwang = []
                    for i in range(len(self.__player.gwang)):
                        gotgwang_img.append(PhotoImage(file = "./img_matgo/"+self.__player.gwang[i].img()))
                        gotgwang.append(Label(image = gotgwang_img[i]))
                        gotgwang[i].place(x= 15+i*11, y=320)
                    gotbeegwang_img = []
                    gotbeegwang = []
                    for i in range(len(self.__player.beegwang)):
                        gotbeegwang_img.append(PhotoImage(file = "./img_matgo/"+self.__player.beegwang[i].img()))
                        gotbeegwang.append(Label(image = gotbeegwang_img[i]))
                        gotbeegwang[i].place(x= 15+i*11 + 10*(len(self.__player.gwang)), y=320)
                    gotreddan_img = []
                    gotreddan = []
                    for i in range(len(self.__player.reddan)):
                        gotreddan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.reddan[i].img()))
                        gotreddan.append(Label(image = gotreddan_img[i]))
                        gotreddan[i].place(x= 80+i*11, y=320)
                    gotbluedan_img = []
                    gotbluedan = []
                    for i in range(len(self.__player.bluedan)):
                        gotbluedan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.bluedan[i].img()))
                        gotbluedan.append(Label(image = gotbluedan_img[i]))
                        gotbluedan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 , y=320)
                    gotchodan_img = []
                    gotchodan = []
                    for i in range(len(self.__player.chodan)):
                        gotchodan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.chodan[i].img()))
                        gotchodan.append(Label(image = gotchodan_img[i]))
                        gotchodan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 + (len(self.__player.bluedan))*11 , y=320)
                    gotdan_img = []
                    gotdan = []
                    for i in range(len(self.__player.dan)):
                        gotdan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.dan[i].img()))
                        gotdan.append(Label(image = gotdan_img[i]))
                        gotdan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 + (len(self.__player.bluedan))*11 +(len(self.__player.chodan))*11 , y=320)
                    gotgodori_img = []
                    gotgodori = []
                    for i in range(len(self.__player.godori)):
                        gotgodori_img.append(PhotoImage(file = "./img_matgo/"+self.__player.godori[i].img()))
                        gotgodori.append(Label(image = gotgodori_img[i]))
                        gotgodori[i].place(x= 190+i*11, y=320)
                    gotanimal_img = []
                    gotanimal = []
                    for i in range(len(self.__player.animal)):
                        gotanimal_img.append(PhotoImage(file = "./img_matgo/"+self.__player.animal[i].img()))
                        gotanimal.append(Label(image = gotanimal_img[i]))
                        gotanimal[i].place(x= 190+i*11 + len(self.__player.godori)*11, y=320)
                    gotpee_img = []
                    gotpee = []
                    for i in range(len(self.__player.pee)):
                        gotpee_img.append(PhotoImage(file = "./img_matgo/"+self.__player.pee[i].img()))
                        gotpee.append(Label(image = gotpee_img[i]))
                        gotpee[i].place(x= 300+i*11, y=320)
                    gotdoublepee_img = []
                    gotdoublepee = []
                    for i in range(len(self.__player.doublepee)):
                        gotdoublepee_img.append(PhotoImage(file = "./img_matgo/"+self.__player.doublepee[i].img()))
                        gotdoublepee.append(Label(image = gotdoublepee_img[i]))
                        gotdoublepee[i].place(x= 300+i*11+ 10*len(self.__player.pee), y=320)
                    playerfuck = Label(a,text = "뻑 갯수 : "+str(player.fuck_display))
                    playerfuck.place(x= 430, y= 380)
                    playerscore = Label(a,text = "점수 : "+str(player.score))
                    playerscore.place(x=430,y=400)
                    playershake = Label(a,text = "흔들기 : " + str(player.shake_display))
                    playershake.place(x=430,y=420)
                    computerfuck = Label(a,text = "뻑 갯수 : "+str(computer.fuck_display))
                    computerfuck.place(x= 430, y= 10)
                    computerscore = Label(a,text = "점수 : "+str(computer.score))
                    computerscore.place(x=430,y=30)
                    computershake = Label(a,text = "흔들기 : " + str(computer.shake_display))
                    computershake.place(x=430,y=50)
                    playergo = Label(a,text = "고 : " + str(player.go_display))
                    playergo.place(x = 430, y=440)
                    computergo = Label(a,text="고 :" +str(computer.go_display))
                    computergo.place(x=430,y=70)
                    c_gotgwang_img = []
                    c_gotgwang = []
                    for i in range(len(self.__computer.gwang)):
                        c_gotgwang_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.gwang[i].img()))
                        c_gotgwang.append(Label(image = c_gotgwang_img[i]))
                        c_gotgwang[i].place(x= 15+i*11, y=80)
                    c_gotbeegwang_img = []
                    c_gotbeegwang = []
                    for i in range(len(self.__computer.beegwang)):
                        c_gotbeegwang_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.beegwang[i].img()))
                        c_gotbeegwang.append(Label(image = c_gotbeegwang_img[i]))
                        c_gotbeegwang[i].place(x= 15+i*11 + 10*(len(self.__computer.gwang)), y=80)
                    c_gotreddan_img = []
                    c_gotreddan = []
                    for i in range(len(self.__computer.reddan)):
                        c_gotreddan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.reddan[i].img()))
                        c_gotreddan.append(Label(image = c_gotreddan_img[i]))
                        c_gotreddan[i].place(x= 80+i*11, y=80)
                    c_gotbluedan_img = []
                    c_gotbluedan = []
                    for i in range(len(self.__computer.bluedan)):
                        c_gotbluedan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.bluedan[i].img()))
                        c_gotbluedan.append(Label(image = c_gotbluedan_img[i]))
                        c_gotbluedan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 , y=80)
                    c_gotchodan_img = []
                    c_gotchodan = []
                    for i in range(len(self.__computer.chodan)):
                        c_gotchodan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.chodan[i].img()))
                        c_gotchodan.append(Label(image = c_gotchodan_img[i]))
                        c_gotchodan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 + (len(self.__computer.bluedan))*11 , y=80)
                    c_gotdan_img = []
                    c_gotdan = []
                    for i in range(len(self.__computer.dan)):
                        c_gotdan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.dan[i].img()))
                        c_gotdan.append(Label(image = c_gotdan_img[i]))
                        c_gotdan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 + (len(self.__computer.bluedan))*11 +(len(self.__computer.chodan))*11 , y=80)
                    c_gotgodori_img = []
                    c_gotgodori = []
                    for i in range(len(self.__computer.godori)):
                        c_gotgodori_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.godori[i].img()))
                        c_gotgodori.append(Label(image = c_gotgodori_img[i]))
                        c_gotgodori[i].place(x= 190+i*11, y=80)
                    c_gotanimal_img = []
                    c_gotanimal = []
                    for i in range(len(self.__computer.animal)):
                        c_gotanimal_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.animal[i].img()))
                        c_gotanimal.append(Label(image = c_gotanimal_img[i]))
                        c_gotanimal[i].place(x= 190+i*11 + len(self.__computer.godori)*11, y=80)
                    c_gotpee_img = []
                    c_gotpee = []
                    for i in range(len(self.__computer.pee)):
                        c_gotpee_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.pee[i].img()))
                        c_gotpee.append(Label(image = c_gotpee_img[i]))
                        c_gotpee[i].place(x= 300+i*11, y=80)
                    c_gotdoublepee_img = []
                    c_gotdoublepee = []
                    for i in range(len(self.__computer.doublepee)):
                        c_gotdoublepee_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.doublepee[i].img()))
                        c_gotdoublepee.append(Label(image = c_gotdoublepee_img[i]))
                        c_gotdoublepee[i].place(x= 300+i*11+ 10*len(self.__computer.pee), y=80)
                    
                    #self.printscreen()
                    if computer.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="컴퓨터 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["computer", 10*self.__panmoney]
                    if len(computer.hand)==0:
                        if computer.score>=7 and computer_score_last < computer.score:
                            self.__multiple=Score(computer).multiple(player)
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="컴퓨터 승리 !")
                            win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                        else:
                            nagari_window = Toplevel(a)
                            nagari_label = Label(nagari_window,text="나가리입니다")
                            nagari_label.pack()
                            def finish():
                                nagari_window.destroy()
                                nagari_window.quit()
                            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
                            nagari_btn.pack()
                            nagari_window.mainloop()
                            return ["nagari"]
                    check = Turn.computer_go_stop(computer, player, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(computer).multiple(player)
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="컴퓨터 승리 !")
                        win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    player_score_last=player.score
                    computer_score_last=computer.score
                    
                else: # 컴퓨터 선공
                    time.sleep(1)
                    self.__field = Turn.computerturn(player, computer, self.__field, self.__deck, self.__ai)
                    img_field = PhotoImage(file = "./img_matgo/Field.png")
                    x = Label(image = img_field)
                    x.place(x =0, y=0)
                    ph =[]
                    ch =[]
                    plhand_img = []
                    comhand_img = []
                    for i in range(len(player.hand)):
                        print(i)
                        plhand_img.append(PhotoImage(file = "./img_matgo/"+player.hand[i].img()))
                        ph.append(Label(image = plhand_img[i]))
                        ph[i].place(x=3+(i)*40,y=391)
                    for i in range(len(computer.hand)):
                        comhand_img.append(PhotoImage(file = "./img_matgo/"+"뒤집은거.png"))
                        ch.append(Label(image = comhand_img[i]))
                        ch[i].place(x=3+(i)*40,y=5)
                    
                    
                    fd =[[],[],[],[],[],[],[],[],[],[],[],[]]
                    fdhand_img = [[],[],[],[],[],[],[],[],[],[],[],[]]
                    cnt= 0
                    a_cnt=0
                    for i in self.__field:
                        for j in range(len(i)):
                            fdhand_img[cnt].append(PhotoImage(file = "./img_matgo/"+i[j].img()))
                            fd[cnt].append(Label(image = fdhand_img[cnt][j]))                
                            fd[cnt][j].place(x= 15+cnt*45+5*j -a_cnt*45, y=170+5*j)
                        cnt+=1
                    c_gotgwang_img = []
                    c_gotgwang = []
                    for i in range(len(self.__computer.gwang)):
                        c_gotgwang_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.gwang[i].img()))
                        c_gotgwang.append(Label(image = c_gotgwang_img[i]))
                        c_gotgwang[i].place(x= 15+i*11, y=80)
                    c_gotbeegwang_img = []
                    c_gotbeegwang = []
                    for i in range(len(self.__computer.beegwang)):
                        c_gotbeegwang_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.beegwang[i].img()))
                        c_gotbeegwang.append(Label(image = c_gotbeegwang_img[i]))
                        c_gotbeegwang[i].place(x= 15+i*11 + 10*(len(self.__computer.gwang)), y=80)
                    c_gotreddan_img = []
                    c_gotreddan = []
                    for i in range(len(self.__computer.reddan)):
                        c_gotreddan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.reddan[i].img()))
                        c_gotreddan.append(Label(image = c_gotreddan_img[i]))
                        c_gotreddan[i].place(x= 80+i*11, y=80)
                    c_gotbluedan_img = []
                    c_gotbluedan = []
                    for i in range(len(self.__computer.bluedan)):
                        c_gotbluedan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.bluedan[i].img()))
                        c_gotbluedan.append(Label(image = c_gotbluedan_img[i]))
                        c_gotbluedan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 , y=80)
                    c_gotchodan_img = []
                    c_gotchodan = []
                    for i in range(len(self.__computer.chodan)):
                        c_gotchodan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.chodan[i].img()))
                        c_gotchodan.append(Label(image = c_gotchodan_img[i]))
                        c_gotchodan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 + (len(self.__computer.bluedan))*11 , y=80)
                    c_gotdan_img = []
                    c_gotdan = []
                    for i in range(len(self.__computer.dan)):
                        c_gotdan_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.dan[i].img()))
                        c_gotdan.append(Label(image = c_gotdan_img[i]))
                        c_gotdan[i].place(x= 80+i*11 +(len(self.__computer.reddan))*11 + (len(self.__computer.bluedan))*11 +(len(self.__computer.chodan))*11 , y=80)
                    c_gotgodori_img = []
                    c_gotgodori = []
                    for i in range(len(self.__computer.godori)):
                        c_gotgodori_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.godori[i].img()))
                        c_gotgodori.append(Label(image = c_gotgodori_img[i]))
                        c_gotgodori[i].place(x= 190+i*11, y=80)
                    c_gotanimal_img = []
                    c_gotanimal = []
                    for i in range(len(self.__computer.animal)):
                        c_gotanimal_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.animal[i].img()))
                        c_gotanimal.append(Label(image = c_gotanimal_img[i]))
                        c_gotanimal[i].place(x= 190+i*11 + len(self.__computer.godori)*11, y=80)
                    c_gotpee_img = []
                    c_gotpee = []
                    for i in range(len(self.__computer.pee)):
                        c_gotpee_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.pee[i].img()))
                        c_gotpee.append(Label(image = c_gotpee_img[i]))
                        c_gotpee[i].place(x= 300+i*11, y=80)
                    c_gotdoublepee_img = []
                    c_gotdoublepee = []
                    for i in range(len(self.__computer.doublepee)):
                        c_gotdoublepee_img.append(PhotoImage(file = "./img_matgo/"+self.__computer.doublepee[i].img()))
                        c_gotdoublepee.append(Label(image = c_gotdoublepee_img[i]))
                        c_gotdoublepee[i].place(x= 300+i*11+ 10*len(self.__computer.pee), y=80)
                    gotgwang_img = []
                    gotgwang = []
                    for i in range(len(self.__player.gwang)):
                        gotgwang_img.append(PhotoImage(file = "./img_matgo/"+self.__player.gwang[i].img()))
                        gotgwang.append(Label(image = gotgwang_img[i]))
                        gotgwang[i].place(x= 15+i*11, y=320)
                    gotbeegwang_img = []
                    gotbeegwang = []
                    for i in range(len(self.__player.beegwang)):
                        gotbeegwang_img.append(PhotoImage(file = "./img_matgo/"+self.__player.beegwang[i].img()))
                        gotbeegwang.append(Label(image = gotbeegwang_img[i]))
                        gotbeegwang[i].place(x= 15+i*11 + 10*(len(self.__player.gwang)), y=320)
                    gotreddan_img = []
                    gotreddan = []
                    for i in range(len(self.__player.reddan)):
                        gotreddan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.reddan[i].img()))
                        gotreddan.append(Label(image = gotreddan_img[i]))
                        gotreddan[i].place(x= 80+i*11, y=320)
                    gotbluedan_img = []
                    gotbluedan = []
                    for i in range(len(self.__player.bluedan)):
                        gotbluedan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.bluedan[i].img()))
                        gotbluedan.append(Label(image = gotbluedan_img[i]))
                        gotbluedan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 , y=320)
                    gotchodan_img = []
                    gotchodan = []
                    for i in range(len(self.__player.chodan)):
                        gotchodan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.chodan[i].img()))
                        gotchodan.append(Label(image = gotchodan_img[i]))
                        gotchodan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 + (len(self.__player.bluedan))*11 , y=320)
                    gotdan_img = []
                    gotdan = []
                    for i in range(len(self.__player.dan)):
                        gotdan_img.append(PhotoImage(file = "./img_matgo/"+self.__player.dan[i].img()))
                        gotdan.append(Label(image = gotdan_img[i]))
                        gotdan[i].place(x= 80+i*11 +(len(self.__player.reddan))*11 + (len(self.__player.bluedan))*11 +(len(self.__player.chodan))*11 , y=320)
                    gotgodori_img = []
                    gotgodori = []
                    for i in range(len(self.__player.godori)):
                        gotgodori_img.append(PhotoImage(file = "./img_matgo/"+self.__player.godori[i].img()))
                        gotgodori.append(Label(image = gotgodori_img[i]))
                        gotgodori[i].place(x= 190+i*11, y=320)
                    gotanimal_img = []
                    gotanimal = []
                    for i in range(len(self.__player.animal)):
                        gotanimal_img.append(PhotoImage(file = "./img_matgo/"+self.__player.animal[i].img()))
                        gotanimal.append(Label(image = gotanimal_img[i]))
                        gotanimal[i].place(x= 190+i*11 + len(self.__player.godori)*11, y=320)
                    gotpee_img = []
                    gotpee = []
                    for i in range(len(self.__player.pee)):
                        gotpee_img.append(PhotoImage(file = "./img_matgo/"+self.__player.pee[i].img()))
                        gotpee.append(Label(image = gotpee_img[i]))
                        gotpee[i].place(x= 300+i*11, y=320)
                    gotdoublepee_img = []
                    gotdoublepee = []
                    for i in range(len(self.__player.doublepee)):
                        gotdoublepee_img.append(PhotoImage(file = "./img_matgo/"+self.__player.doublepee[i].img()))
                        gotdoublepee.append(Label(image = gotdoublepee_img[i]))
                        gotdoublepee[i].place(x= 300+i*11+ 10*len(self.__player.pee), y=320)
                    playerfuck = Label(a,text = "뻑 갯수 : "+str(player.fuck_display))
                    playerfuck.place(x= 430, y= 380)
                    playerscore = Label(a,text = "점수 : "+str(player.score))
                    playerscore.place(x=430,y=400)
                    playershake = Label(a,text = "흔들기 : " + str(player.shake_display))
                    playershake.place(x=430,y=420)
                    playergo = Label(a,text = "고 : " + str(player.go_display))
                    playergo.place(x = 430, y=440)
                    computergo = Label(a,text="고 :" +str(computer.go_display))
                    computergo.place(x=430,y=70)
                    computerfuck = Label(a,text = "뻑 갯수 : "+str(computer.fuck_display))
                    computerfuck.place(x= 430, y= 10)
                    computerscore = Label(a,text = "점수 : "+str(computer.score))
                    computerscore.place(x=430,y=30)
                    computershake = Label(a,text = "흔들기 : " + str(computer.shake_display))
                    computershake.place(x=430,y=50)
                    #self.printscreen()
                    if computer.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="컴퓨터 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["computer", 10*self.__panmoney]
                    if len(computer.hand)==0:
                        if computer.score>=7 and computer_score_last < computer.score:
                            self.__multiple=Score(computer).multiple(player)
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="컴퓨터 승리 !")
                            win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    check = Turn.computer_go_stop(computer, player, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(computer).multiple(player)
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="컴퓨터 승리 !")
                        win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    # time.sleep(1)
                    
                    self.__field = Turn.playerturn(player, computer, self.__field, self.__deck,root)
                    
                    #self.printscreen()
                    if player.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="플레이어 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["player", 10*self.__panmoney]
                    if len(player.hand)==0:
                        if player.score>=7 and player_score_last < player.score:
                            self.__multiple=Score(player).multiple(computer)
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="플레이어 승리 !")
                            win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                        else:
                            nagari_window = Toplevel(a)
                            nagari_label = Label(nagari_window,text="나가리입니다")
                            nagari_label.pack()
                            def finish():
                                nagari_window.destroy()
                                nagari_window.quit()
                            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
                            nagari_btn.pack()
                            nagari_window.mainloop()
                            return ["nagari"]
                    check = Turn.player_go_stop(player,root)
                    # check = Turn.computer_go_stop(player, computer, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(player).multiple(computer)
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="플레이어 승리 !")
                        win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    player_score_last=player.score
                    computer_score_last=computer.score
            
            nagari_window = Toplevel(a)
            nagari_label = Label(nagari_window,text="나가리입니다")
            nagari_label.pack()
            def finish():
                nagari_window.destroy()
                nagari_window.quit()
            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
            nagari_btn.pack()
            nagari_window.mainloop()
            return ["nagari"]

    def printscreen(self):
        print("\n\n\n# Computer #\n[", end=" ")
        for k in range(len(self.__computer.hand)//2):
            check=True
            for i in range(12):
                if len(self.__field[i])!=0:
                    if self.__field[i][0].month==self.__computer.hand[k].month:
                        check=False
            if check:
                print("( "+str(k+1)+" -", self.__computer.hand[k],")", end=" ")
            else:
                print("( "+str(k+1)+" -", self.__computer.hand[k],")", end=" ")
        print("]")
        print("[", end=" ")
        for k in range(len(self.__computer.hand)//2, len(self.__computer.hand)):
            check=True
            for i in range(12):
                if len(self.__field[i])!=0:
                    if self.__field[i][0].month==self.__computer.hand[k].month:
                        check=False
            if check:
                print("( "+str(k+1)+" -", self.__computer.hand[k],")", end=" ")
            else:
                print("( "+str(k+1)+" -", self.__computer.hand[k],")", end=" ")
        print("]\n")
        print("[ 점수 :", str(self.__computer.score),"]", end=" ")
        print("[ 흔들기 :", str(self.__computer.shake_display), "]", end=" ")
        print("[ 뻑 :", str(self.__computer.fuck_display), "]", end=" ")
        print("[ "+str(self.__computer.go_display)+"고"+" ]")
        print("광 [ ", end=" ")
        for k in self.__computer.gwang:
            print(k, end=" ")
        for k in self.__computer.beegwang:
            print(k, end=" ")
        print(" ]", end=" ")
        print("열끗 [ ", end=" ")        
        for k in self.__computer.godori:
            print(k, end=" ")
        for k in self.__computer.animal:
            print(k, end=" ")
        print(" ]")
        print("단 [ ", end=" ")  
        for k in self.__computer.reddan:
            print(k, end=" ")        
        for k in self.__computer.bluedan:
            print(k, end=" ")
        for k in self.__computer.chodan:
            print(k, end=" ")
        for k in self.__computer.dan:
            print(k, end=" ")
        print(" ]", end=" ")
        print("피 [ ", end=" ")
        for k in self.__computer.doublepee:
            print(k, end=" ")
        for k in self.__computer.pee:
            print(k, end=" ")
        print(" ]\n")
        print("============================================\n")
        for k in range(4):
            print("[ ", end=" ")
            for i in self.__field[k]:
                print(i, end=" ")
            print(" ]", end=" ")
        print("\n")
        for k in range(4, 8):
            print("[ ", end=" ")
            for i in self.__field[k]:
                print(i, end=" ")
            print(" ]", end=" ")
        print("\n")
        for k in range(8, 12):
            print("[ ", end=" ")
            for i in self.__field[k]:
                print(i, end=" ")
            print(" ]", end=" ")
        print("\n")
        print("============================================\n")
        print("[ 점수 :", str(self.__player.score),"]", end=" ")
        print("[ 흔들기 :", str(self.__player.shake_display), "]", end=" ")
        print("[ 뻑 :", str(self.__player.fuck_display), "]", end=" ")
        print("[ "+str(self.__player.go_display)+"고"+" ]")
        print("광 [ ", end=" ")
        for k in self.__player.gwang:
            print(k, end=" ")
        for k in self.__player.beegwang:
            print(k, end=" ")
        print(" ]", end=" ")
        print("열끗 [ ", end=" ")
        for k in self.__player.godori:
            print(k, end=" ")
        for k in self.__player.animal:
            print(k, end=" ")
        print(" ]")
        print("단 [ ", end=" ")  
        for k in self.__player.reddan:
            print(k, end=" ")        
        for k in self.__player.bluedan:
            print(k, end=" ")
        for k in self.__player.chodan:
            print(k, end=" ")
        for k in self.__player.dan:
            print(k, end=" ")
        print(" ]", end=" ")
        print("피 [ ", end=" ")
        for k in self.__player.doublepee:
            print(k, end=" ")
        for k in self.__player.pee:
            print(k, end=" ")
        print(" ]\n")
        print("[", end=" ")
        for k in range(len(self.__player.hand)//2):
            check=True
            for i in range(12):
                if len(self.__field[i])!=0:
                    if self.__field[i][0].month==self.__player.hand[k].month:
                        check=False
            if check:
                print("( "+str(k+1)+" -", self.__player.hand[k],")", end=" ")
            else:
                print("( "+str(k+1)+" -", self.__player.hand[k],"V )", end=" ")
        print("]")
        print("[", end=" ")
        for k in range(len(self.__player.hand)//2, len(self.__player.hand)):
            check=True
            for i in range(12):
                if len(self.__field[i])!=0:
                    if self.__field[i][0].month==self.__player.hand[k].month:
                        check=False
            if check:
                print("( "+str(k+1)+" -", self.__player.hand[k],")", end=" ")
            else:
                print("( "+str(k+1)+" -", self.__player.hand[k],"V )", end=" ")
        print("]\n# "+self.__player.name+" #\n")


def main(root):
    # main procedure
    window = tk.Toplevel(root)
    def close_window():
        window.destroy()
        window.quit()
    window.title("<<<맞고>>>")
    btn_label = Label(window, text = "맞고 게임을 시작하시겠습니까?")
    btn_label.grid(row=0,column=0)
    btn_start = Button(window, text = "Start",command =close_window)
    btn_start.grid(row = 1,column=0)
    btn_quit = Button(window, text = "Quit",command = quit)
    btn_quit.grid(row = 1, column = 1)
    window.mainloop()
    while True:
        ask = Reader.load(root)
        if ask:
            slot_window = Toplevel(root)
            for i in range(1,6):
                text=open("save"+str(i)+".txt", "a")
                text.close()
                text=open("save"+str(i)+".txt", "r")
                player_money=text.readline()[:-1]
                computer_money=text.readline()[:-1]
                ai=text.readline()[:-1]
                name=text.readline()[:-1]
                print("[ 슬롯", i, "]")
                slot_label = Label(slot_window,text = "[ 슬롯"+str(i)+" ]")
                slot_label.pack()
                if player_money=="":
                    slot_label['text'] = slot_label['text'] + " 비었음"
                else:
                    slot_label['text'] = slot_label['text'] + " 저장된 파일 있음"
                    if name=="":
                        slot_label['text'] = slot_label['text'] + "\n이름 : ???"
                    else:
                        slot_label['text'] = slot_label['text'] + "\n이름 : "+name
                    if not (ai=="easy" or ai=="normal" or ai=="hard" or ai=="hell" or ai=="impossible"):
                        slot_label['text'] = slot_label['text'] + "\n난이도 : ???"
                    else:
                        slot_label['text'] = slot_label['text'] + "\n난이도 : "+ai
                text.close()
            def finish():
                slot_window.destroy()
                slot_window.quit()
            slot_button = Button(slot_window,text = "끄기",command = finish)
            num=Reader.load_num(root)
            
            slot_button.pack()
            slot_window.mainloop()
            slot1_window = Toplevel(root)
            text=open("save"+str(num)+".txt", "r")
            player_money=text.readline()[:-1]
            computer_money=text.readline()[:-1]
            ai=text.readline()[:-1]
            name=text.readline()[:-1]
            text.close()
            if not (player_money.isdigit() and computer_money.isdigit()) or \
            not (ai=='easy' or ai=='normal' or ai=='hard' or ai=='hell' or ai=='impossible') or \
            name=="":
                label = Label(slot1_window,text = "세이브 파일이 없거나 손상되었습니다.")
                label.pack()
            else:
                label1 = Label(slot1_window,text = "성공적으로 불러왔습니다.")
                label2 = Label(slot1_window,text = name+"님의 돈 :"+str(player_money))
                label3 = Label(slot1_window,text = "컴퓨터의 돈 :"+str(computer_money))
                label4 = Label(slot1_window,text = "난이도 :"+ai)
                label1.pack()
                label2.pack()
                label3.pack()
                label4.pack()
                player_money=int(player_money)
                computer_money=int(computer_money)
                break
            def finish():
                slot1_window.destroy()
                slot1_window.quit()
            button = Button(slot1_window,text = "제출", command=finish)
            button.pack()
            slot1_window.mainloop()
        else:        
            player_money=Reader.init_money(root)
            computer_money=player_money
            ai=Reader.ai(root)
            name=Reader.name(root)
            break
    while True:
        nagari=0
        while True:
            ready=MatgoController(name, ai, nagari, player_money, computer_money)
            result=ready.play(root)
            if result[0]=="player":
                (player_money, computer_money) = (player_money+result[1], computer_money-result[1])
                print("승리했습니다. "+str(result[1])+" 원을 얻었습니다.")
                print("플레이어 소지금:", player_money)
                print("컴퓨터 소지금:", computer_money)
                break
            elif result[0]=="computer":
                (player_money, computer_money) = (player_money-result[1], computer_money+result[1])
                print("패배했습니다. "+str(result[1])+" 원을 잃었습니다.")
                print("플레이어 소지금:", player_money)
                print("컴퓨터 소지금:", computer_money)
                break
            elif result[0]=="double": # 양측 총통
                print("무승부입니다.")
                print("플레이어 소지금:", player_money)
                print("컴퓨터 소지금:", computer_money)
                break
            else: # result[0]=="nagari"
                print("나가리입니다. 판돈이 2배가 되어 게임이 재시작됩니다.")
                print("플레이어 소지금:", player_money)
                print("컴퓨터 소지금:", computer_money)
                ready.nagari()
        if player_money <= 0:
            print("플레이어가 파산했습니다.")
            break
        if computer_money <= 0:
            print("컴퓨터가 파산했습니다.")
            break
        save_complete=False
        if not Reader.again(root): # 다시 안할래요    
            while True:
                if Reader.save(root):
                    for i in range(1,6):
                        text=open("save"+str(i)+".txt", "a+")
                        text.close()
                        text=open("save"+str(i)+".txt", "r")
                        print("[ 슬롯", i, "]")
                        if text.readline()[:-1]=="":
                            print("비었음")
                        else:
                            print("저장됨")
                        text.close()
                    number=Reader.save_num(root)
                    text=open("save"+str(number)+".txt", "r+")
                    if text.readline()[:-1]!="":
                        if Reader.re_check(root):
                            text.close()
                            text1=open("save"+str(number)+".txt", "w")
                            text1.write(str(player_money)+"\n"+str(computer_money)+"\n"+ai+"\n"+name+"\n")
                            text1.close()
                            print("저장되었습니다.")
                            save_complete=True
                            break
                    else:
                        text.write(str(player_money)+"\n"+str(computer_money)+"\n"+ai+"\n"+name+"\n")
                        text.close()
                        print("저장되었습니다.")
                        save_complete=True
                        break
                else: # 저장 안할래요
                    print("Bye!")
                    save_complete=True
                    break
        if save_complete:
            break
root = Tk()
root.title("맞고")
root.geometry("600x500")

root.update()
main(root)
root.mainloop()