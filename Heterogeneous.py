import mdptoolbox
import mdptoolbox.example
import os

currentPath = os.getcwd()

print(currentPath)

os.chdir(currentPath)

files = os.listdir(currentPath)
print("Files in %r : %s" % (currentPath, files))

""" agg 에 대한 전이확률 Pa는 0 ~ n.max 인 배열에서 
n이 0일 때 n이 1이 될 확률이 람다 뮤 타우,
n이 0일 때 n이 0이 될 확률이 1 - 람다 뮤 타우,
위의 것을 n이 n.max - 1 까지 반복해서 배열 안을 채운다. """

nmax = 3
n = 0
n1 = 1

"""임의의 람다 뮤 타우"""
p = 0.1 

""" 뮤w타우 """ 
Pw = 0.5

""" 뮤c타우 """
Pc = 0.1



Pp = [[0 for j in range(nmax)] for i in range(nmax)]

for n in range(nmax-1):
    Pp[n][n+1] = p
    Pp[n][n] = 1 - p


"""push 에 대한 전이확률 Pp는 = 0 ~ max 인 배열에서
n이 0이 아닐 때 모든 곳에서 100퍼센트 확률로 n이 0이 됨"""

Pa = [[0 for j in range(nmax)] for i in range(nmax)]

for n in range(nmax-1):
    Pa[n+1][0] = 1


""" 네트워크 유형의 전이확률은 2 x 2 배열에서 c -> w 확률 뮤c타우이고, 
c -> c 확률 1 - 뮤c타우 이다. w -> c 확률 뮤w타우 ,
 w -> w 확률 1 - 뮤w타우이다. *0이 c, 1 이 w """

PN = [[0 for j in range(2)] for i in range(2)]

PN[0][0] = 1 - Pc
PN[0][1] = Pc
PN[1][0] = Pw
PN[1][1] = 1 - Pw 


""" action이 push 일 때 리워드는 Wm(연결설정비용Ls + 연결전달비용Ld x n)
    action이 agg 일 때 리워드는 s(n), 본문에서는 n으로 정의함"""

Ls = 1
Ld  = 0.59
w = 0.4
wc = 1.5
ww = 1

fc = [[0 for j in range(1)] for i in range(nmax)]

for n in range(nmax-1):
    fc[n+1][0] = wc * (Ls + (n+1) * Ld)

fw = [[0 for j in range(1)] for i in range(nmax)]

for n in range(nmax-1):
    fw[n+1][0] = ww * (Ls + (n+1) * Ld)

gc = [[0 for j in range(1)] for i in range(nmax)]

for n in range(nmax):
    gc[n][0] = n



gw = [[0 for j in range(1)] for i in range(nmax)]

for n in range(nmax):
    gw[n][0] = n


print(gw)



