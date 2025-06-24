import os
import sys

"""
Python 과제 1
- 논리 연산자를 사용하지 않고 동일한 결과 출력하기
- 논리 and 연산자와 논리 or 연산자를 사용하지 않고 동일한 결과 출력하기

Ex)
정수 (2 개) 입력 : 10 0

=====> 결과 <=====
10 and 0 = False
10 or 0 = True
"""


# Practice 1
def start(args):
	nVal = input("\n정수 2개를 입력하세요 : ").split()
	
	# 문자열을 숫자로 변환
	nValA = int(nVal[0])
	nValB = int(nVal[1])
	
	# truthy인지 falsy인지 구분
	nValBoolA = not ((not nValA) + (not nValB))
	nValBoolB = not ((not nValA) * (not nValB))
	
	# nValA랑 nValB랑 둘다 같아야 True
	# nValA 또는 nValB 중 하나라도 truthy면 Ture
	# 만약 둘 중 하나라도 음수값이 들어온다면..?
	
	# true and true => true
	# true and false => false
	# false and true => false
	# false and false => false
	
	
	# false or ture => ture
	# false or false => false
	# true or ture => true
	# true or false => true
	
	print(f"{nValA} and {nValB} = {nValBoolA}")
	print(f"{nValA} or {nValB} = {nValBoolB}")
	pass
