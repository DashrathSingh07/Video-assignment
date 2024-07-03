from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
from datetime import datetime

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend')
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/videocollab"
mongo = PyMongo(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = file.filename
        file.save(os.path.join(app.static_folder, 'uploads', filename))
        return 'File uploaded', 200

@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()  # Add current timestamp
    data.pop('time', None)  # Remove 'time' if it exists
    print("Received comment via POST:", data)  # Debugging line
    result = mongo.db.comments.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return jsonify({'status': 'Comment added'}), 200

@app.route('/comments', methods=['GET'])
def get_comments():
    comments = mongo.db.comments.find()
    comments_list = []
    for comment in comments:
        comment['_id'] = str(comment['_id'])
        comments_list.append(comment)
    return jsonify(comments_list), 200

@socketio.on('addComment')
def handle_add_comment(json):
    json['timestamp'] = datetime.now().isoformat()  # Add current timestamp
    json.pop('time', None)  # Remove 'time' if it exists
    print("Received comment via WebSocket:", json)  # Debugging line
    result = mongo.db.comments.insert_one(json)
    json['_id'] = str(result.inserted_id)
    emit('newComment', json, broadcast=True)

if __name__ == '__main__':
    if not os.path.exists(os.path.join(app.static_folder, 'uploads')):
        os.makedirs(os.path.join(app.static_folder, 'uploads'))
    socketio.run(app, debug=True)
