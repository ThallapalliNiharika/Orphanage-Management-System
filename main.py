from flask import  *
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="niharika",
   database="niha"
)

@app.route('/',methods=['GET','POST'])
def Home():
    return render_template("Home.html")

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    return render_template("dashboard.html")

@app.route('/donation',methods=['GET','POST'])
def donation():
    return render_template("donation.html")

@app.route('/IAC',methods=['GET','POST'])
def IAC():
    return render_template("IAC.html")

@app.route('/save_login',methods=['GET','POST'])
def save_login():
    if(request.method=="POST"):
        email=request.form.get("Email")
        password=request.form.get("psw")
        mycursor = mydb.cursor()
        sql="select email,password from signup where email=%s and password=%s"
        data=(email,password,)
        mycursor.execute(sql,data)
        result = mycursor.fetchall()
        if(len(result)==1):
            return render_template("dashboard.html")

        else:
            result = -1
            if result == -1:
                m = "check your email and password"
                l = "/login"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("login.html")



@app.route('/save_signup',methods=['GET','POST'])
def save_signup():
    if(request.method=="POST"):
        Name = request.form.get("Name")
        email=request.form.get("email")
        password=request.form.get("psw")
        psw_repeat = request.form.get("psw_repeat")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT email from signup where email='" + email + "'")
        result=mycursor.fetchall()
        if(len(result)==0):
            mycursor.execute("INSERT INTO signup VALUES(%s,%s,%s,%s)", (Name, email, password, psw_repeat))
            mydb.commit()
            return render_template("login.html")
        else:
            result=-1
            if result == -1:
                m = "This email has already exists"
                l = "/signup"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
