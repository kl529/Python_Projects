import nltk

def takesecon(element):
    return element[1]


rank = 10
noun_list, verb_list, adj_list = [], [], []
f = open('ENG_all.txt', 'r')  # 분석할 파일 입력
for line in f:  # 파일을 한줄씩 읽음
    tokens = line.split(" ")
    tags_en = nltk.pos_tag(tokens)
    print(tags_en)
    for line2 in tags_en:  # 그 줄에 있는 형용어를 읽음
        # print(line2[1],"*","\n")
        decide = False  # 그 단어가 이때까지 안나온 단어라고 생각하자
        if (line2[1] == 'NN' or line2[1] == 'NNS' or line2[1] == 'NNP' or line2[1] == 'NNPS' or line2[1] == 'PRP' or line2[1] == 'PRP$') and (line2[0] != '\n') :  # 만약 그 형용어가 명사라면
            count = 0  # 형태소의 개수
            for dow in noun_list:
                count += 1
                if line2[0] == dow[0]:
                    decide = True
                    break;
            if decide:  # 있는 단어면 횟수 +1
                noun_list[count - 1][1] += 1
            else:  # 없는 단어면 새로 추가
                noun_list.append([line2[0], 1])
        if line2[1] == 'VB' or line2[1] == 'VBD' or line2[1] == 'VBG' or line2[1] == 'VBN' or line2[1] == 'VBP' or line2[1] == 'VBZ':  # 만약 그 형용어가 동사라면
            count = 0
            for dow in verb_list:
                count + 1
                if line2[0] == dow[0]:
                    decide = True
                    break;
            if decide:
                verb_list[count - 1][1] + 1
            else:
                verb_list.append([line2[0], 1])
        if line2[1] == 'JJ':  # 만약 그 형용어가 형용사라면
            count = 0
            for dow in adj_list:
                count += 1
                if line2[0] == dow[0]:
                    decide = True
                    break;
            if decide:
                adj_list[count - 1][1] += 1
            else:
                adj_list.append([line2[0], 1])
f2 = open('new.txt', 'w')  # 분석내용을 저장할 파일 입력
f2.write("\n\n---noun---")
noun_list.sort(key=takesecon, reverse=True)
for i in range(rank):  # len(noun_list)
    noun_list[i][1] = str(noun_list[i][1])
    a = "\n" + str(i + 1) + ". " + ' : '.join(noun_list[i])
    f2.write(a)
f2.write("\n\n---verb---")
verb_list.sort(key=takesecon, reverse=True)
for i in range(rank):  # len(verb_list)
    verb_list[i][1] = str(verb_list[i][1])
    a = "\n" + str(i + 1) + ". " + ' : '.join(verb_list[i])
    f2.write(a)
f2.write("\n\n---adj---")
adj_list.sort(key=takesecon, reverse=True)
for i in range(rank):  # len(adj_list)
    adj_list[i][1] = str(adj_list[i][1])
    a = "\n" + str(i + 1) + ". " + ' : '.join(adj_list[i])
    f2.write(a)
f.close()
f2.close()
print("finish")








