
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>title</title>
  <link rel="stylesheet" href="stylesheet.css" type="text/css">
  </head>
  <body>
  <form method="POST">
      <input type="text" name="nazwa">   <br>
      <input type="text" name="kategoria">   <br>
      <input type="text" name="trudnosc">   <br>
      <input type="submit">
  </form>
  </body>
</html>
<?php 

session_start();

if(isset($_POST["nazwa"])) {
    
    $nazwa = $_POST["nazwa"];
    $kategoria = $_POST["kategoria"];
    $trudnosc = $_POST["trudnosc"];
    
    $host = "localhost";
    $db_user = "root";
    $db_password = "root";
    $db_name = "test";
    
    if(empty($nazwa) || empty($kategoria) || empty($trudnosc))    {
        
        echo "Uzupełnij wszystkie pola!";
        
    } else {
        try 
		{
			$polaczenie = new mysqli($host, $db_user, $db_password, $db_name);
			if ($polaczenie->connect_errno!=0)
			{
				throw new Exception(mysqli_connect_errno());
			}
			else
			  {
					
					if ($polaczenie->query("INSERT INTO testy VALUES(NULL,'$nazwa','$kategoria','$trudnosc')"))
					{
						echo "Dodano pomyślnie!";
					}
					else
					{
						throw new Exception($polaczenie->error);
					}
					
				}
				
				$polaczenie->close();
			}
		catch(Exception $e)
		{
			echo '<span style="color:red;">Błąd serwera! Przepraszamy za niedogodności i prosimy o rejestrację w innym terminie!</span>';
			echo '<br />Informacja developerska: '.$e;
		}
    }
}

?>
