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

## Developer's guide
The aim of this project is to provide an interface to Habitica on any computer with bash and ordinary GNU utils (e.g. a Openstack machine, a work machine, etc.). As such, it should not have dependencies that are not likely to be installed on a fresh Linux install.

Any pull requests that follow the spirit of the above paragraph are _very_ likely to be accepted. 
