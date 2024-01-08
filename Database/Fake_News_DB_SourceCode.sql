DROP TABLE processed_data;

CREATE TABLE processed_data (
    title_text VARCHAR,
    label INT
   
    
);

ALTER TABLE processed_data ADD COLUMN id SERIAL PRIMARY KEY;

SELECT * FROM processed_data