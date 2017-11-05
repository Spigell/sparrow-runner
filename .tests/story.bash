sparrow plg install bash 
./sparrow-runner.py bash command "echo HELLO. I AM A PLUGIN" --format concise

sparrow project create sparrow-runner 
sparrow task add sparrow-runner main bash 

./sparrow-runner.py sparrow-runner/main command "echo HI. I AM A TASK" --format concise

sparrow project remove sparrow-runner 
