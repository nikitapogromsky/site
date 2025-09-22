from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> web-site </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(to right, #74ebd5, #9face6);
            color: #222;
            margin-top: 15%;
        }
        h1 {
            font-size: 2.5em;
        }
        #time {
            font-size: 1.8em;
            margin-top: 20px;
        }
    </style>
    <script>
        function updateTime() {
            fetch("/time")
                .then(response => response.text())
                .then(data => {
                    document.getElementById("time").innerText = data;
                });
        }
        setInterval(updateTime, 1000);
        window.onload = updateTime;
    </script>
</head>
<body>
    <h1>Hello, this is my mini site</h1>
    <p>Time now:</p>
    <div id="time">Loading...</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

@app.route('/time')
def time():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")

if __name__ == '__main__':
    app.run(debug=True)
