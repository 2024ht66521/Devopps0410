from flask import Flask, request, jsonify, render_template_string
from threading import Lock

app = Flask(__name__)
workouts = []
lock = Lock()

INDEX_HTML = """
<!doctype html>
<title>ACEest Fitness</title>
<h1>ACEest Fitness & Gym</h1>
<form id="addForm" method="post" action="/api/workouts">
  Workout name: <input name="workout" required>
  Duration (minutes): <input name="duration" type="number" required>
  <button type="submit">Add Workout</button>
</form>
<h2>Logged Workouts</h2>
<ul id="list">
{% for w in workouts %}
  <li>{{ loop.index }}. {{ w.workout }} - {{ w.duration }} minutes</li>
{% else %}
  <li>No workouts logged yet.</li>
{% endfor %}
</ul>
"""

@app.route('/')
def index():
    return render_template_string(INDEX_HTML, workouts=workouts)

@app.route('/api/workouts', methods=['GET', 'POST'])
def api_workouts():
    if request.method == 'GET':
        return jsonify(workouts)
    data = request.get_json() if request.is_json else request.form
    workout = data.get('workout')
    duration = data.get('duration')
    if not workout or not duration:
        return jsonify({'error': 'workout and duration required'}), 400
    try:
        duration_int = int(duration)
    except ValueError:
        return jsonify({'error': 'duration must be an integer'}), 400
    entry = {'workout': workout, 'duration': duration_int}
    with lock:
        workouts.append(entry)
    return jsonify(entry), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
