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
		<h1> Show Currently Checked-out Books </h1>
		<table>
			<tr>
				<th colspan="2" style="text-align:center"> Member Info </th>
				<th colspan="2" style="text-align:center"> Book Info </th>
				<th colspan="3" style="text-align:center"> Library Info </th>
			</tr>
			<tr>
				<th> Member First Name </th>
				<th> Member Last Name </th>
				<th> Book Title </th>
				<th> Author Last Name </th>
				<th> Library Code </th>
				<th> Dewey Decimal Number </th>
				<th> Number Currently Available at this Library </th>
			</tr>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					$query = "SELECT member.FirstName, member.LastName, book_catalog.Title, book_catalog.AuthorLName, library.LCode, inventory.DeweyDecimal, inventory.NumAvailable
								FROM book_catalog, member, library, inventory, checks_out
								WHERE checks_out.CheckInDate IS NULL AND checks_out.MID = member.MID AND checks_out.DeweyDecimal = inventory.DeweyDecimal AND inventory.Lcode = library.Lcode AND inventory.ISBN = book_catalog.ISBN";
					
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
						
					while($row = $result->fetch_assoc()){
						echo '<tr>';
						echo '<td>';
						echo $row['FirstName'];
						echo '</td>';
						echo '<td>';
						echo $row['LastName'];
						echo '</td>';
						echo '<td>';
						echo $row['Title'];
						echo '</td>';
						echo '<td>';
						echo $row['AuthorLName'];
						echo '</td>';
						echo '<td>';
						echo $row['LCode'];
						echo '</td>';
						echo '<td>';
						echo $row['DeweyDecimal'];
						echo '</td>';
						echo '<td>';
						echo $row['NumAvailable'];
						echo '</td>';
						echo '</tr>';
					}
				?>
		</table>
		<hr />
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>