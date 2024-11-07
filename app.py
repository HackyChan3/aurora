from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize global variables
tasks = []
timer = {'hours': 0, 'minutes': 0, 'seconds': 0}
speech_text = "Click button to record speech. Say 'stop recording' to stop."

@app.route('/', methods=['GET', 'POST'])
def index():
    global tasks, timer, speech_text  # Declare them as global to modify them

    if request.method == 'POST':
        if 'add_task' in request.form:
            task = request.form['task'].strip()
            tasks.append({'task': task, 'done': False})
        elif 'set_timer' in request.form:
            timer['hours'] = int(request.form['hours'])
            timer['minutes'] = int(request.form['minutes'])
            timer['seconds'] = int(request.form['seconds'])
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
            print(request.form)
            print(speech_text)

    # Render the template with current tasks, timer, and speech text
    print(tasks)
    return render_template('index.html', tasks=tasks, timer=timer, speech_text=speech_text)

if __name__ == '__main__':
    app.run(debug=True)
