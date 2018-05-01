# Description

simple wrapper for [sparrow](https://github.com/melezhik/sparrow) client.

Translates

`sparrow-runner.py bash command "echo 1"`

into

`sparrow plg run bash --param command="echo 1"`

## Supported option
- format

## Tests
$ strun --root ./.tests
