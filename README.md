# opencv-runner
A docker image to run opencv python files in.

This uses an opencv python image: https://hub.docker.com/r/jjanzic/docker-python3-opencv/ to run python files in.  

I'm following turorials here https://opencv-python-tutroals.readthedocs.io/en/latest/

`docker build -t oliverstigley/opencv-runner .`

`docker run oliverstigley/opencv-runner python ./src/test.py` to get going. 
