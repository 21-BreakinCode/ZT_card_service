---
source: container
tags:
  - programming/container
---
> https://docs.docker.com/engine/reference/builder/#format

> [!abstract] Build and run SINGLE container
> A text document that contains all the commands a user could call on the command line to assemble an image.

# Instructions

- `FROM`: 
	- specify base image
- `WORKDIR`: 
	- any following cmd will be ==executed relative to this path==
- `COPY ./ ./`: 
	- copy additional files into container
	- 1st `./` is the copy source from local
	- 2nd `./` is place to put in container
- `RUN`: 
	- run cmd ==during== the build process
- `CMD`: 
	- run cmd ==after== the build process
- `EXPOSE`: 
	- informs Docker that the container listens on the specified ==network ports== at runtime.


```dockerfile
# Specify the base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies and prepare the environment
RUN apk add --update --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Set the default command to run the application
CMD ["python3", "app.py"]

# Expose the specified network port
EXPOSE 8000
```