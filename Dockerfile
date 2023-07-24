FROM tensorflow/tensorflow

RUN apt update  &&  apt -y install git wget  &&  apt autoremove  &&  apt autoremove

WORKDIR /root
RUN pip install tensorflow-io 'git+https://github.com/KichangKim/DeepDanbooru.git#egg=DeepDanbooru'

RUN wget https://github.com/KichangKim/DeepDanbooru/releases/download/v3-20211112-sgd-e28/deepdanbooru-v3-20211112-sgd-e28.zip -O model.zip  && \
    unzip model.zip -d model  && \
    rm model.zip
ENV PROJECT_PATH=/root/model

COPY ./deepdanball.py /root/

WORKDIR /mnt
ENTRYPOINT [ "python", "/root/deepdanball.py" ]
