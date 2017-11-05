# Description

simple wrapper on sparrow for better ( for my opinion ) runtime commandline

Translates
`sparrow-runner.py bash-pssh hosts 127.0.0.1 commands "echo 1"`

into

`sparrow plg run bash-pssh --param hosts=127.0.0.1 --param commands="echo 1"

## Supported option
- format

## Tests
$ strun --root ./.tests
