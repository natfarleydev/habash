# habash
A (very minimal) habitica terminal client written entirely in bash.

It requires the `$HABITICA_TOKEN` and `$HABITICA_UUID` to be set in the environment.

WARNING: This script does not have any checks in it for accidental deletion of tasks etc., so if you don't understand how this script works, don't use it! 

Usage is simple:

```
$ habash help
Welcome to Habash!

This is a very basic bash script to ease contacting Habitica on the command line. It is essentially a basic wrapper around curl, with some extra commands for ease of use.

Available commands:
habash getidoftask TASK_TEXT
habash up TASK_TEXT
habash down TASK_TEXT
habash createtodo TASK_TEXT
habash createhabit TASK_TEXT
```

## Developer's guide
The aim of this project is to provide an interface to Habitica on any computer with bash and ordinary GNU utils (e.g. a Openstack machine, a work machine, etc.). As such, it should not have dependencies that are not likely to be installed on a fresh Linux install.

Any pull requests that follow the spirit of the above paragraph are _very_ likely to be accepted. 
