
# Indian Number Plate Recognition

An open source Indian Number Plate Recogniton project built using deep learning.




## Try it out!

[Click here!!](https://anpr-docker.herokuapp.com/)


## Version

* 24 August 21 - v1.0

    *  works with car number plates 



## Whats next?

python pip framework comming!!
## Screenshots

![App Screenshot 1](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as1.png?raw=true)

![App Screenshot 2](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as2.png?raw=true)

![App Screenshot 3](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as3.png?raw=true)

![App Screenshot 4](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as4.png?raw=true)

![App Screenshot 4](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as5.png?raw=true)

![App Screenshot 4](https://github.com/patrickn699/Indian-Number-Plate-Extraction/blob/master/OP_SS/as6.png?raw=true)

## Installation

1. Download or clone the repo

2. To run it locally, firstly install the requirements 

```bash
  pip instll requirements.txt
```

3. Then navigate to root folder from either file explorer or through cmd/terminal

4. In the root folder open cmd/terminal and type the following command

```bash
  streamlit run app.py
```
5. Then the app will be opened inside your browser.

### for windows

Make sure you have chrome driver installed in your system and if you are using windows then go the file get_details.py
change the path on line number 25,26 where your chorme drive is present.

```python
   chrome_path = r'path to chrome driver'
   options.binary_location = r'path to chrome.exe'
```

### for linux
If you are using linux then go to the get_details.py file and comment the lines 25,26,31 then uncomment lines 28 and 29.

```python
   options.binary_location = '/usr/bin/google-chrome'
   driver = webdriver.Chrome(chrome_options=options,executable_path=r'/usr/bin/chromedriver')

```

---
### for docker

To run it inside the docker container make sure that you have docker installed in your system.
if you want to run the container locally then simply navigate to folder INPD_docker simply uncomment the following lines insider the dockerfile 77,81,83 and comment 78,82

```docker
   EXPOSE 8501
   #EXPOSE $PORT

   ENTRYPOINT ["streamlit","run"]
   #CMD streamlit run sapp_dock.py --server.port $PORT
   CMD [ "sapp_dock.py"]
```

After making the changes you need to build the image using the folliwng command

```docker
   docker build -t INPR-latest 
```

Once the image has been built, then execute the following command

```docker
   docker run -dp 3000:3000 INPR-latest
```

In few seconds go the url given below to access the app

```docker
   http://localhost:3000
```

---

## Note

This is the initial build of the app so it won't be perfect in feteching the details of the number plate but to increase the success rate please make sure the uploaded image meets the following points.

    1. The image should be clear and of high resolution
    2. The number plate should also be visible clearly
    3. The number plate should not be far away 
    4. The text on the plate should not be blured or distorted
    5. The plate shold not be broken or partially covered 

I am still trying to imporve it continiously so stay tuned!





 












## Tech Stack

**Frontend:** Streamlit

**Backend:** Python, Pytorch, Selenium

  
## Feedback

If you have any feedback, bugs, queries please reach out to me on [Linkedin](https://www.linkedin.com/in/prathmesh-patil-b151051a3) and also raise an issue about the same.

  