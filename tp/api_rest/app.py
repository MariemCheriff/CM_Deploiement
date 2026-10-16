
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



# Afficher un étudiant sachant son identifiant
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)

    if student:
        return jsonify(student)

    return jsonify({"erreur": "L'étudiant n'existe pas !"}), 404



# Modifier un étudiant (PUT)
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)

    if not student:
        return jsonify({"message": "Étudiant non trouvé !"}), 404

    data = request.get_json()
    student.update(data)  # Mise à jour des données

    return jsonify(student), 200

#supprimer un étudiant 
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student=next((s for s in students if s['id']==id),None)

    if not student:
        return jsonify({"error: etudiant non trouvé"}),404

    students.remove(student)
    return jsonify({"message": "Étudiant supprimé avec succès !"}), 200


# Lancer le serveur
# Force Flask à écouter sur toutes les interfaces (IPv4 + IPv6) :
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)