<h1>Liste des étudiants</h1>

<ul>
    <?php foreach ($students as $student): ?>
        <li>
            <?= htmlspecialchars($student['name']) ?>
            (<?= htmlspecialchars((string)$student['age']) ?> ans)
        </li>
    <?php endforeach; ?>
</ul>