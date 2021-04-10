DROP PROCEDURE IF EXISTS pattern;
DELIMITER $$
CREATE PROCEDURE pattern()
BEGIN
    DECLARE x  INT;
    SET x = 20;
    loop_label:  LOOP
        IF  x < 1 THEN 
            LEAVE  loop_label;
        END  IF;
        SELECT REPEAT('* ', x);
        SET  x = x - 1;               
    END LOOP ;
END$$
DELIMITER ;
CALL pattern();

/*
SET @NUMBER = 21;
SELECT REPEAT('* ', @NUMBER := @NUMBER - 1)
    FROM information_schema.tables LIMIT 20;
*/