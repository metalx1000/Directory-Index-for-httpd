#!/bin/sh
echo -en "Content-Type: text/html\r\n\r\n"

cat << EOH
<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="//ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Basic List Group</h2>
  <div id="list" class="list-group">
EOH

#create list
#ls -a --group-directories-first ..${REQUEST_URI#${SCRIPT_NAME}}|while read line
ls -a "..${REQUEST_URI#${SCRIPT_NAME}}"|while read line
do
  echo "<a href='$line' class='list-group-item'>$line</a>"
done

cat << EOF
  </div>
</div>

</body>
</html>
EOF
