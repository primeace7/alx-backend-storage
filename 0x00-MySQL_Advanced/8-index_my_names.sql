-- create an index with first letter of names column
CREATE INDEX idx_name_first
ON names(name(1));
