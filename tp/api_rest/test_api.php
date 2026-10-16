
<?php
$url = "http://localhost:5001/students"; #l'url et il faut préciser le port 
#envoie une requete GET à l'url
$response = file_get_contents($url);

echo "<pre>"; #permet retour à la ligne
echo $response; #afficher réponse 
echo "</pre>";
?>
