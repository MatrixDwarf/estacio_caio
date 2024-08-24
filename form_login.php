<html>
<body>
<h1>Login do Usuário</h1>
<?php
    if(isset($_GET["erro"]))
        echo("<hr/><h2>".$_GET['erro']. "</h2><hr>");
?>
<form action="login.php" method="POST">
    <p>Login : <input type="email" name="login"/></p>
    <p>Senha : <input type="password" name="senha"/></p>
    <input type="submit" value="enviar"/>
</form>
</body>
</html>