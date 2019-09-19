<!DOCTYPE html lang="fr">
<head>
</head>
<body>
  <?php
  // enregistre valeur
  if($_POST['favcolor']){
    $fp=fopen("color.txt", "w");
    $json=json_encode($_POST);
    fwrite($fp, $json);
  }
  // récupère la valeur
  $fp=fopen("color.txt", "r+");
  $json=fread($fp,filesize("color.txt"));
  fclose($fp);
  if($json!=""){// valeur par défaut
    $_POST=json_decode($json,true);
  }else{ // fichier non vide
    $_POST['favcolor']="#ff0000";
  }
  ?>
  Select a color :
  <form method="post">
    <input type="color" name="favcolor" value="<?php echo $_POST['favcolor']; ?>"><br>
    <button>CLIQUE</button>
  </form>
<body>
