from flask import Flask, render_template, request
import requests

app = Flask(__name__)

tasks = []
speech_text = "Click button to record speech. Say 'stop recording' to stop."
image_link = None  # Store the Google Image link


def get_google_image(query, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "cx": cse_id,
        "key": api_key,
        "searchType": "image",
        "num": 1,  # Number of results to return
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "items" in data:
        return data["items"][0]["link"]  # Return the first image link
    else:
        return "No images found"


@app.route('/', methods=['GET', 'POST'])
def index():
    global tasks, speech_text, image_link

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
        elif 'get_image' in request.form:
            speech_text = request.form['get_image'].strip()

            # Query Google Images using the speech text
            api_key = "AIzaSyBE6wcvy8UhNDLks0U907DNGW7LfpEx50U"  # Replace with your actual API key
            cse_id = "c1c4057b1d35f4d99"  # Replace with your Custom Search Engine ID
            image_link = get_google_image(speech_text, api_key, cse_id)

    return render_template('index.html', tasks=tasks, speech_text=speech_text, image_link=image_link)


if __name__ == '__main__':
    app.run(debug=True)
