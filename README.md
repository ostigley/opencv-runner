# opencv-runner
A docker image to run opencv python files in.

This uses an opencv python image: https://hub.docker.com/r/jjanzic/docker-python3-opencv/ to run python files in.  

I'm following turorials here https://opencv-python-tutroals.readthedocs.io/en/latest/

`docker build -t oliverstigley/opencv-runner .`

`docker create --name opencv -it oliverstigley/opencv-runner /bin/bash`

`docker start opencv`

`docker exec -it opencv python src/python/test.py`

Make changes to your `/python` folder, and run

`docker cp python opencv:src/`

`docker cp opencv:src/results results`

to update the container.
