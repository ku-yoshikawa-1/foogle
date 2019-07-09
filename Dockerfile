FROM python:3.7.3
SHELL ["/bin/bash", "-c"]
#ENV FLASK_APP /root/hello.py
#ENV FLASK_ENV development
RUN pip install flask==1.0.3 flask-cors==3.0.7 flask_mysqldb
WORKDIR /root
#EXPOSE 5000

# CMD ["python3", "hello.py"]

# docker container run -it -v /[FOOGLE_PATH]:/root foogle sh
# docker container run -v [FOOGLE_PATH]:/root -p 5000:5000 foogle