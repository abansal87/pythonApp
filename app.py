from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result1',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form
      return render_template("result1.html",result = result)

@app.route('/result2',methods = ['POST', 'GET'])
def result2():
   if request.method == 'POST':
      result = request.form
      return render_template("result2.html",result = result)

@app.route('/result3',methods = ['POST', 'GET'])
def result3():
   if request.method == 'POST':
      result = request.form
      return render_template("result3.html",result = result)

@app.route('/result4',methods = ['POST', 'GET'])
def result4():
   if request.method == 'POST':
      result = request.form
      return render_template("result4.html",result = result)

@app.route('/result5',methods = ['POST', 'GET'])
def result5():
   if request.method == 'POST':
      result = request.form
      return render_template("result5.html",result = result)

@app.route('/result6',methods = ['POST', 'GET'])
def result6():
   if request.method == 'POST':
      result = request.form
      return render_template("result6.html",result = result)

@app.route('/result7',methods = ['POST', 'GET'])
def result7():
   if request.method == 'POST':
      result = request.form
      return render_template("result7.html",result = result)

@app.route('/result8',methods = ['POST', 'GET'])
def result8():
   if request.method == 'POST':
      result = request.form
      return render_template("result8.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)