# DataRoot University: Data Science Fundamentals. Snake Project

Snake project is a Python assignment from the week 2.
## Project structure
```

snake
    ├── env                  - contains files with environmental elements.
    │   ├── core             - main parts of env. 
    │   │   ├── snake.py     - snake properties.
    │   │   └── world.py     - grid world properties.
    │   │
    │   ├── utils            - additional parts of env
    │   │   └── renderer.py  - observation rendering tool. 
    │   │
    │   └── snake_env.py     - compilation of main parts of environment.
    │
    ├── settings             - here you can store different constant values, connection parameters, etc.
    │   └── constants.py     - multiple constants storage for their convenient usage.
    │
    ├── tests      	         - tests for your code
    |   ├── validators       - main tests utils
    │   │     │
    │   │     ├── snake_validator.py    - snake tests utils
    │   │     └── world_validator.py    - world tests utils
    │   │
    |	├── test_snake.py    - tests for snake's step method
    |	└── test_world.py    - tests for world methods
    |    
    └── interactor.py        - script to allow you playing Snake manually.
```

# Result

![image](https://github.com/DataRootUniversity/ds-fundamentals/blob/master/snake-project/figures/snake.gif?raw=true)
