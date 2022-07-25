FROM ubuntu:focal

ARG MYPATH
ARG USER

ENV MYPATH=$MYPATH
ENV USER=$USER

RUN apt update && apt install -y curl

RUN curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"

RUN sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH

RUN $MYPATH/bin/conda init bash
RUN $MYPATH/bin/conda config --set auto_activate_base false
RUN $MYPATH/bin/conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy

CMD ["bash"]
