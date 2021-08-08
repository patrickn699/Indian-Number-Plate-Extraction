FROM python:3.8-slim-buster

WORKDIR /INPD_docker

COPY requirements.txt requirements.txt
COPY .  .

RUN apt-get update && apt-get install -y git
RUN apt-get install gcc g++ -y
RUN apt-get install g++ -y

RUN pip install opencv-python-headless
RUN apt-get install -y libgl1-mesa-dev
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install -r requirements.txt

RUN pip install 'git+https://github.com/facebookresearch/fvcore'

RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]
CMD ["sapp_dock.py"]