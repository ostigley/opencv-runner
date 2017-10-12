FROM jjanzic/docker-python3-opencv
COPY . /src
CMD ["python", "/src/test.py"]