from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0) # this columns is never used, could be ignored
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): # Everytime we create an element this function returns the task and the Id of the task created
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET']) # to get and post data to the database
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content) # To get the input content and add to the database

        try:
            db.session.add(new_task) # add the new_task variable
            db.session.commit() # save to database
            return redirect('/') # return to index page
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # to look / query the database, ordering by the date created and return all the contents
        return render_template("index.html", tasks=tasks) # tasks=tasks is to pass the db content into the index html table

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) # get the task by id, and if doesn't exist will give a 404

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task_to_update.content = request.form['content']

        try:
            # db.session.update(task_to_update)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem when updating your task'
    else:
        return render_template('update.html', task=task_to_update)

if __name__ == "__main__":
    app.run(debug=True)