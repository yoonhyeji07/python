from cx_Oracle import *
def member_save(data):
    cnt = member_selectCheckYn(data)
    if cnt > 0:
        member_update(data)
    else:
        member_insert()



# 아이디 존재 유무
def member_selectCheckYn(data):
    print(data)
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select count(*) cnt from member where userid = :1',data)
    cnt = tuple(cur)[0][0]
    cur.close()
    conn.close()
    return cnt

#멤버추가
def member_insert(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('insert into member values (:1,:2)',('hong','홍길동'))
    cur.close()
    conn.commit()
    conn.close()

#멤버수정
def member_update(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('update member set name=:1 where userid=:2',data)
    cur.close()
    conn.commit()
    conn.close()