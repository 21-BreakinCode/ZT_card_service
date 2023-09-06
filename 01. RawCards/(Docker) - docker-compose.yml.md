---
source: container
tags:
  - programming/container
---
> [!example] Use case
> To build MULTIPLE container in a configuration file


# Explain
```yaml
version: '3'
services: 
	redis-server:  # Redis server
		image: 'redis'
	node-app: # using "Dockerfile" in current directory
		restart: on-failure 
		# restart policy: no, always, on-failure, unless-stopped
		build: .
		ports:
			- "4001:8081" # map port: 4001 -> 8081
```

- Two services → **redis-server** & **node-app** 
> [!abstract] Restart policies explain:
> 
> - `no` : Never attempt to restart this . container if it stops or crashes
> - `always` : If this container stops _for any reason_ always attempt to restart it
> - `on-failure` : Only restart if the container stops with an error code
> - `unless-stopped` : Always restart unless we (the developers) forcibly stop it

# CMD
```bash
docker-compose up --build  # rebuile or buile docker image
```

```bash
docker-compose up -d  # launch compose in backgroud
```

```bash
docker-compose down  # stop & delete container
```

```bash
docker-compose ps  # print out status of docker compose
```