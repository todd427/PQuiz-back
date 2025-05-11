from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = "submissions.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/api/submit", methods=["POST"])
def receive_submission():
    data = request.get_json()
    data['received_at'] = datetime.utcnow().isoformat()
    with open(DATA_FILE, "r+") as f:
        submissions = json.load(f)
        submissions.append(data)
        f.seek(0)
        json.dump(submissions, f, indent=2)
    return jsonify({"message": "Submission received", "status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
