def solution(A):
    front_counter=0
    back_counter=0
    diff_list=[]
    for item in A:
        front_counter+=item
        back_counter=sum(A)-front_counter
        diff_list.append(abs(front_counter-back_counter))
    return min(diff_list)

print(solution([3,1,2,4,3]))
