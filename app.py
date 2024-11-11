from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []
speech_text = "Click button to record speech. Say 'stop recording' to stop."

@app.route('/', methods=['GET', 'POST'])
def index():
    global tasks, speech_text

    if request.method == 'POST':
        if 'add_task' in request.form:
            task = request.form['task'].strip()
            tasks.append({'task': task, 'done': False})
        elif 'mark_done' in request.form:
            index = int(request.form['mark_done'])
            if 0 <= index < len(tasks):
                tasks[index]['done'] = True
        elif 'remove_task' in request.form:
            index = int(request.form['remove_task'])
            if 0 <= index < len(tasks):
                tasks.pop(index)
        elif 'speech_input' in request.form:
            speech_text = "Click button to record speech. Say 'stop recording' to stop."

    return render_template('index.html', tasks=tasks, speech_text=speech_text)

if __name__ == '__main__':
    app.run(debug=True)
