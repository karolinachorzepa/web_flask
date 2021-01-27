from flask import Flask
from flask import request, redirect, render_template

app=Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def about_me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET'])
def contact():
    if request.method=='GET': 
        return render_template("contact.html")

@app.route('/mypage/contact_form', methods=['GET','POST'])
def contact_form():
    if request.method=='POST':
        print(request.form)
    return render_template("contact_form.html")


if __name__ == "__main__":
    app.run()
