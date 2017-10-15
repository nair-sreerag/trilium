from flask import Blueprint, jsonify
from flask_login import login_required

from sql import getResults

notes_history_api = Blueprint('notes_history_api', __name__)


@notes_history_api.route('/api/notes-history/<string:note_id>', methods = ['GET'])
@login_required
def get_note_history(note_id):
    history = getResults("select * from notes_history where note_id = ? order by date_modified desc", [note_id])

    return jsonify(history)


@notes_history_api.route('/api/recent-changes/', methods = ['GET'])
@login_required
def get_recent_changes():
    recent_changes = getResults("select * from notes_history order by date_modified desc limit 1000")

    return jsonify(recent_changes)