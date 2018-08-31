#!/usr/bin/env bash

export EGGS="Wolf TigerCub PandaCub LionCub Fox FlyingPig Dragon Cactus BearCub"

for egg in $EGGS
do
    echo "Selling the '$egg' egg"
    while true
    do if habash sell eggs $egg | grep -Po '"success":false' > /dev/null
       then
           echo "Sold out!"
           break
       else echo "Sold 1 '$egg' egg."
       fi
    done
done
