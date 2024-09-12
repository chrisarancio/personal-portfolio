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
		<h1> Checkout a Book </h1>
				<?php
					//Create a connection to the MySQL server and store DB resource handle
					$db = new mysqli("localhost", "root", "", "library");
					//Check to see if connection established and exit on error
					if($db->connect_errno) {
						echo "Failed to connect to MySQL: (" . $db->connect_errno . ") " . $db->connect_errno;
						die("Goodbye");
					}
					
					$mid = $_POST['MID'];
					$deweydecimal = $_POST['DeweyDecimal'];
					$checkoutperiod = $_POST['checkoutperiod'];
					
					$checkoutdate = date("Y-m-d");
					$checkoutdate2 = date_create($checkoutdate);
					$duedate = date_add($checkoutdate2, date_interval_create_from_date_string("$checkoutperiod days"));
					$duedate = $duedate->format('Y-m-d');
					
					$query = "SELECT NumAvailable FROM inventory WHERE DeweyDecimal = $deweydecimal";
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
					$result = $db->query($query);
					$result = $result->fetch_array();
					$numavailable = intval($result[0]);
					
					//Check to see if book is avaiable (empty function checks if numavailable is 0) and update the inventory value
					if(empty($numavailable))
					{
						die('<h3> Sorry, there are no avaiable copies of that book. </h3>
							<hr />
							<h3> <a href="http://localhost:8012/phase6/addcheckout.php"> Return to Checkout Page </a> </h3>
							<hr />
							<h3> <a href="home.html"> Return to Home Page </a> </h3>');
					}
					else
					{
						$query = "UPDATE inventory SET NumAvailable = (NumAvailable - 1) WHERE DeweyDecimal = $deweydecimal";
						$result=$db->query($query);
						if($result==FALSE) {
							echo "<p>QUERY ERROR: ". $db->error ."</p>";
						}
					}
						
					//Insert into checks_out this new transaction
					$query = "INSERT INTO checks_out VALUES ($mid, $deweydecimal, '$checkoutdate', NULL, '$duedate')";
					$result=$db->query($query);
					if($result==FALSE) {
						echo "<p>QUERY ERROR: ". $db->error ."</p>";
					}
				?>
				
				<h3> Successful checkout and the database was updated! Here is a summary: </h3>
				<table>
					<tr>
						<th> MID </th>
						<th> Dewey Decimal </th>
						<th> Checkout Date </th>
						<th> Due Date </th>
					</tr>
					<tr>
					<?php
						echo '<td>';
						echo "$mid";
						echo '</td>';
						echo '<td>';
						echo "$deweydecimal";
						echo '</td>';
						echo '<td>';
						echo "$checkoutdate";
						echo '</td>';
						echo '<td>';
						echo "$duedate";
						echo '</td>';
					?>
					</tr>
				</table>
		<hr />
		
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>