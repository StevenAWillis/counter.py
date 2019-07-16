from flask import Flask, render_template, request, redirect, session

app  =Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def count():
    if 'count' not in session:
        session['count'] =0
    else:
        session['count'] +=1

    if 'countv' not in session:
        session['countv'] =0
    else:
        session['countv'] +=1
    
    return render_template("index.html", count_visits = session['count'],count_visits2 = session['countv'])

@app.route("/by2")
def count_2():

    session['count'] +=1
    
    return redirect("/" )

@app.route("/reset")
def count_reset():

    session['count'] = 0
    
    return redirect("/" )

@app.route("/manual_count",methods=['POST'])
def manual_count():
    # session['manual_counter'] = request.form['number']
    # session['count'] += int(session['manual_counter'])-1
    session['count'] += int(request.form['number'])-1
    
    return redirect("/" )



app.run(debug=True)