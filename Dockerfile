FROM tesseractshadow/tesseract4re
FROM jjanzic/docker-python3-opencv
COPY . /src
RUN pip install matplotlib pillow pytesseract image
CMD ["python", "/src/test.py"]