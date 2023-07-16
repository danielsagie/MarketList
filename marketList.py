from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketList.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    item = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(length=30), nullable=False, unique=True)
    quantity = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item {self.type}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/list')
def list_page():
    items = Item.query.all()
    return render_template('list.html', items=items)
