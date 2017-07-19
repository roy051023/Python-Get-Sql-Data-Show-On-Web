<?php

	$output = shell_exec('python test.py '.$_POST["type"].' '.$_POST["value"]);
    echo $output;
?>