def solution(A):
    for item in A:
        counter=A.count(item)

        if counter%2!=0:
            return item
            break