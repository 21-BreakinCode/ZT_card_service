---
source: container
tags:
  - programming/container
---

> [!info] Reference
> - [Official CMD options](https://docs.docker.com/engine/reference/commandline/cli/)


# Example
```bash
docker run -it <container_id> bash
```

# Command Options
> [!example] Brief
> 1. run
> 2. ps
> 3. stop || kill
> 4. system prune
> 5. exec -it ${container_id} sh
> 6. resource ls (`image`, `container`, `volume`, `network`)



```bash
docker run <image name> # create & run container

# create image: `docker create <image name>`
```

```bash
docker ps # list all "running" container
```

```bash
docker stop # hot shut down
docker kill # terminate immediately
```

```bash
docker system prune # 刪除相關暫存檔案
```

```bash
docker log <container ID> # returning logs run by container
```

```bash
docker exec -it <container id> sh

# exec: run another cmd
# -it: allow to provide input to container
# sh: go into container cmd processors
```

```bash
docker build -t <dockerId>/<projectName>:<version> 

# tagging image in docker
```

```bash
docker run -p <out port>:<in port> <imageName>

# -p: claim port mapping
# <out port>: local port
# <in port>: container port 
```