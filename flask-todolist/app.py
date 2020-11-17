from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#convention
app = Flask(__name__)

#config databse
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite' #///=relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    # class of modifying database inherit from db.Model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100)) #max_len=100
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    # define index pag, flask will search the html in /templates fold
    #show all todos
    todo_list = Todo.query.all()
    return render_template('base.html', todolist=todo_list)

@app.route("/add", methods=["POST"])
def add():
    #add new item
    title = request.form.get("title")
    new_todo = Todo(title=title,complete = False)
    db.session.add(new_todo)
    db.session.commit()
    #after add redirect to the index page
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    #return one object
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    #after add redirect to the index page
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    #return one object
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    #after add redirect to the index page
    return redirect(url_for("index"))


@app.route('/about')
def about():
    # show string About on */about url
    return "About"

#another way to run flask app in command line
#export FLASK_APP=app.py
#export FLASK_ENV=development
#flask run
if __name__ == "__main__":
    #create database
    db.create_all()
    '''
    #store a To-do object to the database
        new_todo = Todo(title="todo 1",complete=False)
        db.session.add(new_todo)
        db.session.commit()
    '''

    app.run(debug=True)