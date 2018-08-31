# habash
A (very minimal) habitica terminal client written entirely in bash.

It requires the `$HABITICA_TOKEN` and `$HABITICA_UUID` to be set in the environment.

Usage is simple:

```
$ habash help
Usage: habash <command> [command arguments]
    habash up "Floss"
    habash create-todo "Buy milk"

Contacts Habitica API through cURL with minimal dependencies.

Commands available (aliases separated with |):
    ls
    cast <SPELL NAME> <(optional) TARGET ID>
    id <TASK TEXT>
    up|done <TASK_TEXT>
    down <TASK_TEXT>
    delete <TASK_TEXT>
    create-todo|ct <TASK_TEXT>
    create-habit|ch <TASK_TEXT>

e.g.
    habash done Use habash on the command line

Post issues at https://github.com/nasfarley88/habash/issues
```

## Examples

`habash` is designed to be a component in a larger work chain (e.g. as a git
commit hook). The following are some example(s) of how this can be used.

### Draining MP on a single spell

With `habash cast`, it's possible to create a simple bash loop to drain all mana
on a single spell. E.g.

```bash
while true; do if habash cast fireball $(habash id Morning prayer) | grep -Po '(?!"message":)"Not enough mana."'; then break; fi; done
```

or with a little more formatting

```bash
while true
do if habash cast fireball $(habash id Morning prayer) | \ # Cast fireball on 'Morning prayer'
        grep -Po '(?!"message":)"Not enough mana."'        # Test if the last time has failed
then break                                                 # If it has failed with not enough mana, break the loop
fi
done
```

And all remaining mana will drain using the spell 'Burst of Flames' on the task
'Morning prayer'.

### Selling common eggs

In the `./examples` directory there is a script for selling common eggs
(`sell-common-eggs.sh`). Simply run it and the script will sell all your common
eggs.

Completed your stable already? Set up a cron job and watch the gold flow in!

```bash
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

```

## Developer's guide
The aim of this project is to provide an interface to Habitica on any computer with bash and ordinary GNU utils (e.g. a Openstack machine, a work machine, etc.). As such, it should not have dependencies that are not likely to be installed on a fresh Linux install.

Any pull requests that follow the spirit of the above paragraph are _very_ likely to be accepted. 
