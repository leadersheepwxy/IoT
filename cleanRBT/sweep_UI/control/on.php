<?php
$host = '172.20.10.2';
$port = '8888';
$message = 'on';


function send_tcp_message($host, $port, $message)
{
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    @socket_connect($socket, $host, $port);
 
    $num = 0;
    $length = strlen($message);
    do{
        $buffer = substr($message, $num);
        $ret = @socket_write($socket, $buffer);
        $num += $ret;
    } while ($num < $length);
 
    $ret = '';
    do{
        $buffer = @socket_read($socket, 1024, PHP_BINARY_READ);
        $ret .= $buffer;
    } while (strlen($buffer) == 1024);
 
    socket_close($socket);
 
    return $ret;
}
 
$ret = send_tcp_message($host, $port, $message);
?>
<head>
<script language="javascript"> location.replace('control_page.php') </script>
</head>