from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask.helpers import url_for

import csv
import os
import uuid

import sprinter.data_handler as data_handler

app = Flask(__name__)

@app.route('/story', methods=['GET'])
def show_add_form():
    statuses = data_handler.get_status_list()    
    return render_template("form.html", statuses=statuses, story={})


@app.route('/story', methods=['POST'])
def create_story():
    new_story = {
        "id" : uuid.uuid1(),
        "title" : request.form['title'],
        "description" : request.form['description'],
        "criteria" :request.form['criteria'],
        "business_value" : request.form['business_value'],
        "estimation" :request.form['estimation'],
        "status" :request.form['status']
    }
    
    data_handler.add_story(new_story)
    
    return redirect(url_for('show_list'))


@app.route('/story/<story_id>', methods=['GET'])
def show_edit_form(story_id):
    statuses = data_handler.get_status_list()    
    story = data_handler.get_story_by_id(story_id)
    
    return render_template("form.html", statuses=statuses, story=story)


@app.route('/story/<story_id>', methods=['POST'])
def show_update_form(story_id):
    updated_story =  {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "criteria" :request.form['criteria'],
        "business_value" : request.form['business_value'],
        "estimation" :request.form['estimation'],
        "status" :request.form['status']
        }
    
    data_handler.update_story(story_id, updated_story)
    
    return redirect(url_for("show_list"))


@app.route('/story/<story_id>/delete', methods=['GET'])
def delete_story(story_id):
    data_handler.delete_story(story_id)

    return redirect(url_for("show_list"))


@app.route('/')
@app.route('/list')
def show_list():
    stories = data_handler.get_user_story_list()
     
    return render_template("list.html", stories=stories)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""

    data_handler.set_default_statuses()
    data_handler.clear_user_stories()

    print('Initialized the database.')
