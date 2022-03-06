from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="084"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  #n以下の素数を列挙(10**6くらいまでは高速に動く)
  import itertools
  import math
  def Eratosthenes(n):
    prime=[]
    furui=list(range(2,n+1))
    while furui[0]<math.sqrt(n):
      prime.append(furui[0])
      furui=[i for i in furui if i%furui[0]!=0]
    return prime+furui
  prime=set(Eratosthenes(10**5))
  like=[1 if i%2==1 and i in prime and (i+1)//2 in prime else 0 for i in range(10**5+1)]
  like=list(itertools.accumulate(like))
  Q=int(input())
  for i in range(Q):
    l,r=map(int,input().split())
    print(like[r]-like[l-1])
  """ここから上にコードを記述"""

  print(test_case[__+1])