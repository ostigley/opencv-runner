FROM jjanzic/docker-python3-opencv
COPY . /src
RUN pip install matplotlib pillow pytesseract
CMD ["python", "/src/test.py"]