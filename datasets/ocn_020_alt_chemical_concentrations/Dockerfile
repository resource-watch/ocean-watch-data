FROM python:3.6
MAINTAINER Rachel Thoms <rachel.thoms@wri.org>

# install core libraries
RUN apt-get update
RUN pip install --upgrade pip

# install application libraries
RUN pip install carto==1.11.1
RUN pip install requests
RUN pip install pandas
RUN pip install python-rapidjson
RUN pip install cartoframes
RUN pip install geopandas
RUN pip install datetime
RUN pip install python-dateutil
RUN pip install xml_python
RUN pip install python-math
RUN pip install concurrent-utils

# set name
ARG NAME=ocn_020d
ENV NAME ${NAME}

# copy the application folder inside the container
RUN mkdir -p /opt/$NAME/data
WORKDIR /opt/$NAME/
COPY contents .

RUN useradd $NAME
RUN chown -R $NAME:$NAME .
USER $NAME

CMD ["python", "main.py"]
