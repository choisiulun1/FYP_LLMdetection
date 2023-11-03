from flask import Flask, jsonify,render_template_string
from flask_cors import CORS
import gradio as gr
from threading import Thread
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000","*"]}})

@app.route('/')
def index():
    # Embed the Gradio interface
    return render_template_string("""
        <!doctype html>
        <html>
        <head>
            <title>Gradio in Flask</title>
        </head>
        <body>
            <iframe src="http://0.0.0.0:1234/" width="100%" height="500px" style="border:none;"></iframe>
        </body>
        </html>
    """)



@app.route('/api/data')
def get_data():
    return jsonify({'data': 'Hello from Flask!'})

def run_gradio():
    iface = gr.Interface(fn=index, inputs="text", outputs="text")
    iface.launch(inline=True, server_name="0.0.0.0", server_port=1234,share=True)

gradio_thread = Thread(target=run_gradio)
gradio_thread.start()

def start_vue_server():
    # This will start the server and immediately return the process object
    process = subprocess.Popen('npm run serve', shell=True, cwd='front-end')
    return process

thread = Thread(target=start_vue_server)
thread.start()



if __name__ == '__main__':
    app.run(debug=True,port=5000)
