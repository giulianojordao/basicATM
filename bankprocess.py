import sqlite3
import os.path
import smtplib

conn = sqlite3.connect('bankdb12.sqlite')
cur = conn.cursor()

cur.executescript('''CREATE TABLE IF NOT EXISTS Details (Name, Age, Email, AccountNo, LastTransaction, Money)''')
cur.execute('''INSERT INTO Details (AccountNo) VALUES (11111111);''')
cur.execute('''INSERT INTO Details (AccountNo) VALUES (22222222);''')

while True:
    print('Welcome to the Andhra Bank!!!')
    x = int(raw_input('Enter Account No.: '))
    y = int(raw_input('Enter Password: '))
    Select = int(raw_input('Enter 1. Enter Details \n2. View Details \n3. Update Details \n4. Mail \n'))
    if Select==1:
        a = raw_input('Enter Your Name: ')
        b = int(raw_input('Enter Your Age: '))
        c = raw_input('Enter Your Email: ')
        d = int(raw_input('Your Last Transaction: '))
        e = int(raw_input('Amount: '))
        cur.execute('''INSERT INTO Details (Name, Age, Email, AccountNo, LastTransaction, Money) VALUES (?, ?, ?, ?, ?, ?)''', (a, b, c, x, d, e,))
    elif Select==2:
        cur.execute('''SELECT * FROM Details WHERE AccountNo=?''', (x,))
        print cur.fetchall()
    elif Select==3:
        a = raw_input('Enter Your Name: ')
        b = int(raw_input('Enter Your Age: '))
        c = raw_input('Enter Your Email: ')
        d = int(raw_input('Your Last Transaction: '))
        e = int(raw_input('Amount: '))
        cur.execute('''UPDATE Details SET Name=?, Age=?, Email=?, LastTransaction=?, Money=? WHERE AccountNo=?''', (a, b, c, d, e, x,))
    elif Select==4:
        fromaddr = 'kuku1096gupta@gmail.com'
        cur.execute('''SELECT Email FROM Details WHERE AccountNo=?''', (x,))
        toaddrs = 'cur.fetchone()'
        cur.execute('''SELECT * FROM Details WHERE AccountNo=?''', (x,))
        msg = 'cur.fetchall()'


        # Credentials (if needed)
        username = 'sender mail id'
        password = 'password'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    else:
        print 'Invalid Input!!!'

    f = int(raw_input('Do You Want to use it Again???'))
    if f==1:
        continue
    else:
        break
conn.commit()
conn.close()

        
    

