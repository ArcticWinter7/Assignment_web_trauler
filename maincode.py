import mymodule
from flask import Flask, render_template, url_for

catlist = ["advertising","automotives"]
namelist_,addresslist_,contactlist_ = mymodule.module1(catlist)
print(namelist_)
lengtho = len(namelist_)

app = Flask(__name__)
@app.route('/')


def index():
    thing1 = "yes"

    return render_template('index.html',namlist = namelist_, addlist=addresslist_,contlist =contactlist_,lengtho2 = lengtho)

if __name__ == "__main__":
    app.run(debug = True)

def printthing(thing):
    print(thing)
        

