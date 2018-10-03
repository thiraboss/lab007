import sqlite3,time
conn = sqlite3.connect('thiraboss.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM user'):
        print (row[0])
def login(username,password):
        while True:
                #username = input("username: ")
                #password = input("password: ")
                with sqlite3.connect('thiraboss.db') as db:
                    cursor = db.cursor()
                find_user = ('SELECT * FROM user WHERE username =? and password =?')
                cursor.execute(find_user,[(username),(password)])
                results = cursor.fetchall()

                if results:
                    for i in results:
                        print("Welcome " +username)
                        return 1
                    break
                else:
                    print("username or password is not correct.")
                    #again = input("do you want to try again?(y/n): ")
                    #if again.lower() == "n":
                    #   print('goodbye')
                    #    time.sleep(1)
                    return 0 
                    break


