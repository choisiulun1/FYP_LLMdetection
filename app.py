from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
import gradio as gr
from threading import Thread
import subprocess
from helper import GradioHelper, VueHelper

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/api/*": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000", "*"]}
    },
)


@app.route("/")
def index():
    # Embed the Gradio interface
    return render_template_string(
        """
        <!doctype html>
        <html>
        <head>
            <title>Gradio in Flask</title>
        </head>
        <body>
            <iframe src="http://localhost:1234/" width="100%" height="500px" style="border:none;"></iframe>
        </body>
        </html>
    """
    )


@app.route("/api/data")
def get_data():
    return jsonify({"data": "Hello from Flask!"})

iface = gr.Interface(fn=index, inputs="text", outputs="text")
gradio = GradioHelper(iface, port=1234)
gradio.start()
vue = VueHelper(port=5001)
vue.start()


if __name__ == '__main__':
    app.run(debug=True,port=5000)
