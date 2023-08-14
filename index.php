<?php
$servername = "postgresql://curtis:w2dn6NMc745ufuQT58FYBA@okay-pup-4890.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full";
$username = "curtis";
$password = "w2dn6NMc745ufuQT58FYBA";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>

