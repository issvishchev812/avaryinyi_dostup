from flask import Flask, render_template, request, redirect, url_for
from login_form import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'



@app.route('/distribution', methods=['GET', 'POST'])
def index():
    astronauts = ['Риддли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандрес', 'Шон Бин']
    return render_template('distribution.html', arr=astronauts)





if __name__ == '__main__':
    app.run(port=5252, host='127.0.0.1')