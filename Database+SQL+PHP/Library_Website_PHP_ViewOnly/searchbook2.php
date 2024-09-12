<!DOCTYPE html>
<html>
	<head>
		<title>Library Organizations Database</title>
		<style type="text/css">
			body {font-family:"Verdana";}
			table {border:2px solid black; border-collapse:collapse;}
			th, td {border:2px solid black;text-align:left; vertical-align:top; padding-left:10pt;padding-right:10pt;}
			a	 {color:blue;}
		</style>
	</head>
	<body>
		<h1> Search Book by Author </h1>
		<table>
			<tr>
				<th> ISBN </th>
				<th> Library Organization </th>
				<th> Library Code </th>
				<th> Dewey Decimal Number </th>
				<th> Libary Address </th>
				<th> Number Owned by Library </th>
				<th> Number Currently Available </th>
			</tr>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					$lname = $_POST['lname'];
					$title = $_POST['title'];
					
					echo "<h3> Here are the results for Author = '$lname' and Title = '$title' </h3>";
					
					$query = "SELECT book_catalog.ISBN, inventory.LCode, inventory.DeweyDecimal, inventory.NumAvailable, inventory.Quantity, library.OrgAcronym, library.Address, library.Town, library.State FROM book_catalog, inventory, library WHERE library.LCode = inventory.LCode AND inventory.ISBN = book_catalog.ISBN AND AuthorLName LIKE '%$lname%' AND Title LIKE '%$title%' ORDER BY ISBN ASC, NumAvailable DESC, OrgAcronym ASC;";
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
						
					while($row = $result->fetch_assoc()){
						echo '<tr>';
						echo '<td>';
						echo $row['ISBN'];
						echo '</td>';
						echo '<td>';
						echo $row['OrgAcronym'];
						echo '</td>';
						echo '<td>';
						echo $row['LCode'];
						echo '</td>';
						echo '<td>';
						echo $row['DeweyDecimal'];
						echo '</td>';
						echo '<td>';
						echo $row['Address'] . ', '. $row['Town'] . ', ' . $row['State'];
						echo '</td>';
						echo '<td>';
						echo $row['Quantity'];
						echo '</td>';
						echo '<td>';
						echo $row['NumAvailable'];
						echo '</td>';
						echo '</tr>';
					}
				?>
		</table>
		<hr />
		<h3> <a href="searchbook.php"> Return to Book Search Page </a> </h3>
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>