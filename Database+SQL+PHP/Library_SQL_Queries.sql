-- How many books does each library have?
SELECT library.Lcode AS Library_Code, library.Address AS Address, library.Town AS Town, library.State AS State, SUM(inventory.Quantity) AS Total_Books
FROM library, inventory
WHERE library.Lcode = inventory.Lcode
GROUP BY Library_Code
ORDER BY Total_Books DESC;

-- How many members does each library have?
SELECT library.Lcode AS Library_Code, library.Address AS Address, library.Town AS Town, library.State AS State, COUNT(member.MID) AS Num_Members
FROM library, member
WHERE library.Lcode = member.Lcode
GROUP BY Library_Code
ORDER BY Num_Members DESC;

-- How many computers does each library have?
SELECT library.Lcode AS Library_Code, library.Address AS Address, library.Town AS Town, library.State AS State, COUNT(computer.CID) AS Total_Computers
FROM library, computer
WHERE library.Lcode = computer.Lcode
GROUP BY Library_Code
ORDER BY Total_Computers DESC;

-- Is there anyone currently logged into a computer (where LogOnTime != NULL & LogOffTime == NULL)?
SELECT member.FirstName, member.LastName, member.MID
FROM member, logs_in
WHERE member.MID = logs_in.MID AND LogOnTime IS NOT NULL AND LogOffTime IS NULL;

-- How many computers are there of each make?
SELECT computer.Make, COUNT(computer.Make) AS Num
FROM computer
GROUP BY computer.Make;

-- What is the most popular operating system and what percentage of computers are that operating system?
SELECT computer.OperatingSystem, MAX(XX.num) AS Count, ((MAX(XX.num)/YY.total) * 100) AS Percentage
FROM computer,
	 (SELECT COUNT(computer.OperatingSystem) AS Num
	  FROM computer
	  GROUP BY computer.OperatingSystem) AS XX,
     (SELECT COUNT(*) AS total
      FROM computer) AS YY;
	  
-- What books are fully checked out? Inlcude ISBN, book title, and LCode.
SELECT inventory.ISBN, book_catalog.Title, library.Lcode
FROM inventory, book_catalog, library
WHERE inventory.NumAvailable = 0 AND inventory.ISBN = book_catalog.ISBN AND inventory.Lcode = library.Lcode;

-- What books are currently checked out and by whom?
SELECT member.FirstName, member.LastName, book_catalog.title AS Title, library.Lcode, inventory.DeweyDecimal
FROM book_catalog, member, library, inventory, checks_out
WHERE checks_out.CheckInDate IS NULL AND checks_out.MID = member.MID AND checks_out.DeweyDecimal = inventory.DeweyDecimal AND inventory.Lcode = library.Lcode AND inventory.ISBN = book_catalog.ISBN;

-- How many member libraries does each Library Organization have?
SELECT library_organization.OrgAcronym, COUNT(library.Lcode) AS Num_Libraries
FROM library_organization, library
WHERE library.OrgAcronym = library_organization.OrgAcronym
GROUP BY library_organization.OrgAcronym
ORDER BY Num_Libraries DESC;

-- What books have not been returned before the due date, i.e. are past due? Include book title, Dewey Decimal number, Lcode, and member name.
SELECT member.FirstName, member.LastName, book_catalog.title AS Title, library.Lcode, inventory.DeweyDecimal
FROM book_catalog, member, library, inventory, checks_out
WHERE checks_out.CheckInDate IS NULL AND checks_out.DueDate < CURRENT_DATE AND checks_out.MID = member.MID AND checks_out.DeweyDecimal = inventory.DeweyDecimal AND inventory.Lcode = library.Lcode AND inventory.ISBN = book_catalog.ISBN;

-- When did the first member join every library organization?
SELECT library_organization.OrgAcronym, MIN(MembershipStartDate) AS MembershipStartDate
FROM library, library_organization
WHERE library.OrgAcronym = library_organization.OrgAcronym
GROUP BY library_organization.OrgAcronym;

-- When did the first member join every library (oldest member start date for each library)?
SELECT library.Lcode, MIN(member.StartDate) AS StartDate
FROM library, member
WHERE library.Lcode = member.Lcode
GROUP BY library.Lcode;

-- When did the newest member join every library (newest member start date for each library)?
SELECT library.Lcode, MAX(member.StartDate) AS StartDate
FROM library, member
WHERE library.Lcode = member.Lcode
GROUP BY library.Lcode;

-- When did the newest member join every library organization?
SELECT library_organization.OrgAcronym, MAX(MembershipStartDate) AS MembershipStartDate
FROM library, library_organization
WHERE library.OrgAcronym = library_organization.OrgAcronym
GROUP BY library_organization.OrgAcronym;

-- What is the oldest book by publication year for each library? Replace libraries with books of only NULL year as "Unknown."
SELECT library.Lcode, coalesce(MIN(book_catalog.Year), 'Unknown') AS PublicationYear
FROM library, book_catalog, inventory
WHERE library.Lcode = inventory.Lcode AND inventory.ISBN = book_catalog.ISBN 
GROUP BY library.Lcode;

-- What is the newest book by publication year for each library? Replace libraries with books of only NULL year as "Unknown."
SELECT library.Lcode, coalesce(MAX(book_catalog.Year), 'Unknown') AS PublicationYear
FROM library, book_catalog, inventory
WHERE library.Lcode = inventory.Lcode AND inventory.ISBN = book_catalog.ISBN 
GROUP BY library.Lcode;

-- What books have authors with a middle initial and what is it?
SELECT book_catalog.ISBN, book_catalog.Title, book_catalog.AuthorMInit
FROM book_catalog
WHERE book_catalog.AuthorMInit IS NOT NULL;

-- How many authors have two or more books in the catalog and what are their names?
SELECT book_catalog.AuthorFname AS FirstName, coalesce(book_catalog.AuthorMInit, '') AS Minit, book_catalog.AuthorLname AS LastName, COUNT(book_catalog.ISBN) AS Num_Books
FROM book_catalog
GROUP BY book_catalog.AuthorFname, coalesce(book_catalog.AuthorMInit, ''), book_catalog.AuthorLname
HAVING Num_Books >= 2;

-- What library members have a middle initial and what is it?
SELECT member.MID, member.Lcode, member.MInit
FROM member
WHERE member.MInit IS NOT NULL;

-- What is the average number of days that library members check out a book?
SELECT AVG(CheckInDate - CheckOutDate) AS Avg_Days_Checked_Out
FROM checks_out;