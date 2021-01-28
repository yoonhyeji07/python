from cx_Oracle import *
# import cx_Oracle
# def item_insert(data):
#     conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('insert into item values (:1,:2,:3,:4)',data)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# item_insert(('8806','샘플3',2000,'파이쎤3'))

# def item_delete(data):
#     conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('delete from item where code=:1',data)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# item_delete(('8805',))

# def item_update(data):
#     conn = connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('''update item
#                     set itemname = :1,
#                     price = :2,
#                     bigo = :3
#                     where code = :4 ''', data)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# item_update(('상품변경',1800,'수정테스트','8804'))

#전체조회
# def item_select():
#     conn = connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('select * from item order by code')
#     #언패킹
#     for code,name,price,bigo in cur:
#         print(code,name,price,bigo)
#     cur.close()
#     conn.close()
#
# item_select()

#조건 조회
def item_select_find(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''select * from item 
        where itemname like '%' || :find || '%' ''',data)
    print(len(list(cur)))
    #언패킹
    for code,name,price,bigo in cur:
        print(code,name,price,bigo)
    cur.close()
    conn.close()
# name = input('검색할 상품명?')
# item_select_find((name,))

#순위조회
def victor_seq():
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''select m.userid, m.name, count(v.userid) cnt
            from victor v right join member m on(v.userid =m.userid)
            group by m.userid,m.name
            order by cnt desc    ''')
    #언패킹
    for seq, x in enumerate(cur):
        print(seq+1, x[0], x[1], x[2])
    cur.close()
    conn.close()

victor_seq()