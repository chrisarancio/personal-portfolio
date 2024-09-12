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
		<h1> Add a Member </h1>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					$fname = $_POST['fname'];
					$minit = $_POST['minit'];
					$lname = $_POST['lname'];
					$password = $_POST['password'];
					$lcode = $_POST['lcode'];
					$startdate = date("Y-m-d");
						
					//Insert into checks_out this new transaction
					$query = "INSERT INTO member VALUES (NULL, '$fname', '$minit', '$lname', '$startdate', '$password', $lcode)";
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
				?>
				
				<h3> Successfully added new member and the database was updated! Here is a summary: </h3>
				<table>
					<tr>
						<th> First Name </th>
						<th> Middle Initial </th>
						<th> Last Name </th>
						<th> Password </th>
						<th> Library Code </th>
						<th> Start Date </th>
					</tr>
					<tr>
					<?php
						echo '<td>';
						echo "$fname";
						echo '</td>';
						echo '<td>';
						echo "$minit";
						echo '</td>';
						echo '<td>';
						echo "$lname";
						echo '</td>';
						echo '<td>';
						echo "$password";
						echo '</td>';
						echo '<td>';
						echo "$lcode";
						echo '</td>';
						echo '<td>';
						echo "$startdate";
						echo '</td>';
					?>
					</tr>
				</table>
		<hr />
		
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>