-- create stored routine to compute average score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN users_id INT)
BEGIN

DECLARE user_avg FLOAT;
SET user_avg = (SELECT AVG(score) FROM corrections WHERE user_id = users_id);

UPDATE users
SET average_score = user_avg
WHERE id = users_id;

END //

DELIMITER ;
