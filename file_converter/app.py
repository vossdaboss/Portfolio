from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_file():
    if request.method == 'POST':
        input_path_full = request.form['input_path']
        output_path_full = request.form['output_path']
        input_format = request.form['input_format']
        output_format = request.form['output_format']

        cmd = ['python', 'convert_file.py', input_path_full, output_path_full, input_format, output_format]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            output_path_full = os.path.join('output', output_path_full)  # update output path to new location
            if output_format == 'json' or output_format == 'csv' or output_format == 'xml' or output_format == 'SQL':
                return send_file(output_path_full, as_attachment=True)
        else:
            result.stderr

    return render_template('index.html')