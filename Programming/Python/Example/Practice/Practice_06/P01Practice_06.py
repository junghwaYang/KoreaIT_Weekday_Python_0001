import os
import sys

"""
Python 과제 6
- 다양한 형태 출력하기
- 라인 수를 입력 받아 해당 라인만큼 다양한 형태를 출력한다

Ex)
라인 수 입력 : 5
*   *
 * *
  *
 * *
*   *

*****
   *
  *
 *
*****

*   *
**  *
* * *
*  **
*   *

    *
   ***
  *****
 *******
*********

*********
 *******
  *****
   ***
    *
"""


# Practice 6
def start(args):
	nNumLines = int(input("정수를 입력하세요:"))
	print()
	
	nWidth_Max = (nNumLines * 2) - 1
	
	for i in range(0, nNumLines):  # i의 범위
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):  # j의 범위
			bIsStar = j >= nCenter >= j
			print("{0}".format("*" if bIsStar else " "), end = "")
		print()
	
	print()
	
	for i in range(0, nNumLines)[::-1]:  # i의 범위 [::-1] 은 slice라고 한다
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):  # j의 범위
			bIsStar = j >= nCenter >= j
			print("{0}".format("*" if bIsStar else " "), end = "")
		print()
