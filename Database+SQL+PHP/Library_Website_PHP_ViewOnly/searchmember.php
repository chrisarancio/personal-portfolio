<!DOCTYPE html>
<html>
	<head>
		<title>Library Organizations Database</title>
		<style type="text/css">
			body {font-family:"Verdana";}
			a	 {color:blue;}
		</style>
	</head>
	<body>
		<h1> Search Members By Library </h1>
		<h3> This is the Member Search Page. Please begin by selecting which Library Organization the Member belongs to: </h3>
		<form method="post" action="searchmember2.php">
		<table>
			<tr>
				<td> Select Library Organization: </td>
				<td>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					echo '<select name="orgacronym">';
						$query = "SELECT * FROM library_organization ORDER BY OrgAcronym ASC";
						$result=$db->query($query);
						if($result==FALSE) {
							echo "<p>QUERY ERROR: ". $db->error ."</p>";
						}
						
						while($row = $result->fetch_assoc()){
							echo '<option value="';
							echo $row['OrgAcronym'];
							echo '">';
							echo $row['OrgAcronym'];
							echo "</option>";
						}
					echo '</select>';
					?>
				</td>
			</tr>
		</table>
		<table>
			<tr>
				<td> <input type="submit" /> </td>
				<td> <input type="reset" /> </td>
			</tr>
		</table>
		</form>
		<hr />
		
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>