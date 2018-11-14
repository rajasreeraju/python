from flask import Flask,render_template,request
from employeelist import Employee

app=Flask(__name__)
getEmp=Employee()


@app.route("/")
def home():
    return render_template('home.html')
@app.route("/employeelist")
def employee():
    getEmp=Employee()
    return render_template('employeelist.html',emp=getEmp)

if(__name__=='__main__'):
    app.run(debug=True)