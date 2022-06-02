## Unit3 homework11
### Usage for testing your own code
#### before your test

`mkdir inputs`\
`mkdir outputs`\
`mkdir analysis`\
`mkdir log`\
`mkdir outputs/xh`\
`mkdir outputs/partner`\
or
'make setup'

build artifact in IDEA and put your code.jar into this folder

#### MacOS/Linux
`bash auto1.sh code num_of_cases`
#### Windows(use it in git bash)
change 'python3' in auto3.sh to 'python'\
remove 'time' in auto3.sh

`bash auto1.sh code num_of_cases`

### Usage for aoe

before your test

`bash aoe_init.sh num_of_tested_jars`\
put tested artifacts in 'hackjars'

hackjars\
├── 1.jar\
├── 2.jar\
└── 3.jar

### Then slain all of them :)
`bash code num_of_tested_jars num_of_cases`
