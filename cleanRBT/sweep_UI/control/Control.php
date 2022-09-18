<!-- 用樹莓派以TCP發送資料 -->
<?php

$host = '172.20.10.2'; #用ifconfig看樹莓派的IP，填入這個位置
$port = '8888';
$message = $_POST["btn"];

function send_tcp_message($host, $port, $message)
{
    # 使用IPv4(網際網路通訊協定第四版)與TCP(傳輸控制協定)進行連接
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    @socket_connect($socket, $host, $port);
 
    $num = 0;
    $length = strlen($message); #取字串長度
    do
    {
        $buffer = substr($message, $num);
        $ret = @socket_write($socket, $buffer);
        $num += $ret;
    } while ($num < $length);
 
    $ret = '';
    do
    {
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
