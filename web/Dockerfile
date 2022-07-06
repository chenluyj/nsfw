FROM python:3.8
MAINTAINER chenlu@moguding.net
WORKDIR /home/app
ADD nsfwUtil.py /home/app/nsfwUtil.py
ADD requirements.txt /home/app/requirements.txt
ADD server.py /home/app/server.py
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN pip install -r /home/app/requirements.txt
ENTRYPOINT [ "sh", "-c", "python /home/app/server.py" ]