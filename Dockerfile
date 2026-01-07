## Take a base image of python:3.8-slim-buster, so what will happen is that from the docker hub we will bring up this python:3.8 version of linux base image
## so that it can be taken and can be done w.r.t the deployment. It will be basically taking the base image of a environment.
FROM python:3.8-slim-buster
## We are creating a working directory called as app
WORKDIR /app
## Next is copying this entire project into this app folder, the entire projet will be copied into this app folder
COPY . /app
## This is the command where we are updating all the packages before doing the deployment in that particular server(linux machine) --> We will definitely be using the ubuntu machine over there
RUN apt update -y && apt install awscli -y
## Then we will go ahead and do the installment of the entire requirements.txt 
RUN pip install -r requirements.txt
## Once the installment of requirements.txt takes place, below is the command used to run the file that is app.py, there we are also specifying that we are working in python 3.8 version and app.py is the file name which it will be running
CMD ["python3", "app.py"]