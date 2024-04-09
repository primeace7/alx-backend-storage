-- create and index on the first letter of names column and score column
CREATE INDEX idx_name_first_score
ON names(name(1), score);
