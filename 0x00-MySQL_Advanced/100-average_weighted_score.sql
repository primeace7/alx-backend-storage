-- compute weighted average of students
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN users_id INT)
DEFINE user_total INT;
SET user_total = SELECT SUM(score) FROM corrections WHERE user_id = users_id
