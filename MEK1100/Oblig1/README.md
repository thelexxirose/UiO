## Running the programs

I am going to assume that you have cloned this repository, so I will be skipping this part of the process.

To run the programs, you first need to set an environment variable that points to the **MEK1100** directory.
To do that run this command in the terminal:
```
export MEK1100=<path to MEK1100 dir>
```
If you want the environment variable to be permanent, then you can edit the *.profile* file. 
To edit the file, type this command:

```
sudo nano ~/.profile
```
then navigate your way down to the bottom of the file, and then type in the same command we used in the terminal before:
```
export MEK1100=<path to MEK1100 dir>
```
and then save the file by pushing **ctrl + x**, then **y**, and then **enter**


Now make sure that you have installed all the necessary dependencies. In the **UiO** directory, type this command:

```
pip3 install -r requirements.txt
```

In **MEK1100/Python** you can type in `python3 <filename>.py`, and it should run the program.
