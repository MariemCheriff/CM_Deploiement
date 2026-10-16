
from flask import Flask, jsonify, request

# Créer l'application Flask
app = Flask(__name__)

# Liste des étudiants
students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41}
]

# Racine de l'API
#l'equivalent de index.html
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"


# Endpoint pour lister tous les étudiants
@app.route('/students', methods=['GET'])
# Méthode HTTP GET qui permet de retourner la liste des étudiants
def get_students():
    # jsonify transforme la liste students en JSON
    return jsonify(students)


# Ajouter un étudiant (POST)
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()

    # Pour récupérer les données envoyées par le client
    # Attribuer un numéro de manière incrémentable
    new_student['id'] = len(students) + 1

    # Ajouter l'étudiant à la liste
    students.append(new_student)

    return jsonify(new_student), 201
    # Le code 201 pour dire création réussie


# Récupérer un étudiant par son ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Étudiant non trouvé"}), 404


# Lancer le serveur
# Force Flask à écouter sur toutes les interfaces (IPv4 + IPv6) :
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)