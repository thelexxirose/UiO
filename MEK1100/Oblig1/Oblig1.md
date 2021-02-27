## Running the programs using docker

The easiest way of running these programs is to run them with docker.

The first thing you have to do is to pull the repository by typing this command in the terminal:
```
docker pull thelexxirose/mek1100_oblig1
```

After you have pulled down the repo, run the image by typing in this command:
```
docker run -t -d --name mek1100_oblig1 thelexxirose/mek1100_oblig1
```

To check if the container is up and running, you can use this command:
```
docker ps
```
and the container you just created should pop up.

Now you can run the command under to access the bash terminal of the container:
```
docker exec -it mek1100_oblig1 /bin/bash
```

If you want to run any of the programs, just type `python <filename>.py`, and then you'll run the program.
To run the test, simply type `pytest`, and then it'll tell you if it was successful or not.
