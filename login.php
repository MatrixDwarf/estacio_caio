<?php
    session_start();
    $erro = "";
    if(!isset($_POST["login"]) or ($_POST["login"] == ""))

        $erro = "Preencha o Login!";

    elseif(!isset($_POST["senha"]) or ($_POST["senha"]== ""))
        $erro = "Senha inválida ou não preenchida. tente novamente!"
    else{

        $login=$_POST["login"];
        $senha=$_POST["senha"];
        if($login != "admin" or $senha != "1234"){
            $erro="Login ou Senha inváldos";
        }
        else{
            $_SESSION["usuario"] = "Administrador";
        }
    } 
    
    if($erro!="")
        header ("Location: form_login.php?erro$erro", true, 301);
    else{
        header ("Location: protegida.php", true, 301);
    }

?>