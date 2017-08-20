from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask.helpers import url_for

from sprinter.connectdatabase import ConnectDatabase
from sprinter.models import Status, UserStory

app = Flask(__name__)


@app.route('/story', methods=['GET'])
def show_add_form():
    statuses = Status.select()
    return render_template("form.html", statuses=statuses, story={})


@app.route('/story', methods=['POST'])
def create_story():
    new_story = UserStory.create(
        title=request.form['title'],
        description=request.form['description'],
        criteria=request.form['criteria'],
        business_value=request.form['business_value'],
        estimation=request.form['estimation'],
        status=request.form['status']
    )
    if (new_story):

        return redirect(url_for('show_list'))


@app.route('/story/<story_id>', methods=['GET'])
def show_edit_form(story_id):
    statuses = Status.select()
    story = UserStory.get(id=story_id)

    return render_template("form.html", statuses=statuses, story=story)


@app.route('/story/<story_id>', methods=['POST'])
def show_update_form(story_id):
    story = UserStory.get(id=story_id)
    story.title = request.form['title']
    story.description = request.form['description']
    story.criteria = request.form['criteria']
    story.business_value = request.form['business_value']
    story.estimation = request.form['estimation']
    story.status = request.form['status']
    story.save()

    return redirect(url_for("show_list"))


@app.route('/story/<story_id>/delete', methods=['GET'])
def delete_story(story_id):
    story = UserStory.get(id=story_id)
    story.delete_instance()

    return redirect(url_for("show_list"))


@app.route('/')
@app.route('/list')
def show_list():
    stories = UserStory.select()
    #stories = read_stroy_from_file(erp)
    return render_template("list.html", stories=stories)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    ConnectDatabase.db.connect()
    ConnectDatabase.db.create_tables([UserStory, Status], safe=True)
    Status.create(name="Planning")
    Status.create(name="To Do")
    Status.create(name="Done")
    Status.create(name="In Progress")
    Status.create(name="Review")
    print('Initialized the database.')
