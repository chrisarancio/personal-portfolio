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
		<h1> Search Members By Library </h1>
		<table>
			<tr>
				<th> Last Name </th>
				<th> First Name </th>
				<th> Middle Initial </th>
			</tr>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					echo '<h3> Here are the members of your chosen library: </h3>';
					
					$lcode = $_POST['lcode'];
					
					$query = "SELECT * FROM member WHERE LCode = '$lcode' ORDER BY LastName, FirstName, MInit";
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
						
					while($row = $result->fetch_assoc()){
						echo '<tr>';
						echo '<td>';
						echo $row['LastName'];
						echo '</td>';
						echo '<td>';
						echo $row['FirstName'];
						echo '</td>';
						echo '<td>';
						echo $row['MInit'];
						echo '</td>';
						echo '</tr>';
					}
				?>
		</table>
		<hr />
		
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>