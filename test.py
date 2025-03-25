from flask import Flask, render_template, request, redirect, url_for
from login_form import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
id_kap = 'admin'
password_kap = 'admin'


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if form.id_kap.data == id_kap and form.password_kap.data == password_kap:
            return render_template('auto_answer.html', form=form, id_kap=id_kap, password_kap=password_kap)
        return render_template('login.html', form=form, err='Данные не совпадают')
    return render_template('login.html', form=form, err='')




if __name__ == '__main__':
    app.run(port=5252, host='127.0.0.1')