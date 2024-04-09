-- create trigger to update item quantity after order
DELIMITER //
//
CREATE TRIGGER IF NOT EXISTS update_items
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
END
//
DELIMITER ;
