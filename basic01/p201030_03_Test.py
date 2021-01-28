#파이션의 메모리 관리
#참조하는 변수의 카운터가 0이 되면 메모리에서 삭제
class Test:
    def __del__(self):
        print('삭제')

t = Test() #Test()카운터=>1
a = t #Test()카운터=>2
# del t
t = Test() #Test()카운터=>1
a=10 #Test()카운터=>0 Test()객체 메모리에서 del
input()