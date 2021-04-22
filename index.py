from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/unitconvertor")
def unit():
   return render_template("unit.html")


@app.route("/cal",methods=["POST","GET"])
def value():
    l = request.form["left"]
    value = request.form.get("value")
    if value == "mmtocm":
        ans = int(l)/10
        unit = "cm"
    elif value == "cmtoinch":
        ans = int(l)/2.54
        unit = "inch"
    elif value == "mtocm":
        ans = int(l)*100
        unit = "cm"
    elif value == "mtoyard":
        ans = int(l)*1.09361
        unit = "yard"
    elif value == "mtofoot":
        ans = int(l)*3.281
        unit = "foot"
    elif value == "mtoinch":
        ans = int(l)*39.37
        unit = "inch"
    elif value == "mtokm":
        ans = int(l)*0.001
        unit = "km"
    elif value == "inchtocm":
        ans = int(l)*2.54
        unit = "cm"
    elif value == "inchtoyard":
        ans = int(l)/36
        unit = "yard"
    elif value == "inchtofoot":
        ans = int(l)/12
        unit ="foot"
    elif value == "foottoyard":
        ans = int(l)/3
        unit = "yard"
    elif value == "foottoinch":
        ans = int(l)*12
        unit = "inch"
    elif value == "kmtomile":
        ans = int(l)/1.609
        unit = "mile"
    elif value == "miletokm":
        ans = int(l)*1.609
        unit = "km"
    else:
        print("thank you")
    return render_template("unit.html",value = ans,unit = unit)




if __name__ == "__main__":
    app.run(debug=True)