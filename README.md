# Dockerize_app
## Dockerfile
This defines instructions used to build a docker image, details of the dockerfile for this project is found in the <a href="/Dockerfile"> Dockerfile </a>

#### Explanation of the Dockerfile commands

* FROM - Specifies the base image from which the image is built. 
* MAINTAINER - Specifies the name and email of the owner

* RUN - Runs installation files. you can add additional content to the image by running installation tasks and storing the results of these commands. 
In this project we install python3 and pip. We then use pip in the second RUN command to install all packages in the requirements.txt file.

* COPY - copies files/directories from the host machine to the container during the build process. 

* WORKDIR - sets the working directory in the container 

* ENTRYPOINT - Defines the entry point of the application, in our case its python3

* CMD - Runs the app.py file in the app directory.


## Build the Image

## Run the image