# API REST – Gestion des étudiants

On utilise Flask , un framework Python qui permet de créer facilement les API REST.

L'API REST permet de gérer des étudiants : récupérer la liste des étudiants, ajouter un étudiant, rechercher un étudiant par son identifiant, modifier ses informations et le supprimer.

Elle est comparable à Java RMI, car les deux permettent la communication entre des applications distantes. Cependant, contrairement à Java RMI, qui repose principalement sur des objets et des interfaces Java, l'API REST utilise le protocole HTTP et le format JSON, ce qui facilite l'interopérabilité entre des applications développées dans différents langages.

## Installation

Pour installer Flask, il faut exécuter la commande dans le terminal :

```bash
python -m pip install flask
```

## Exécution

On lance le serveur avec la commande :

```bash
python app.py
```

L'API est accessible à l'adresse : http://127.0.0.1:5001/

## Fonctionnalités

- `GET /` : vérifier que le serveur fonctionne.
- `GET /students` : récupérer tous les étudiants.
- `POST /students` : ajouter un étudiant.
- `GET /students/<id>` : récupérer un étudiant par son identifiant.
- `PUT /students/<id>` : modifier les informations d'un étudiant.
- `DELETE /students/<id>` : supprimer un étudiant.

**Attention :`/students` est le nom de la route de l'API. Il ne correspond pas directement à la variable Python locale `students`, même si cette variable contient la liste des étudiants utilisée par les fonctions. C'est plutot une bonne pratique.

## Test de l'API REST avec Postman

Pour tester l'API, on peut utiliser Postman, en choisissant la méthode HTTP correspondante et l'URL de la ressource.

- GET : `http://127.0.0.1:5001/students` pour afficher tous les étudiants.
- POST : `http://127.0.0.1:5001/students` pour ajouter un étudiant.
- GET : `http://127.0.0.1:5001/students/1` pour afficher l'étudiant d'identifiant 1.
- PUT : `http://127.0.0.1:5001/students/1` pour modifier l'étudiant d'identifiant 1.
- DELETE : `http://127.0.0.1:5001/students/1` pour supprimer l'étudiant d'identifiant 1.

Pour les requêtes POST et PUT, sélectionner `Body`, puis `raw` et `JSON` dans Postman.

Exemple de données JSON :

```json
{
  "name": "Meriem",
  "age": 22
}
```

Cliquer sur Send pour envoyer la requête et consulter la réponse du serveur.

!!! : 

On peut aussier tester sur le terminal : 
curl -X TYPE_METHODE URL_ROUTE

Les étudiants sont stockés dans une liste Python en mémoire. Les modifications et les ajouts sont donc perdus lorsque le serveur est arrêté ou redémarré.

## Test de l'API REST avec PHP et XAMPP (tets_api)

Il est possible de tester l'API REST depuis un client PHP. XAMPP fournit PHP et le serveur web Apache nécessaires pour exécuter le fichier `test_api.php`.

### 1. Créer le fichier PHP

Créer un fichier `test_api.php` dans le dossier `htdocs` de XAMPP, par exemple `C:\xampp\htdocs\test_api.php`.

```php
<?php
$url = "http://localhost:5001/students";

$response = file_get_contents($url);

echo "<pre>";
echo $response;
echo "</pre>";
?>
```

### 2. Exécuter le test

- Démarrer **Apache** depuis le panneau de contrôle XAMPP.
- Démarrer le serveur Flask avec la commande `python test.py`.
- Ouvrir le navigateur à l'adresse suivante : http://localhost/test_api.php

Le fichier PHP envoie une requête HTTP GET à l'API Flask et affiche la liste des étudiants au format JSON.

Remarque : Flask doit être démarré sur le port `5001`, conformément à la configuration de l'application.


### Test de l'API avec PHP (test_api_1)

Le fichier `test_api.php` permet de récupérer la liste des étudiants depuis l'API Flask et d'afficher les données sous forme json.

Le fichier `test_api_1.php` est une version améliorée qui affiche les étudiants dans un tableau.

Les deux fichiers utilisent `file_get_contents()` pour envoyer une requête HTTP GET et `json_decode()` pour convertir la réponse JSON en tableau PHP.



### 3. Test de l'API avec PHP : test_api3.php


Le fichier `config.php` centralise l'adresse de l'API :

```php
<?php
define('API_BASE_URL', 'http://127.0.0.1:5001');
```


**Explication du fonctionnement :**

- `require_once` charge le fichier `config.php`, qui contient l'adresse de l'API.
- `API_BASE_URL . '/students'` construit l'URL de la route Flask.


ça permet d'utiliser un fichier de configuration séparé afin de centraliser l'adresse de l'API.


### Utilisation de la POO avec StudentService :test_api4.php

La classe `StudentService` centralise la récupération des étudiants depuis l'API REST Flask grâce à la méthode statique `getAllStudents()`.
ça permet de : 
- Réutilisation du code.
- Code plus lisible et plus facile à maintenir et à évoluer.

La méthode étant `static`, elle peut être appelée directement avec `StudentService::getAllStudents()`, sans créer d'objet.


### Séparation du contrôleur et de la vue

Le fichier test_api5.php joue le rôle de contrôleur : il récupère les données des étudiants via StudentService , puis les transmet à la vue views/students.php pour l'affichage.

utilité : séparer la récupération des données de leur affichage, rendre le code plus lisible et faciliter sa maintenance. Cette organisation suit le principe de l'architecture MVC (Modèle, Vue, Contrôleur).