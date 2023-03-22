
SELECT id AS 'identifier', first_name AS 'First Name', last_name AS 'Last Name'
FROM users;

SELECT id AS 'Identifier', CONCAT(first_name, ' ', last_name) AS 'Full Name'
FROM users;

SELECT id, first_name, last_name
FROM users;

SELECT *
FROM users;

INSERT INTO users(first_name, last_name)
VALUES('Bentley', 'Nam');

INSERT INTO users(first_name, last_name)
VALUES ('Joanne', 'Lee'),
	('Andrew', 'Park'),
       ('Dahvin', 'Yim');
       
SELECT *
FROM users
WHERE first_name = 'Jung' AND last_name = 'Nam';

SELECT *
FROM users
WHERE id > 2;

UPDATE users
SET last_name = 'Lee', first_name = 'Joanne'
WHERE id = 2;

DELETE FROM users
WHERE id = 5;

SELECT *
FROM users;

INSERT INTO todos(name, status, user_id)
VALUES('Leanring Flask', 'complete',1),
      ('Leanring Routes', 'complete',1),
      ('Leanring Sessions', 'complete',2),
      ('Leanring POST', 'complete',3),
      ('Leanring SQL', 'in_progress',1),
      ('Leanring ERD', 'in_progess',2);
      
SELECT u.first_name, u.last_name, t.name, t.status
FROM todos t
	JOIN users u ON t.user_id = u.id
WHERE u.id = 1;

SELECT *
FROM todos, users
WHERE todos.user_id = users.id AND users.id = 1;

SELECT u.first_name, u.last_name, t.name, t.status
FROM users u
	LEFT JOIN todos t ON t.user_id = u.id;

SELECT u.first_name, COUNT(t.user_id) AS 'Num of todos'
FROM users u
	JOIN todos t ON u.id = t.user_id
GROUP BY(u.first_name)
ORDER BY u.first_name DESC;

