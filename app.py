import os  
from flask import Flask, request, send_file, render_template, redirect, url_for  
from Filtre_Python.filtre_app import( convert_gray, filtreMoyenneur,filtre_Erosion,gradient_Morphologique,
filtre_Dilatation,filtre_Edgedetection,filtre_Cartoon,contraste,oil_paint)
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    filename = None
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file.filename:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            return redirect(url_for('upload_file', filename=file.filename))

    filename = request.args.get('filename')
    processed_filename = request.args.get('processed_filename')
    return render_template('index2.html', filename=filename, processed_filename=processed_filename)



@app.route('/convert-gray/<filename>',methods=['GET', 'POST'])
def convert_to_gray(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"gray_{filename}")
    shutil.copy(input_path, output_path)
    processed_output = convert_gray(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))



@app.route('/filtre-moyenneur/<filename>',methods=['GET', 'POST'])
def filtre_moyenneur_image(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"filtered_{filename}")
    shutil.copy(input_path, output_path)
    processed_output = filtreMoyenneur(output_path, filterSize=3)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))

@app.route('/filtre-erosion/<filename>',methods=['GET', 'POST'])
def filtre_erosion(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"erosion_{filename}")
    shutil.copy(input_path, output_path)

    processed_output = filtre_Erosion(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/filtre-dilation/<filename>',methods=['GET', 'POST'])
def filtre_dilation(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"dilation_{filename}")
    shutil.copy(input_path, output_path)

    processed_output = filtre_Dilatation(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))

@app.route('/gradient_morphologique/<filename>',methods=['GET', 'POST'])
def gradient_morphologique(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"gradient_{filename}")
    shutil.copy(input_path, output_path)

    processed_output = gradient_Morphologique(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/edge_detection/<filename>',methods=['GET', 'POST'])
def edge_detection(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"edge_detection_{filename}")
    shutil.copy(input_path, output_path)

    processed_output = filtre_Edgedetection(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/filtre-cartoon/<filename>',methods=['GET', 'POST'])
def filtre_cartoon(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    output_path = os.path.join(UPLOAD_FOLDER, f"cartoon{filename}")
    shutil.copy(input_path, output_path)

  
    processed_output = filtre_Cartoon(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/filtre-contraste/<filename>',methods=['GET', 'POST'])
def filtre_contraste(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)


    output_path = os.path.join(UPLOAD_FOLDER, f"contrast{filename}")
    shutil.copy(input_path, output_path)


    processed_output = contraste(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/filtre-oil_painting/<filename>',methods=['GET', 'POST'])
def filtre_oil_painting(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)

  
    output_path = os.path.join(UPLOAD_FOLDER, f"oil_paint{filename}")
    shutil.copy(input_path, output_path)

    processed_output = oil_paint(output_path)
    
    new_filename = os.path.basename(processed_output)
    return redirect(url_for('upload_file', filename=filename, processed_filename=new_filename))


@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
