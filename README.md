# About
> 1) Will scan all the files/folders in the given project path
>2) Get all the .py extended files and save their names, so the imported custom written python files to the other python files are not cosnidered as seperate libraries
>3) Scan all the python files, and only save the lines where only "import" / "from" start the line itself
>4) Will not save the same library name more than once if that specific library was used more than once in the same project, however, in different python files


### Input Project/Folder Structure

```
Demo
    │
    └── Demo
            │
            └── Demo
                    │
                    └──  numpy.py
                    │
                    └── Demo1
                            │
                            └── Demo2
                            │       │
                            │       └── demo.py 
                            │
                            └── Demo3 
                                    │
                                    └── demo2.py

```

### Final requirements.txt file tested on the Demo folder

![Blurred Images](https://i.imgur.com/QezzgyQ.png "This is a sample blurred data.")

### Demo
> Currently, just to check the accuracy and the performance of the script, I have tested
> it on the other projects with huge in files and complex folder structures, where it works
> completely fine.
![DEMO](https://i.imgur.com/oc4ttGs.png)


### Run the script

|Windows|Linux & MacOS|
|--------------------------|:--------------------------|
|```$python main.py```|```$python3 main.py```|




### To be added
1) Args and Kwargs argument input
2) Custom output path 
3) Efficiency 
4) Specific/Custom cases exceptions

### Article

Medium - 
https://woosal1337.medium.com/requirements-txt-generator-python-cedf7d14bfec

Dev.to -
https://dev.to/woosal/requirements-txt-generator-script-1200


### Contributors
<a href="https://www.github.com/woosal1337"><img src="https://i.imgur.com/oW4JaIe.jpg" width="75" height="75"></a>
