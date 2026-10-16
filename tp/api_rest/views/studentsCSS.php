<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Liste des étudiants</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>

    <h1>Liste des étudiants</h1>

    <ul>
        <?php foreach ($students as $student): ?>
            <li>
                <?= htmlspecialchars($student['name']) ?>
                (<?= htmlspecialchars((string)$student['age']) ?> ans)
            </li>
        <?php endforeach; ?>
    </ul>

    <!-- PHP fournit les données -->
    <!-- HTML structure la page -->
    <!-- CSS embellit la présentation -->

</body>
</html>