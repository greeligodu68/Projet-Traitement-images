import os  
from flask import Flask, request, send_file, render_template, redirect, url_for  
from Filtre_Python.conversion_gris import convert_gray,filtreMoyenneur
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Crée le dossier s'il n'existe pas



@app.route('/', methods=['GET', 'POST']) # ca c'est la page de base 
def upload_file():
    if request.method == 'POST' and 'file' in request.files:  
        file = request.files['file']  
        if file.filename : 
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # Crée le chemin pour enregistrer le fichier
            file.save(file_path)  # Sauvegarde l'image dans le dossier créé juste avant 
            return redirect(url_for('upload_file', filename=file.filename))  # Recharge la page avec l'image envoyée
    
    filename = request.args.get('filename')  # Récupère le nom du fichier pour l'afficher après redirection
    return render_template('index.html', filename=filename) 


@app.route('/convert-gray/<filename>', methods=['GET', 'POST'])
def convert_to_gray(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)  # Chemin de l'image d'origine
    output_path = convert_gray(input_path)   # Exécute la fonction pour convertir en gris
    new_filename = os.path.basename(output_path) 
    return redirect(url_for('upload_file', filename=new_filename))     # Recharge la page avec l'image traitée

@app.route('/filtre-moyenneur/<filename>', methods=['GET', 'POST'])
def filtre_moyenneur_image(filename):
    input_path = os.path.join(UPLOAD_FOLDER, filename)  
    output_path = filtreMoyenneur(input_path, filterSize=3)  
    new_filename = os.path.basename(output_path) 
    return redirect(url_for('upload_file', filename=new_filename))  

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)  # Envoie le fichier en téléchargement
                                                                                # as attachement permet de forcer le téléchargement et non pas just afficher
if __name__ == '__main__':
    app.run(debug=True)
