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
		<h1> Search Book By Author </h1>
		<h3> This is the Book Search Page. Please enter the author's last name and the title of the book: </h3>
		<form method="post" action="searchbook2.php">
		<table>
			<tr>
				<p> Author Last Name:
				<input type="text" name="lname" required />
				</p>
				
				<p> Book Title:
				<input type="text" name="title" required />
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