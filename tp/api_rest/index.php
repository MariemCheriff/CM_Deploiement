<?php

require_once 'config/config.php';
require_once 'services/StudentService.php';

// Récupération des données
$students = StudentService::getAllStudents();

// Affichage de la vue
require_once 'views/studentsCSS.php';