CREATE TABLE table_name(
    Column1 datatype,
    Column2 datatype,
    Column3 datatype
)
INSERT INTO table_name(Column1, Column2, Column3)
values
('value1','value2','value3'),
('value1','value2','value3'),
('value1','value2','value3');


CREATE TABLE Students(
    StudentID INT NOT NULL AUTO_INCREMENT,
    FullName NOT NULL VARCHAR (30),
    Email NOT NULL VARCHAR (30),
    PhoneNumber VARCHAR (13),
    Age VARCHAR (3),
    Gender VARCHAR(6),
    BirthDate DATE,
    City NOT NULL VARCHAR (20),
    PinCode VARCHAR(6),
    Roll VARCHAR(15)
    PRIMARY KEY (studentID),
)
INSERT INTO Students(StudentID, FullName, Email, PhoneNumber, Age, BirthDate, City, PinCode, Roll)
values
(1, 'Ram','ramkumar1234@gmail.com', '9576619184', 23, '23-12-1997', 'Kusunda', '828116', '1'),
(2, 'Sourav','souravbiswas1234@gmail.com', '9576619185',24, '23-07-1997', 'Dhanbad', '828116', '2'),
(3, 'Vishal','vishalsingh1234@gmail.com', '9576619186', 25, '23-12-1996', 'Dhanbad', '828116', '3'),
(4, 'Asif','asifnasim1234@gmail.com', '9576619187', 26, '23-12-1995', 'Jhariya', '828116', '4'),
(5, 'Mayank','mayankgupta1234@gmail.com', '9576619188', 28, '23-12-1994', 'Kendua', '828116', '5');