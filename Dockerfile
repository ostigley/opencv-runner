FROM jjanzic/docker-python3-opencv
COPY . /src
RUN pip install matplotlib
CMD ["python", "/src/test.py"]