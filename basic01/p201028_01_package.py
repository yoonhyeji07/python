#패키지
# import pPackage.test01
# print(pPackage.test01.a)
# pPackage.test01.sample()

# from pPackage.test01 import sample,a
# sample()
# print(a)

#모든함수/변수/클래스 등 import
# from pPackage.test01 import *
# sample()
# print(a)

#패키지밑의 모듈 import
# from pPackage import test02,test01
# test01.sample()
# test02.sample2()

# __all__ 에 지정된 모듈 import
from pPackage import *
test01.sample()
test02.sample2()






