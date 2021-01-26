from flask import Flask
from flask import request, redirect, render_template

app2=Flask(__name__)

@app2.route('/')

@app2.route('/mypage/me', methods=['GET'])
def about_me():
    return render_template("1stside.html")

@app2.route('/mypage/contact', methods=['GET'])
def contact_me():
    return render_template("2ndside.html")

@app2.route('/mypage/contactcontactmeform', methods=['GET'])
def contact_me_form():
    return render_template("3rdside.html")

@app2.route('/mypage/contactmeform', methods=['POST'])
def contact_me_formmessage():
    if request.method=='POST':
        print(request.form)
    return render_template("3rdhtml.html")

        
if __name__ == "__main__":
    app2.run()
