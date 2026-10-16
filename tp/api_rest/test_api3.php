
<?php

require_once __DIR__ . '/config.php';

$url = API_BASE_URL . '/students';
$response = file_get_contents($url);

$students = json_decode($response, true);

echo "<h1>Liste des étudiants</h1>";

foreach ($students as $student) {
    echo htmlspecialchars($student['name']) . " - "
       . htmlspecialchars((string)$student['age']) . " ans<br>";
}

?>
