def solution(A):
    n=len(A)+1
    total=int((n*(n+1))/2)
    return total-sum(A)

print(solution([2,3,1,5]))