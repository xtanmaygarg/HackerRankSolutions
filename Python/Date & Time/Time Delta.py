from datetime import *
Month = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6,
         'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
for _ in range(int(input())):
    S = input().split()
    T = input().split()
    ST = S[4].split(':')
    TT = T[4].split(':')
    SD = datetime(int(S[3]), Month[S[2]], int(S[1]), int(ST[0]), int(ST[1]), int(ST[2]))
    TD = datetime(int(T[3]), Month[T[2]], int(T[1]), int(TT[0]), int(TT[1]), int(TT[2]))
    SZ = S[5]
    TZ = T[5]
    SS = int(SZ[1:3]) * 3600 + int(SZ[3:]) * 60
    TS = int(TZ[1:3]) * 3600 + int(TZ[3:]) * 60
    if SZ[0] == '+':
        SS = -SS
    if TZ[0] == '+':
        TS = -TS
    STD = timedelta(seconds = SS)
    TTD = timedelta(seconds = TS)
    SD = SD + STD
    TD = TD + TTD
    if SD > TD:
        print(int((SD - TD).total_seconds()))
    else:
        print(int((TD - SD).total_seconds()))
