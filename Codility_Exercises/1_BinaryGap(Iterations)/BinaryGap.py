def solution(N):
    binary=bin(N)
    number=binary[3:]


    gap_list=[]
    i=0
    if N!=0:
        while i<int(len(number)):
            j=number[i:].find("1")
            if j==-1:
                break
            else:
                gap_list.append(number[i:j+i])
                i+=j+1

        if gap_list==[]:
            return 0
        else:

            return len(max(gap_list))


    else:
        print("This number doesn't have a binary gap!!!")
        return 0

solution(1041)