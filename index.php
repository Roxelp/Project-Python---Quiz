
<!DOCTYPE html>
<html>
  <head>
      <style>
          table, tr, td {
              border: 1px solid #000;
              border-collapse: collapse;
          }
      </style>
    <meta charset="UTF-8">
    <title>title</title>
  <link rel="stylesheet" href="stylesheet.css" type="text/css">
  </head>
  <body>
      <div style="width: 50%; float:left">
  <form method="POST">
    <input type="number" name="id_testu">   <br>
      <input type="text" name="pytanie">   <br>
      <input type="text" name="odp1">   <br>
      <input type="text" name="odp2">   <br>
      <input type="text" name="odp3">   <br>
      <input type="text" name="odp4">   <br>
      <input type="number" name="nr_odp"> <br>
      <input type="submit">
      <?php 

session_start();

if(isset($_POST["id_testu"])) {
    
    $id = $_POST["id_testu"];
    $pytanie = $_POST["pytanie"];
    $odp1 = $_POST["odp1"];
    $odp2 = $_POST["odp2"];
    $odp3 = $_POST["odp3"];
    $odp4 = $_POST["odp4"];
    $prawidlowa = $_POST["nr_odp"];
    
    if(empty($id) || empty($pytanie) || empty($odp1)|| empty($odp2) || empty($odp3)|| empty($odp4)|| empty($prawidlowa))    {
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
					
					if ($polaczenie->query("INSERT INTO pytania VALUES(NULL,'$id','$pytanie','$odp1','$odp2','$odp3','$odp4','$prawidlowa')"))
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
  </form>
      </div>
      <div style="width: 50%; float:left">
        <table>
        <?php 
          
    $host = "localhost";
    $db_user = "root";
    $db_password = "root";
    $db_name = "test";
    
            try 
            {
                $polaczenie = new mysqli($host, $db_user, $db_password, $db_name);
                if ($polaczenie->connect_errno!=0)
                {
                    throw new Exception(mysqli_connect_errno());
                }
                else
                    {
                        $sql = "SELECT * FROM testy";
                        $rezultat = $polaczenie->query($sql);
                    
                        if($rezultat->num_rows > 0) {
                            while($row = $rezultat->fetch_assoc()) {
                                echo "
                                    <tr>
                                        <td>". $row['id_testu']  ."</td>
                                        <td>". $row['nazwa'] ."</td>
                                        <td>". $row['kategoria']. "</td>
                                        <td>". $row['trudnosc'] ."</td>
                                    </tr>
                                ";
                            }
                        }
                }

                    $polaczenie->close();
                }
            catch(Exception $e)
            {
                echo '<span style="color:red;">Błąd serwera! Przepraszamy za niedogodności i prosimy o rejestrację w innym terminie!</span>';
                echo '<br />Informacja developerska: '.$e;
            }  
          
        ?>
        </table>
      </div>
  </body>
</html>
