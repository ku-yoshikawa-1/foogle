FROM python:3.7.3
SHELL ["/bin/bash", "-c"]
ENV FLASK_APP /root/hello.py
ENV FLASK_ENV development
RUN pip install flask==1.0.3
WORKDIR /root
#EXPOSE 5000

CMD ["python3", "hello.py"]

# docker container run -it -v /Users/yuukiyamanaka13/projects/foogle:/root foogle sh
# docker container run -v /Users/yuukiyamanaka13/projects/foogle:/root -p 5000:5000 foogle