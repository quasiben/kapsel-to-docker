# Kapsel To Docker

docker build -t "k2d:v1" .
docker build -t "k2d:v1" . --no-cache

docker run -t -i  k2d:v1 /bin/bash


docker rmi $(docker images | grep "^<none>" | awk "{print $3}")



## Usage

- k2d create <KAPSEL DIR>
- k2d list
- k2d upload?
