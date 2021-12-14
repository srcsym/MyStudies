def solution(N):
    bin_n = bin(N)
    bin_num = bin_n[2:]
    print(bin_num)
    if bin_num.count("1") != 1:

        x = bin_num.split("1")
        print(len(max(x)))
    else:
        return 0

solution(1041)