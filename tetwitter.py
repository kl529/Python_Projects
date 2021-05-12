from konlpy.tag import Twitter

def takesecon(element):
    return element[1]

def wordranking(openfile,writefile,rank):
    twitter = Twitter()
    noun_list, verb_list, adj_list = [], [], []
    f = open(openfile, 'r')  # 분석할 파일 입력
    for line in f:  # 파일을 한줄씩 읽음
        iden = twitter.pos(line, norm=True, stem=True)
        for line2 in iden:  # 그 줄에 있는 형용어를 읽음
            decide = False  # 그 단어가 이때까지 안나온 단어라고 생각하자
            if line2[1] == 'Noun':  # 만약 그 형용어가 명사라면
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
            if line2[1] == 'Verb':  # 만약 그 형용어가 동사라면
                count = 0
                for dow in verb_list:
                    count +1
                    if line2[0] == dow[0]:
                        decide = True
                        break;
                if decide:
                    verb_list[count - 1][1] +1
                else:
                    verb_list.append([line2[0], 1])
            if line2[1] == 'Adjective':  # 만약 그 형용어가 형용사라면
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
    f2 = open(writefile, 'w')  # 분석내용을 저장할 파일 입력
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

def main():
    inputfile = input()
    writefile = input()
    rank = int(input())
    wordranking(inputfile, writefile, rank)

if __name__ == "__main__":
    main()