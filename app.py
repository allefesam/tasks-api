from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória para armazenar tarefas
tasks = []
task_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': task_id,
        'title': data['title'],
        'done': False
    }
    tasks.append(task)
    task_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)