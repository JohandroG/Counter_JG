from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="Benny bob wuz heer."


@app.route('/')
def click1():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/addtwo')
def add2():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 2
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/