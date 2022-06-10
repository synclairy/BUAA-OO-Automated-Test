## Unit4 homework14
### Usage for testing your own code
#### before your test

`mkdir inputs`\
`mkdir outputs`\
`mkdir log`\
`mkdir analysis`\
`mkdir outputs/xh`\
`mkdir outputs/partner`\
or\
`make setup`

build artifact in IDEA and put your code.jar into this folder

#### MacOS/Linux
`bash auto2.sh code num_of_cases`
#### Windows(use it in git bash)
change 'python3' in auto2.sh to 'python'\
remove 'time' in auto2.sh

`bash auto2.sh code num_of_cases`

### Usage for aoe

before your test

```
mkdir hackjars
mkdir hackjars/1
mkdir hackjars/2
...
mkdir outputs/0
mkdir outputs/1
mkdir outputs/2
...
```


hackjars\
├── 1.jar\
├── 2.jar\
└── 3.jar\


`bash aoe.sh num_of_partners num_of_cases`