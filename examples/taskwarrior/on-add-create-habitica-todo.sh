#!/usr/bin/bash

read TASK
function gettasktext {
    echo $TASK | grep -Po '(?<="description":").*?(?=")'
}

habash createtodo $(gettasktext $*) > /dev/null & 

echo $TASK
