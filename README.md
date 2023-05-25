# DIS_Project
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
COPY Laptops(L_ID, Company, Product, TypeName, Inches, Resolution, CPU, RAM, Memory, GPU, OpSys, Weight, Price_Euros) FROM '/home/rune/Documents/DIS/Project/CLEANED_laptop_price.csv' DELIMITER ',';

DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
    u_id int GENERATED ALWAYS AS IDENTITY,
    username VARCHAR,
    userpassword VARCHAR,
    PRIMARY KEY (u_id)
);
```
