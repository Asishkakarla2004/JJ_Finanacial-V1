FROM python
EXPOSE 5000
LABEL test application
MAINTAINER Asish
WORKDIR /app1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["app.py"]
