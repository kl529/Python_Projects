from matgoscore import *
from matgohand import *
from matgoai import *
from matgofield import *
from matgocard import *
from tkinter import *
class Turn:
	@staticmethod
	def playerturn(player, computer, field, deck, a):
		playercard = player.put(a)
		#playercard = player.comput(AI("impossible").cardchoose(player, computer, field, deck)) # 카드번호를 내줘야함
		cards, field_result, c2p = fields(player, playercard, field, deck.next(), playercard.special=="폭탄").result()
		print("[ ", end='')		
		for k in cards:
			print(k, end=' ')
		print(" ] 를 얻으셨습니다. "+str(c2p)+" 개의 피를 가져옵니다.")

		# 얻은 카드 / 낸 후 필드 / 뺏어와야 하는 피
		dual=None
		#for i in range(len(cards)):
		#	if cards[i].month=="9" and cards[i].special=="쌍피열끗":
		#		dual = AI("impossible").determine(player, computer, field, deck)
		for i in range(len(cards)):
			if cards[i].month=="9" and cards[i].special=="쌍피열끗":
				dual = Reader.choose(a)
		cards=Turn.pee_rob(computer, cards, c2p)
		player.sort(cards, dual)
		player.set_score(Score(player).result())
		computer.set_score(Score(computer).result())
		return field_result

	@staticmethod
	def computerturn(player, computer, field, deck, ai):
		comcard = computer.comput(ai.cardchoose(computer, player, field, deck)) # 카드번호를 내줘야함
		comcard.flip()
		cards, field_result, p2c = fields(computer, comcard, field, deck.next(), comcard.special=="폭탄").result()
		print("컴퓨터가 [ ", end='')		
		for k in cards:
			print(k, end=' ')
		print(" ] 를 얻었습니다. "+str(p2c)+" 개의 피를 빼앗깁니다.")		
		dual=None
		for i in range(len(cards)):
			if cards[i].month=="9" and cards[i].special=="쌍피열끗":
				dual = ai.determine(computer, player, field, deck)
		cards=Turn.pee_rob(player, cards, p2c)
		computer.sort(cards, dual)
		player.set_score(Score(player).result())
		computer.set_score(Score(computer).result())
		return field_result


	@staticmethod
	def pee_rob(give, cards, number):
		if number==1:
			if len(give.pee)==0:
				if len(give.doublepee)!=0:
					cards.append(give.doublepee_rob())
			else:
				cards.append(give.pee_rob())
			number-=1
		if number==2:
			if len(give.doublepee)==0:
				if len(give.pee)==1:
					cards.append(give.pee_rob())
				elif len(give.pee)>=2:
					cards.append(give.pee_rob())
					cards.append(give.pee_rob())
			elif len(give.doublepee)!=0:
				cards.append(give.doublepee_rob())
			number-=2
		if number==3:
			if len(give.doublepee)==0:
				if len(give.pee)==1:
					cards.append(give.pee_rob())
				elif len(give.pee)==2:
					cards.append(give.pee_rob())
					cards.append(give.pee_rob())
				elif len(give.pee)>=3:
					cards.append(give.pee_rob())
					cards.append(give.pee_rob())
					cards.append(give.pee_rob())
			elif len(give.doublepee)!=0:
				if len(give.doublepee)>=2:
					if len(give.pee)==0:
						cards.append(give.doublepee_rob())
						cards.append(give.doublepee_rob())
					if len(give.pee)>=1:
						cards.append(give.pee_rob())
						cards.append(give.doublepee_rob())
				elif len(give.doublepee)==1:
					if len(give.pee)==0:
						cards.append(give.doublepee_rob())
					elif len(give.pee)>=1:
						cards.append(give.pee_rob())
						cards.append(give.doublepee_rob())
			number-=3
		return cards

	@staticmethod
	def player_go_stop(obj,a):
		if obj.was_score < obj.score:
			if obj.score>=7:
				if Reader.go(a):
					obj.set_was_score(obj.score)
					obj.go
					print("Player : Go!")
					return True # Go
				else:
					print("Player : Stop!")
					return False # Stop
			else:
				return True
		else:
			return True

	@staticmethod
	def computer_go_stop(obj, pobj, field, deck, ai):
		if obj.was_score < obj.score:
			if obj.score>=7:
				if ai.go_stop(obj, pobj, field, deck):
					obj.set_was_score(obj.score)
					obj.go
					print("Computer : Go!")
					return True # Go
				else:
					print("Computer : Stop!")
					return False # Stop
			else:
				return True
		else:
			return True