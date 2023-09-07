from flask import Flask, render_template
import gradio as gr

app = Flask(__name__)

# Define your Gradio interface
def greet(name):
    return f"Hello, {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# Define a route for your Gradio interface
@app.route("/")
def gradio_interface():
    return render_template("interface.html")

# Start the Gradio interface when the Flask app is run
@app.before_first_request
def activate_gradio_interface():
    iface.launch()

if __name__ == "__main__":
    app.run()

