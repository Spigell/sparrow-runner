sparrow plg install bash 
./sparrow-runner.py bash command "echo HELLO. I AM A PLUGIN"

sparrow project create sparrow-runner 
sparrow task add sparrow-runner main bash 

./sparrow-runner.py sparrow-runner/main command "echo HI. I AM A TASK"

sparrow project remove sparrow-runner 
