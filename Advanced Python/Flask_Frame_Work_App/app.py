from flask import Flask,render_template
from flask import redirect,url_for
from flask import request,make_response,session
import pymysql as sql
app=Flask(__name__)
app.secret_key = "kidifjipejfipejfiklkneiefnef08094788y3gfbjbfjfj"
@app.route('/')
def index():
    return "<h1>Hello index</h1>"
@app.route('/start/')
def start():
    return render_template('start.html')
@app.route('/signup/')
def signup():
    return render_template('signup.html')
@app.route('/signup/signup1/',methods=['GET','POST'])
def signup1():
    pass1=request.form.get('pass')
    pass2=request.form.get('cpass')
    if pass1==pass2:
        db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
        c=db.cursor()
        fname=request.form.get('first_name')
        lname=request.form.get('last_name')
        email=request.form.get('email')
        bal=request.form.get('balance')
        acc=''
        if fname == '' or email == '' or pass1 == '':
            error='Please enter valid details.....'
            return render_template('signup.html',error=error)
        else:   
            cmd = "insert into authentication values('{}','{}','{}','{}','{}','{}')".format(acc,fname,lname,email,pass1,bal)
            c.execute(cmd)
            db.commit()
            cmd='SELECT * FROM authentication ORDER BY accno DESC LIMIT 1'
            c.execute(cmd)
            data2=c.fetchone()
            data1={
                'First Name':fname,
                'Last Name':lname,
                'Email':email,
                'balance': bal,
                'accno':data2[0],
                }
            return render_template('signup1.html',data=data1)
    else:
        error = "Password does not matched...Try again"
        return render_template("signup.html",error=error)
@app.route('/login/')
def login():
    return render_template('login.html')
@app.route('/login/login1/',methods=['GET','POST'])
def login1():
    accno=request.form.get('acc')
    password=request.form.get('pass')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
    c=db.cursor()
    cmd = "select * from authentication where accno='{}'".format(accno)
    c.execute(cmd)
    data=c.fetchone()
    if data:
        if data[4]==password:
            msg=f'Hello {data[1]} ! Now you are at transaction page......'
            return render_template('transact.html',msg=msg)
        else:
            error='password does not match.....'
            return render_template('login.html',error=error)
    else:
        error='No such user exist.....Please Signup'
        return render_template('signup.html',error=error)
@app.route('/login/login1/debit/')
def debit():
    return render_template('debit.html')
@app.route('/login/login1/debit/debit1/',methods=['GET','POST'])
def debit1():
    accno=request.form.get('acc')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
    c=db.cursor()
    cmd = "select * from authentication where accno='{}'".format(accno)
    c.execute(cmd)
    data=c.fetchone()
    if data:
        password=request.form.get('pass')
        if data[4]==password:
            amt=request.form.get('amount')
            bal=int(data[5])-int(amt)
            cmd=f'update authentication set Balance={bal} where accno={data[0]}'
            c.execute(cmd)
            db.commit()
            msg=f'Withdrawl Successful......and your updated balance is: {bal}'
            return render_template('transact.html',msg=msg)    
        else:
            msg='Password not Matched........'
            return render_template('debit.html',error=msg)
    else:
        msg='No account exist on this account number....please signup'
        return render_template('start.html',error=msg)
@app.route('/login/login1/credit/')
def credit():
    return render_template('credit.html')
@app.route('/login/login1/credit/credit1/',methods=['GET','POST'])
def credit1():
    accno=request.form.get('acc')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
    c=db.cursor()
    cmd = "select * from authentication where accno='{}'".format(accno)
    c.execute(cmd)
    data=c.fetchone()
    if data:
        password=request.form.get('pass')
        if data[4]==password:
            amt=request.form.get('amount')
            bal=int(data[5])+int(amt)
            cmd=f'update authentication set Balance={bal} where accno={data[0]}'
            c.execute(cmd)
            db.commit()
            msg=f'Deposit Successful......and your updated balance is {bal}'
            return render_template('transact.html',msg=msg)    
        else:
            msg='Password not Matched........'
            return render_template('credit.html',error=msg)
    else:
        msg='No account exist on this account number....please signup'
        return render_template('start.html',error=msg)
@app.route('/login/login1/check_bal/')
def check_bal():
    return render_template('check_bal.html')
@app.route('/login/login1/check_bal/check_bal1/',methods=['GET','POST'])
def check_bal1():
    accno=request.form.get('acc')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
    c=db.cursor()
    cmd = "select * from authentication where accno='{}'".format(accno)
    c.execute(cmd)
    data=c.fetchone()
    if data:
        password=request.form.get('pass')
        if data[4]==password:
            amt=data[5]
            msg=f'Your account balance is: {amt}'
            return render_template('transact.html',msg=msg)
        else:
            msg='Password not Matched........'
            return render_template('check_bal.html',error=msg)
    else:
        msg='No account exist on this account number....please signup'
        return render_template('start.html',error=msg)
@app.route('/login/login1/update_pwd/')
def update_pwd():
    return render_template('update_pwd.html')
@app.route('/login/login1/update_pwd/update_pwd1/',methods=['GET','POST'])
def update_pwd1():
    accno=request.form.get('acc')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='homebanking')
    c=db.cursor()
    cmd = "select * from authentication where accno='{}'".format(accno)
    c.execute(cmd)
    data=c.fetchone()
    if data:
        password=request.form.get('pass')
        if data[4]==password:
            new_pass=request.form.get('npass')
            cmd=f"update authentication set passwd ={new_pass} where accno={data[0]}"
            c.execute(cmd)
            db.commit()
            msg='Your password updated successfully......'
            return render_template('transact.html',msg=msg)
        else:
            msg='Password not Matched........'
            return render_template('update_pwd.html',error=msg)
    else:
        msg='No account exist on this account number....please signup'
        return render_template('start.html',error=msg)
@app.route('/start/about/')
def about():
     return render_template('about.html') 
@app.route('/home/')
def home():
    return render_template('start.html')          
if __name__ == '__main__':
    app.run(host='192.168.43.174',debug=True)