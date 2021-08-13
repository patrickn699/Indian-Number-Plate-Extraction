FROM pytorch/pytorch
FROM python:3.8-slim-buster

# if you forked EasyOCR, you can pass in your own GitHub username to use your fork
# i.e. gh_username=myname
ARG gh_username=JaidedAI
ARG service_home="/home/EasyOCR"
ARG language_models="['en']"

# Configure apt and install packages
RUN apt-get update -y && \
    apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev \
    git \
    # cleanup
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/li

# Clone EasyOCR repo
RUN mkdir "$service_home" \
    && git clone "https://github.com/$gh_username/EasyOCR.git" "$service_home" \
    && cd "$service_home" \
    && git remote add upstream "https://github.com/JaidedAI/EasyOCR.git" \
    && git pull upstream master

# Build
RUN cd "$service_home" \
    && python setup.py build_ext --inplace -j 4 \
    && python -m pip install -e .

RUN apt-get install wget -y && apt-get install -y gnupg2 && apt-get install -y curl

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
#ENV DISPLAY=:99

RUN pip install selenium==3.8.0

WORKDIR /INPD_docker

COPY requirements.txt requirements.txt
COPY .  .

RUN apt-get update && apt-get install -y git
RUN apt-get install gcc g++ -y
RUN apt-get install g++ -y

RUN pip install opencv-python-headless
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install -r requirements.txt

RUN pip install 'git+https://github.com/facebookresearch/fvcore'

RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN python -c "import easyocr; reader = easyocr.Reader(${language_models}, gpu=False)"


EXPOSE 8501


ENTRYPOINT ["streamlit","run"]
CMD ["sapp_dock.py"]