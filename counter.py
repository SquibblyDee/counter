from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'yobogoya'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template('counter.html', counter=session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plus_two')
def addTwo():
    session['count']+=1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)