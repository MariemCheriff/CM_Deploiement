# API REST – Gestion des étudiants

Cette application utilise **Flask**, un framework Python qui permet de créer facilement des serveurs et  API REST.

L'API REST permet de gérer des étudiants : récupérer la liste des étudiants, ajouter un étudiant ou rechercher un étudiant par son identifiant.

Elle est comparable à **Java RMI**, car les deux permettent la communication entre des applications distantes. Cependant, contrairement à Java RMI, qui repose principalement sur des objets et des interfaces Java, l'API REST utilise le protocole HTTP et le format JSON, ce qui facilite l'interopérabilité entre des applications développées dans différents langages.

## Installation

 il faut installer flask, il faut écrire dans le temrinal

```bash
python -m pip install flask
```

## Exécution

```bash
python test.py
```

L'API est accessible à l'adresse : http://127.0.0.1:5000/

## Fonctionnalités

- `GET /students` : récupérer tous les étudiants.
- `POST /students` : ajouter un étudiant.
- `GET /students/<id>` : récupérer un étudiant par son identifiant.