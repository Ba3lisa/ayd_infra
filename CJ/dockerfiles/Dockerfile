FROM ubuntu:18.04

# Build tools and essential libraries
RUN apt-get update -yqq && apt-get install --yes --no-install-recommends build-essential \
    python3-pip python3-dev

# Upgrade pip
RUN apt-get update -yqq && apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

# Symlink python3 -> python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Python requirements
ADD ./dockerfiles/requirements.txt /
RUN pip3 install -r /requirements.txt

# Init working dir
RUN mkdir /bot

# ENV VARS
ENV WORKING_DIR=/bot
ENV PYTHONPATH=/bot

# keep alive
CMD ["tail", "-f", "/dev/null"]
