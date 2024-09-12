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
		<h1> Add a Member </h1>
		<h3> This is the Add a Member Page. </h3>
		<form method="post" action="addmember2.php">
		<table>
			<tr>
				<p> Enter your First Name:
				<input type="text" name="fname" maxlength="20" required />
				</p>
				
				<p> Enter your Middle Initial (optional):
				<input type="text" name="minit" maxlength="20" />
				</p>
				
				<p> Enter your Last Name:
				<input type="text" name="lname" maxlength="20" required />
				</p>
				
				<p> Enter a password for your account:
					<input type="text" name="password" maxlength="20" required />
				</p>
				
				<p> Enter the code for the library you are registering for:
					<input type="number" name="lcode" required />
				</p>
				
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