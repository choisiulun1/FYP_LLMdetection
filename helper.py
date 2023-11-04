from threading import Thread
import subprocess


class VueHelper:
    def __init__(self, port=5001):
        self.port = port

    def __start_vue_server(self):
        print(f"npm run serve --port {self.port}")
        process = subprocess.Popen(f"npm run serve -- --port {self.port}", shell=True, cwd="front-end")
        return process

    def start(self):
        self.thread = Thread(target=self.__start_vue_server)
        self.thread.start()


class GradioHelper:
    def __init__(self, iface, host="0.0.0.0",port=1234 ):
        self.port = port
        self.iface = iface
        self.host = host

    def __start_gradio_server(self):
        print(self.host)
        self.iface.launch(inline=True, server_name=self.host, server_port=self.port,share=True)

    def start(self):
        self.thread = Thread(target=self.__start_gradio_server)
        self.thread.start()
