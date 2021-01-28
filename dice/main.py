from cx_Oracle import *

from sub.member import *
#승자추가
def victor_insert(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('insert into victor values ((select nvl(max(seq) +1,1) seq from victor),:1)',data)
    cur.close()
    conn.commit()
    conn.close()

def userInput(msg):
    userid = input(msg+'아이디는?')
    name = input(msg+'이름은?')
    return (userid, name)

# userid1, name1 = userInput('첫번째')
# member_insert((userid1,name1))
# userid2, name2 = userInput('두번째')
# member_insert((userid2,name2))





def member_selectTest():
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from member')

    # print(cur.fetchmany())
    print(cur.fetchall())
    # for x in cur:
    #     print(x)

    print('건수:', cur.rowcount)
    # for x in cur:
    #     print(x)
    cur.close()
    conn.close()

# member_selectTest()

while True:
    print('1.사용자등록')
    print('2.게임시작')
    print('3.순위 조회')
    print('-' * 15)
    no = input('번호는?')
    if no == '1':
        data = userInput('')
        member_insert(data)
    elif no=='2':
        import random
        firstid = input('1번 아이디')
        secondid = input('2번 아이디')
        #아이디db에 저장
        member_save(firstid)
        member_save(secondid)

        a = random.randint(1,6)
        b = random.randint(1, 6)
        if a>b:
            print('1번 승')
        elif b>a:
            print('2번 승')
        else:
            print('무승부')

    elif no =='3':
        print()


















