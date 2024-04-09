-- validate user email
DELIMITER //
CREATE TRIGGER validate_email
BEFORE UPDATE ON
users FOR EACH ROW
BEGIN
IF CHAR_LENGTH(NEW.email) != 0 AND OLD.valid_email = 0 THEN
SET NEW.valid_email = !OLD.valid_email;
END IF;
END//
DELIMITER ;
