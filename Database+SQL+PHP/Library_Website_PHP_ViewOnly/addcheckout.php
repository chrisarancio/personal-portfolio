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
		<h1> Checkout a Book </h1>
		<h3> This is the Book Checkout Page. Please use the "Search for Book By Author" link below to find the Dewey Decimal Number of the book you would like to check out. </h3>
		<form method="post" action="addcheckout2.php">
		<table>
			<tr>
				<p> Enter your MID:
				<input type="text" name="MID" required />
				</p>
				
				<p> Enter Dewey Decimal:
				<input type="text" name="DeweyDecimal" required />
				</p>
				
				<p> How long would you like to check-out the book for (1-14 days)?:
				<input type="number" name="checkoutperiod" min="1" max="14" required />
				</p>
				
				<tr>
					<td> <input type="submit" /> </td>
					<td> <input type="reset" /> </td>
				</tr>
		</table>
		</form>
		<hr />
		<h3> <a href="searchbook.php"> Link to Book Search Page to find Dewey Decimal Number </a> </h3>
		<hr />
		<h3> <a href="home.html"> Return to Home Page </a> </h3>
	</body>
</html>