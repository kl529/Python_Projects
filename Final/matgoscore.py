class Score:
	def __init__(self, obj):
		self.__obj=obj

	def result(self): # 출력되는 점수
		score=0
		if len(self.__obj.godori)==3:
			score +=5
		if len(self.__obj.godori)+len(self.__obj.animal)>=5:
			score+=len(self.__obj.godori)+len(self.__obj.animal)-4
		if len(self.__obj.reddan)==3:
			score +=3
		if len(self.__obj.bluedan)==3:
			score +=3
		if len(self.__obj.chodan)==3:
			score +=3
		if len(self.__obj.reddan)+len(self.__obj.bluedan)+len(self.__obj.chodan)+len(self.__obj.dan)>=5:
			score += len(self.__obj.reddan)+len(self.__obj.bluedan)+len(self.__obj.chodan)+len(self.__obj.dan)-4
		if len(self.__obj.beegwang)==1:
			if len(self.__obj.beegwang)+len(self.__obj.gwang)==3:
				score +=2
		if len(self.__obj.beegwang)==0:
			if len(self.__obj.gwang)==3:
				score +=3
		if len(self.__obj.beegwang)+len(self.__obj.gwang)==4:
			score += 4
		if len(self.__obj.beegwang)+len(self.__obj.gwang)==5:
			score += 15
		if len(self.__obj.pee)+2*len(self.__obj.doublepee)>=10:
			score += len(self.__obj.pee)+2*len(self.__obj.doublepee)-9
		return score

	def result_end(self):
		if self.__obj.go_display<=2:
			return self.__obj.score+self.__obj.go_display
		else:
			return (self.__obj.score+2)*2**(self.__obj.go_display-2)

	def multiple(self, enemyobj):
		multiple=1
		if len(self.__obj.animal)+len(self.__obj.godori)>=7:
			multiple=multiple*2
			print("멍따")
		if len(self.__obj.gwang)+len(self.__obj.beegwang)>=3 and len(enemyobj.gwang)+len(enemyobj.beegwang)==0:
			multiple=multiple*2
			print("광박")
		if len(self.__obj.pee)+2*len(self.__obj.doublepee)>=10 and len(enemyobj.pee)+2*len(enemyobj.doublepee)<=7:
			multiple=multiple*2
			print("피박")
		if self.__obj.go_display>=0 and enemyobj.go_display>=1:
			multiple=multiple*2
			print("고박")
		multiple=multiple*2**self.__obj.shake_display
		if self.__obj.shake_display>0:
			print(self.__obj.shake_display,"번 흔듦")
		return multiple
		# 멍따 : 열끗 7개 // 2배
		# 광박 : 3개 이상인데 상대는 광이 없을때 // 2배
		# 피박 : 피 점수 얻음. 상대 피 <=7 // 2배
		# 고박 : 내가 고/스톱을 했는데 상대가 고 했으면 // 2배
		# 흔들기 : 개당 2배