#!/usr/bin/bash

read UNMODIFIED_TASK
read MODIFIED_TASK

function gettasktext {
    echo $UNMODIFIED_TASK | grep -Po '(?<="description":").*?(?=",)' | head -1
}

TASK_TEXT=$(gettasktext)

set +e

# On command done, mark as done on habitica.
# On command delete, delete it on habitica.
function run_habash_things {
    (echo $* | grep -Po 'command:done' > /dev/null &&
         echo $(~/git/habash/habash getidoftask $TASK_TEXT) > /dev/null &&
         habash up $(~/git/habash/habash getidoftask $TASK_TEXT) > /dev/null) &

    (echo $* | grep -Po 'command:delete' > /dev/null &&
         echo $(~/git/habash/habash getidoftask $TASK_TEXT) > /dev/null &&
         habash deletetask $(~/git/habash/habash getidoftask $TASK_TEXT) > /dev/null) &
}

run_habash_things &

echo $MODIFIED_TASK

