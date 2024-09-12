GRANT ALL ON library.* to 'root'@'localhost';

CREATE DATABASE library;
USE library;

CREATE TABLE LIBRARY_ORGANIZATION (
OrgAcronym VARCHAR(10) NOT NULL,
Headquarters VARCHAR(20) NOT NULL,
State CHAR(2) NOT NULL,
PRIMARY KEY(OrgAcronym)
);

CREATE TABLE LIBRARY (
LCode INT NOT NULL AUTO_INCREMENT,
Address VARCHAR(20) NOT NULL,
Town VARCHAR(20) NOT NULL,
State CHAR(2) NOT NULL,
PublicStatus BOOLEAN NOT NULL,
OrgAcronym CHAR(4) NOT NULL,
MembershipStartDate DATE NOT NULL,
PRIMARY KEY(LCode),
FOREIGN KEY(OrgAcronym) REFERENCES LIBRARY_ORGANIZATION(OrgAcronym)
);

CREATE TABLE MEMBER (
MID INT NOT NULL AUTO_INCREMENT,
FirstName VARCHAR(20) NOT NULL,
MInit VARCHAR(20),
LastName VARCHAR(20) NOT NULL,
StartDate DATE NOT NULL,
Password VARCHAR(20) NOT NULL,
LCode INT NOT NULL,
PRIMARY KEY(MID),
FOREIGN KEY(LCode) REFERENCES LIBRARY(LCode)
);

CREATE TABLE COMPUTER (
CID INT NOT NULL AUTO_INCREMENT,
Make VARCHAR(20) NOT NULL,
Model VARCHAR(20) NOT NULL,
Year SMALLINT NOT NULL,
SoftwareVersionNum VARCHAR(20) NOT NULL,
OperatingSystem VARCHAR(20) NOT NULL,
LCode INT NOT NULL,
PRIMARY KEY(CID),
FOREIGN KEY(LCode) REFERENCES LIBRARY(LCode)
);

CREATE TABLE BOOK_CATALOG (
ISBN INT NOT NULL AUTO_INCREMENT,
Title VARCHAR(100) NOT NULL,
Subtitle VARCHAR(100),
Year SMALLINT,
AuthorLName VARCHAR(20) NOT NULL,
AuthorFName VARCHAR(20),
AuthorMInit VARCHAR(20),
OrgAcronym VARCHAR(10) NOT NULL,
PRIMARY KEY(ISBN),
FOREIGN KEY(OrgAcronym) REFERENCES LIBRARY_ORGANIZATION(OrgAcronym)
);

CREATE TABLE INVENTORY (
DeweyDecimal INT NOT NULL AUTO_INCREMENT,
Quantity INT NOT NULL,
NumAvailable INT NOT NULL,
LCode INT NOT NULL,
ISBN INT NOT NULL,
PRIMARY KEY(DeweyDecimal),
FOREIGN KEY(LCode) REFERENCES LIBRARY(LCode),
FOREIGN KEY(ISBN) REFERENCES BOOK_CATALOG(ISBN)
);

CREATE TABLE LOGS_IN (
MID INT NOT NULL,
CID INT NOT NULL,
LogOnTime DATETIME NOT NULL,
LogOffTime DATETIME,
PRIMARY KEY(MID, CID),
FOREIGN KEY(MID) REFERENCES MEMBER(MID),
FOREIGN KEY(CID) REFERENCES COMPUTER(CID)
);

CREATE TABLE CHECKS_OUT (
MID INT NOT NULL,
DeweyDecimal INT NOT NULL,
CheckOutDate DATE NOT NULL,
CheckInDate DATE,
DueDate DATE,
PRIMARY KEY(MID, DeweyDecimal),
FOREIGN KEY(MID) REFERENCES MEMBER(MID),
FOREIGN KEY(DeweyDecimal) REFERENCES INVENTORY(DeweyDecimal)
);

-- 11 entries
INSERT INTO LIBRARY_ORGANIZATION VALUES
('OCLN', 'Boston', 'MA'),
('QWER', 'Portland', 'ME'),
('WERT', 'Hartford', 'CT'),
('RILO', 'Providence', 'RI'),
('RTYU', 'New York', 'NY'),
('TYUI', 'Phoenix', 'AZ'),
('YUIO', 'Salem', 'OR'),
('UIOP', 'Richmond', 'VA'),
('IOPA', 'Olympia', 'WA'),
('OPAS', 'Detroit', 'MI'),
('PASD', 'Sacremento', 'CA');

-- 15 entries
INSERT INTO LIBRARY VALUES
(NULL, '123 Apple', 'Palo Alto', 'CA', FALSE, 'PASD', '2011-03-24'),
(NULL, '234 Desk', 'Battle Creek', 'MI', TRUE, 'OPAS', '2009-01-27'),
(NULL, '345 Wood', 'Bellingham', 'WA', FALSE, 'IOPA', '2003-08-03'),
(NULL, '456 Pine', 'Harrisonburg', 'VA', TRUE, 'UIOP', '1999-07-07'),
(NULL, '567 Pear', 'Gresham', 'OR', TRUE, 'YUIO', '2013-04-16'),
(NULL, '678 Grape', 'Scottsdale', 'AZ', FALSE, 'TYUI', '2016-12-08'),
(NULL, '789 Liberty', 'Quincy', 'MA', TRUE, 'OCLN', '2000-11-29'),
(NULL, '890 Old', 'Norwell', 'MA', TRUE, 'OCLN', '2010-07-15'),
(NULL, '321 Wetlands', 'Marshfield', 'MA', TRUE, 'OCLN', '2011-02-04'),
(NULL, '432 Bells', 'Pembroke', 'MA', TRUE, 'OCLN', '2009-04-21'),
(NULL, '543 Anchor', 'Hanover', 'MA', TRUE, 'OCLN', '2011-03-22'),
(NULL, '654 Strawberry', 'Cranston', 'RI', TRUE, 'RILO', '2012-06-27'),
(NULL, '765 Cherry', 'Johnston', 'RI', TRUE, 'RILO', '2014-10-14'),
(NULL, '876 Banana', 'Pawtucket', 'RI', TRUE, 'RILO', '2011-03-24'),
(NULL, '987 Money', 'Newport', 'RI', TRUE, 'RILO', '2008-01-06');

-- 25 Entries
-- Library codes between 1-15
INSERT INTO MEMBER VALUES
(NULL, 'Freddy', 'D', 'Masaru', '2019-05-01', 'efkwq323', 1),
(NULL, 'Anouk', NULL, 'Naseem', '2018-06-02', 'ijdsa', 2),
(NULL, 'Floriana', 'O', 'Shanti', '2017-04-07', '134jnd', 3),
(NULL, 'Tahir', NULL, 'Ottokar', '2020-06-14', '13kfmv878', 4),
(NULL, 'Whitney', 'A', 'Baker', '2021-11-23', 'hgge7h3hd', 5),
(NULL, 'Sebastian', NULL, 'Petar', '2022-09-11', '0knvd3g9', 6),
(NULL, 'Raine', 'B', 'Jaylen', '2022-03-29', '7h6f3fd72', 7),
(NULL, 'Effie', NULL, 'Thor', '2021-11-15', '43fr7qn49', 8),
(NULL, 'Rumen', NULL, 'Ai', '2018-01-09', '63647ndnnfj8', 9),
(NULL, 'Erna', 'R', 'Elizabeth', '2018-12-10', 'effk37eh123', 10),
(NULL, 'Gaby', NULL, 'Aubert', '2017-10-21', 'fjgn873r3', 11),
(NULL, 'Rudolf', NULL, 'Valborg', '2022-02-04', '090987hgggffd', 12),
(NULL, 'Sophea', 'L', 'Indie', '2019-08-06', 'vgedfbged4', 13),
(NULL, 'Lisa', NULL, 'Irina', '2018-09-30', '2df32f2f13', 14),
(NULL, 'Linda', 'R', 'Bendt', '2022-02-09', 'nbbbvffs457923', 15),
(NULL, 'Cecilia', NULL, 'Folke', '2017-05-01', 'i7utfd7utfd876', 7),
(NULL, 'Makara', 'J', 'Loui', '2018-05-24', '54yhtf546', 8),
(NULL, 'Eugenia', NULL, 'Sergei', '2021-12-08', 'uj576u86k543', 9),
(NULL, 'Darina', 'C', 'Ukko', '2019-05-01', '876trs64egv', 10),
(NULL, 'Constance', NULL, 'Cavan', '2020-04-03', '63x298nyb', 11),
(NULL, 'Johan', NULL, 'Blanka', '2022-10-21', '978tdrfrx', 12),
(NULL, 'Merten', 'M', 'Macdara', '2018-07-10', '76ruf6uyfu', 13),
(NULL, 'Senna', 'P', 'Einar', '2022-12-23', '8nycwtinhs', 14),
(NULL, 'Lubor', NULL, 'Anthea', '2022-11-07', '77gqsgfdua87632', 15),
(NULL, 'Darshan', 'E', 'Nuray', '2019-02-06', 'rg3qrgy345', 7);

-- 10 entries
INSERT INTO COMPUTER VALUES
(NULL, 'HP', 'Pavilion', 2015, '1.0.03', 'Windows', 7),
(NULL, 'HP', 'Prodesk', 2018, '1.1.23', 'Windows', 7),
(NULL, 'Dell', 'Inspirion', 2019, '1.2.34', 'Windows', 8),
(NULL, 'Dell', 'Latitude', 2017, '1.0.14', 'Windows', 8),
(NULL, 'Acer', 'Swift', 2021, '1.4.65', 'Windows', 9),
(NULL, 'Apple', 'iMac', 2022, '1.7.02', 'MacOS', 9),
(NULL, 'Apple', 'Macbook Air', 2022, '1.7.01', 'MacOS', 10),
(NULL, 'Microsoft', 'Surface Pro', 2020, '1.5.07', 'Windows', 10),
(NULL, 'Lenovo', 'ThinkPad', 2023, '1.5.75', 'Windows', 10),
(NULL, 'Acer', 'Aspire', 2013, '1.0.00', 'Windows', 10);

-- 34 entries
INSERT INTO BOOK_CATALOG VALUES
(NULL, 'Don Quixote', NULL, 1615, 'Cervantes', NULL, NULL, 'OCLN'),
(NULL, 'A Tale of Two Cities', NULL, 1859, 'Dickens', 'Charles', NULL, 'OCLN'),
(NULL, 'The Lord of the Rings', NULL, 1954, 'Tolkein', 'J.', 'R.R.', 'OCLN'),
(NULL, 'The Little Prince', NULL, 1943, 'de Saint-Exupery', 'Antoine', NULL, 'OCLN'),
(NULL, 'Harry Potter and the Sorcerer''s Stone', NULL, 1997, 'Rowling', 'J.', 'K.', 'OCLN'),
(NULL, 'Alice in Wonderland', NULL, 1951, 'Carroll', 'Lewis', NULL, 'OCLN'),
(NULL, 'Dream of the Red Chamber', NULL, 1791, 'Hsueh-Chin', 'Tsao', NULL, 'OCLN'),
(NULL, 'The Lion, the Witch and the Wardrobe', NULL, 1950, 'Lewis', 'C.', 'S.', 'OCLN'),
(NULL, 'War and Peace', NULL, 1867, 'Tolstoy', 'Leo', NULL, 'OCLN'),
(NULL, 'Anna Karenina', NULL, 1878, 'Tolstoy', 'Leo', NULL, 'OCLN'),
(NULL, 'The Iliad', NULL, NULL, 'Homer', NULL, NULL, 'OCLN'),
(NULL, 'Crime and Punishment', NULL, 1866, 'Dostoevsky', 'Fyodor', NULL, 'OCLN'),
(NULL, 'Frankenstein', NULL, 1818, 'Shelley', 'Mary', NULL, 'RILO'),
(NULL, 'Great Expectations', NULL, 1861, 'Dickens', 'Charles', NULL, 'RILO'),
(NULL, 'A Christmas Carol', NULL, 1843, 'Dickens', 'Charles', NULL, 'RILO'),
(NULL, 'Jane Eyre', NULL, 1847, 'Bronte', 'Charlotte', NULL, 'RILO'),
(NULL, 'Pride and Prejudice', NULL, 1813, 'Austen', 'Jane', NULL, 'RILO'),
(NULL, 'Wuthering Heights', NULL, 1847, 'Bronte', 'Emily', NULL, 'RILO'),
(NULL, 'Adventures of Huckleberry Finn', NULL, 1884, 'Twain', 'Mark', NULL, 'RILO'),
(NULL, 'To the Lighthouse', NULL, 1927, 'Woolf', 'Virginia', NULL, 'QWER'),
(NULL, 'The Metamorphosis', NULL, 1915, 'Kafka', 'Franz', NULL, 'IOPA'),
(NULL, 'Mrs. Dalloway', NULL, 1925, 'Woolf', 'Virginia', NULL, 'OPAS'),
(NULL, 'Les Miserables', NULL, 1862, 'Hugo', 'Victor', NULL, 'PASD'),
(NULL, 'The Count of Monte Cristo', NULL, 1845, 'Dumas', 'Alexander', NULL, 'RTYU'),
(NULL, 'Oedipus the King', NULL, NULL, 'Sophocles', NULL, NULL, 'TYUI'),
(NULL, 'Medea', NULL, NULL, 'Euripides', NULL, NULL, 'UIOP'),
(NULL, 'Antigone', NULL, NULL, 'Sophocles', NULL, NULL, 'WERT'),
(NULL, 'Romeo and Juliet', NULL, 1597, 'Shakespeare', 'William', NULL, 'WERT'),
(NULL, 'Hamlet', NULL, 1601, 'Shakespeare', 'William', NULL, 'WERT'),
(NULL, 'Julius Caesar', NULL, 1599, 'Shakespeare', 'Wlliam', NULL, 'YUIO'),
(NULL, 'Macbeth', NULL, 1623, 'Shakespeare', 'William', NULL, 'QWER'),
(NULL, 'The Republic', NULL, NULL, 'Plato', NULL, NULL, 'PASD'),
(NULL, 'Othello', NULL, 1603, 'Shakespeare', 'William', NULL, 'OPAS'),
(NULL, 'Histories', NULL, NULL, 'Herodotus', NULL, NULL, 'UIOP');

-- 34 entries
INSERT INTO INVENTORY VALUES
(NULL, 2, 1, 1, 1),
(NULL, 2, 0, 2, 2),
(NULL, 2, 1, 3, 3),
(NULL, 2, 1, 4, 4),
(NULL, 2, 1, 5, 5),
(NULL, 2, 1, 6, 6),
(NULL, 2, 1, 7, 7),
(NULL, 2, 1, 8, 8),
(NULL, 2, 0, 9, 9),
(NULL, 2, 1, 10, 10),
(NULL, 4, 3, 11, 11),
(NULL, 2, 1, 12, 12),
(NULL, 2, 1, 13, 13),
(NULL, 2, 1, 14, 14),
(NULL, 2, 1, 15, 15),
(NULL, 5, 4, 7, 16),
(NULL, 2, 1, 7, 17),
(NULL, 2, 1, 8, 18),
(NULL, 2, 1, 8, 19),
(NULL, 1, 1, 9, 20),
(NULL, 2, 1, 9, 21),
(NULL, 2, 1, 10, 22),
(NULL, 2, 1, 10, 23),
(NULL, 3, 0, 11, 24),
(NULL, 2, 1, 11, 25),
(NULL, 2, 1, 12, 26),
(NULL, 4, 4, 12, 27),
(NULL, 2, 1, 13, 28),
(NULL, 2, 1, 14, 29),
(NULL, 1, 1, 14, 30),
(NULL, 2, 1, 15, 31),
(NULL, 3, 2, 15, 32),
(NULL, 2, 1, 15, 33),
(NULL, 2, 1, 15, 34);

INSERT INTO LOGS_IN VALUES
(1, 3, '2023-02-03 12:53:06', '2023-02-03 01:35:45'),
(2, 5, '2023-02-03 12:53:06', '2023-02-03 01:35:45'),
(3, 1, '2023-02-03 12:53:06', NULL);

INSERT INTO CHECKS_OUT VALUES
(4, 3, '2023-11-12', '2023-11-13', '2023-11-19'),
(5, 6, '2023-11-01', NULL, '2023-11-08'),
(6, 8, '2023-11-12', '2023-11-13', '2023-11-19');