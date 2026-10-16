
<?php
//le test_api n'est pas exploitable on veut afficher les données sous forme de tableau 
$url = "http://127.0.0.1:5001/students";
$response = file_get_contents($url);

// Décodage du JSON en tableau PHP
$students = json_decode($response, true);

echo "<pre>"; //on fait des retour à la ligne pour la visibilité
print_r($students);
echo "</pre>";

?>
