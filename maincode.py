import mymodule
from flask import Flask, render_template, url_for, request
app = Flask(__name__)





@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/categories', methods = ["GET"])
def getdata():
    namelist_,addresslist_,contactlist_ = []
    if "peepeepoopoo" in request.args:
        value1 = request.args["peepeepoopoo"]
        namelist_,addresslist_,contactlist_ = mymodule.module1(value1)
    return render_template("datatable.html",namlist = namelist_, addlist=addresslist_,contlist =contactlist_)

if __name__ == "__main__":
    app.run(debug = True)

