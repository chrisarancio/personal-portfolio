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
		<h3> Please select the correct address for the Library you are searching for: </h3>
		<form method="post" action="searchmember3.php">
		<table>
			<tr>
				<td>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					$orgacronym = $_POST['orgacronym'];
					
					echo "<p> Currently searching libraries in: '$orgacronym' </p>";
					
					echo '<select name="lcode">';
						$query = "SELECT * FROM library WHERE OrgAcronym = '$orgacronym' ORDER BY State, Town, Address ASC";
						$result=$db->query($query);
						if($result==FALSE) {
							echo "<p>QUERY ERROR: ". $db->error ."</p>";
						}
						
						while($row = $result->fetch_assoc()){
							echo '<option value="';
							echo $row['LCode'];
							echo '">';
							echo $row['Address'] . ', ' . $row['Town'] . ', ' . $row['State'];
							echo "</option>";
						}
					echo '</select>';
				?>
				</td>
			</tr>
			<tr>
				<td> <input type="submit" /> </td>
			</tr>
		</table>
		</form>
		
		<hr />
		
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>