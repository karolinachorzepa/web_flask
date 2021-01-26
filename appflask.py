#Co do backendu, zaprojektuj prostą aplikację z Flask. 
#W sumie musisz zdefiniować trzy funkcje adnotowane @app.route – dwie, 
#które wyświetlą strony i trzecią przeznaczoną dla zapisywania danych z formularza. 
#Oznacz je odpowiednio.
#/mypage/me – informacje o mnie
#/mypage/contact – informacje kontaktowe
#/mypage/contact (POST) – zapis formularza
#Kod, który ma wysyłać informację, niech po prostu zapisze tę wiadomość na konsoli.
from flask import Flask
from flask import request, redirect, render_template
import random

app1=Flask(__name__)

@app1.route('/mypage/me', methods=['GET'])
def about_me():
    return render_template("1stside.html")

@app1.route('/mypage/contact', methods=['GET'])
def contact_me():
    return render_template("2ndside.html")

@app1.route('/mypage/contactmeform', methods=['GET','POST'])
def contact_me_form():
    if request.methods=='POST':
        print(request.form)
        return redirect("/mypage/contactmeform")
    return render_template("3rdside.html")
        
if __name__ == "__main__":
    app1.run()
