# 딱지놀이(14696번)

Testcase = int(input())
for test in range(Testcase):
    L, *A = list(input().split())
    M, *B = list(input().split())

    C_A = [0]*4
    C_B = [0]*4
    for i in A:
        if i == '1':
            C_A[0]+=1
        elif i == '2':
            C_A[1]+=1
        elif i == '3':
            C_A[2]+=1
        else:
            C_A[3]+=1
    
    for i in B:
        if i == '1':
            C_B[0]+=1
        elif i == '2':
            C_B[1]+=1
        elif i == '3':
            C_B[2]+=1
        else:
            C_B[3]+=1

    if C_A[3]>C_B[3]:
        print('A')
    elif C_A[3] == C_B[3]:
        if C_A[2] > C_B[2]:
            print('A')
        elif C_A[2] < C_B[2]:
            print('B')
        else :
            if C_A[1] > C_B[1]:
                print('A')
            elif C_A[1] < C_B[1]:
                print('B')
            else :
                if C_A[0] > C_B[0]:
                    print('A')
                elif C_A[0] < C_B[0]:
                    print('B')
                else:
                    print('D')
    else:
        print('B')