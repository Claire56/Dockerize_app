# Dockerize a Simple Flask app
## Dockerfile
This defines instructions used to build a docker image, details of the dockerfile for this project is found in the <a href="/Dockerfile"> Dockerfile </a>

#### Explanation of the Dockerfile commands

* FROM - Specifies the base image from which the image is built. 
* MAINTAINER - Specifies the name and email of the owner

* RUN - Runs installation files. you can add additional content to the image by running installation tasks and storing the results of these commands. 
In this project we install python3 and pip. We then use pip in the second RUN command to install all packages in the requirements.txt file.

* COPY - copies files/directories from the host machine to the container during the build process. 

* WORKDIR - sets the working directory in the container 

* ENTRYPOINT - Defines the entry point of the application, in our case its python3. it sets or overwrite the default entrypoint command for the image. The entrypoint sets the command and parameters that will be executed first when a container is run. Any commands and arguments passed at the end of the docker run command will be appended to the entrypoint. 

* CMD - Runs the app.py file in the app directory.


## Build the Image
Image is built using the docker command, as seen below <br>
$docker build -t docker-flask:trial .

#### Explanation docker build
1. The -t flag is used to label the image
2. 'trial' is just a tag for the image and the dot at the end signals build in current directory.

while building docker creates layers resulting from each command in the <a href="/Dockerfile"> Dockerfile </a>, and if changes happen and docker needs to rebuild a certain layer then everything under that layer will be rebuilt. its important to remember that when creating the dockerfile thats why we we COPY the requirements.txt file first and install dependencies before COPYing the rest of the app. This results in a Docker layer containing all the dependencies. 



## Run container based on image
we use the docker run command to run the container based on image, <br>
$docker run --name flaskapp -v$PWD/app:/app -p5000:5000 docker-flask:trial

#### Explanation docker run container

1. The flag --name allows you to give your container a name 
2. The -v option mounts the app folder on the host to the container.
3. The -p option maps the port on the container to the host.


### Using Ngnix and uwing to run app
$ docker run -d --name flaskapp --restart=always -p 80:80 docker-flask:trial


