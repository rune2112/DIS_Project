# DIS_Project
To run the data you must make a DB_cred.json file:
{"dbname": "postgres", "user": "postgres", "host": "127.0.0.1", "password": "%password for database%"}

To run the app:
Run the script "run.py" in the root folder

To create the database, run:
```
DROP TABLE IF EXISTS Laptops;
CREATE TABLE Laptops(
    L_ID int,
    Company VARCHAR,
    Product VARCHAR,
    TypeName VARCHAR,
    Inches numeric,
    Resolution VARCHAR,
    CPU VARCHAR,
    RAM int,
    Memory VARCHAR,
    GPU VARCHAR,
    OpSys VARCHAR,
    Weight numeric,
    Price_Euros numeric,
    PRIMARY KEY (L_ID)
);
COPY Laptops(L_ID, Company, Product, TypeName, Inches, Resolution, CPU, RAM, Memory, GPU, OpSys, Weight, Price_Euros) FROM '%PATH%/CLEANED_laptop_price.csv' DELIMITER ',';

ALTER TABLE laptops ADD username VARCHAR;

UPDATE laptops SET username = 'admin';

DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
    u_id int GENERATED ALWAYS AS IDENTITY,
    username VARCHAR,
    userpassword VARCHAR,
    PRIMARY KEY (u_id)
);

DROP TABLE IF EXISTS cart;
CREATE TABLE cart(
	c_id int GENERATED ALWAYS AS IDENTITY,
	u_id int,
	l_id int,
	PRIMARY KEY (c_id)
);
```
