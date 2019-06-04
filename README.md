# Dockerize a simple Flask app
Docker is a great tool for building microservices, allowing you to create cloud-based applications and systems. To make the most of it via your terminal.
Here I will be dockerising a simple flask app

## Dockerfile
This defines instructions used to build a docker image, details of the dockerfile for this project is found in the <a href="/Dockerfile"> Dockerfile </a>

#### Explanation of the Dockerfile commands

* FROM - Specifies the base image from which the image is built. 
* MAINTAINER - Specifies the name and email of the owner

* RUN - Runs installation files. you can add additional content to the image by running installation tasks and storing the results of these commands. 
In this project we install python3 and pip. We then use pip in the second RUN command to install all packages in the requirements.txt file.

* COPY - copies files/directories from the host machine to the container during the build process. 

* WORKDIR - sets the working directory 

* ENTRYPOINT - Defines the entry point of the application, this makes the container executable. in our case its python3. 

* CMD - you put the file you need run after the entry point.
I like to think of ENTRYPOINT and CMD as the duo that executes the app. => terminal vesrion is  '$python3 app.py'


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
First I created the <a href="/ngnix.conf"> Ngnix configuration file </a>
I also created a <a href="/ngnix.conf"> laucher script </a> to add to the CMD command
<br>
$ docker run -d --name flaskapp --restart=always -p 80:80 docker-flask:trial

### Explanation 
1. The d flag
2. --restart will restart always
3. --name the name of conntainer 
4. -p maps port of container to host

##### Delete container 
$ docker stop flaskapp && docker rm flaskapp

## Resources
1. https://stackabuse.com/dockerizing-python-applications/

2. https://nickjanetakis.com/blog/docker-tip-2-the-difference-between-copy-and-add-in-a-dockerile

3. https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481

