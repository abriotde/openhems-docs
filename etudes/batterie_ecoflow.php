<?php

$Serial = getArg('Serial'); // Serial number EcoFlow Batterie
$APIKEY = getArg('APIKEY'); // API key asked from EcoFlow support@ecoflow.com
$Secret = getArg('Secret'); // Secret password asked from EcoFlow support@ecoflow.com

$header = array(
	"Content-Type: application/json",
	"appKey: ".$APIKEY,
	"secretKey: ".$Secret
);
$url ="https://api.ecoflow.com/iot-service/open/api/device/queryDeviceQuota?sn=".$Serial;
$http_result = httpQuery($url, 'GET', '','', $header);
$sortie = jsonToXML($http_result);
$code = xpath($sortie,"//code");
$message = xpath($sortie,"//message");
if ($code == "0") {
	$datasoc = xpath($sortie,"//data/soc");
	$dataremaintime = xpath($sortie,"//data/remainTime");
	$dataOut = xpath($sortie,"//data/wattsOutSum");
	$dataIn = xpath($sortie,"//data/wattsInSum");
	$finalsortie = "<sortie>Batterie: ".$datasoc."% ".$dataremaintime."min. "."IN: ".$dataIn."W OUT: ".$dataOut."W </sortie>";
} else {
	$finalsortie = "<sortie>".$message."</sortie>";
}
echo $finalsortie
?>
