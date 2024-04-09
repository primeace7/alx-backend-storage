-- update student scores with AddBonus stored procedure
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(50), IN score INT)

BEGIN
DECLARE proj_id INT;
IF !(SELECT project_name IN (SELECT name FROM projects)) THEN
INSERT INTO projects (name) VALUES(project_name);
END IF;

SET proj_id = (SELECT id FROM projects
WHERE name = project_name
LIMIT 1);
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, proj_id, score);

END
//

DELIMITER ;
