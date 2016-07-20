# habash
A (very minimal) habitica terminal client written entirely in bash.

Usage is simple:

```
$ habash helpme
Welcome to Habash!

This is a very basic bash script to ease contacting Habitica on the command line. It is essentially a basic wrapper around curl, with some extra commands for ease of use.

Available commands:
habash getidoftask TASK_TEXT
habash up TASK_TEXT
habash down TASK_TEXT
habash createtodo TASK_TEXT
habash createhabit TASK_TEXT
habash post API_PATH [CURL_ARGUMENTS]
habash get API_PATH [CURL_ARGUMENTS]


WARNING:
This script does not check inputs; if you do something like "habash rm -rf *", this script will execute "rm -rf *". You have been warned!
```
