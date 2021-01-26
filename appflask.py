from flask import Flask
from flask import request, redirect, render_template

app2=Flask(__name__)

@app2.route('/mypage/me', methods=['GET'])
def about_me():
    return render_template("1stside.html")

@app2.route('/mypage/contact', methods=['GET'])
def contact_me():
    return render_template("2ndside.html")

@app2.route('/mypage/contactmeform', methods=['GET','POST'])
def contact_me_form():
    if request.method=='POST':
        print(request.form)
        return redirect("/mypage/contactmeform")
    return render_template("3rdside.html")
        
if __name__ == "__main__":
    app2.run()
