---
source: container
tags:
  - programming/container
---
# Why 
> Easy to install & run software on <mark style="background: #FF5582A6;">any</mark> given computer

- 減少人力安裝成本
- 不用「重新」做依賴源或是套件安裝的管理
- 改善傳統需要額外安裝作業系統，導致啟動慢、佔較大記憶體問題

# What 
- Container: Hypervisor tech.
	- 建立在 OS 上，資源可以「動態」分配
- Docker Client: 
	- Controlling with [[(Docker) - Docker CLI|Docker CLI]] with RESTful API
- Docker Server: 
	- Docker Daemon
- Docker Registry: 
	- Docker Hub
- Volume: 
	- Link a container resource to local directory reference

# How
> [!abstract] How to work
> Actually is installing Linux VM in local computer, where container is being created


> [!info]- install & check
> - homebrew --> `brew install docker`
> - verify --> `docker version`

## Underlying tech
### Namespace
> Isolation between containers

- Abstraction layer to keep containerized process separate
    - Provide a level of resource isolation that enables running multiple containers with separate system resources within the same host, without them interfering with each other
- Types
    - PID - Process IDs
        - process only see their own process
    - Network - NET
        - own network interfaces, routing tables, firewall…
    - Mount - MNT
        - file system mount points has its own root file system
    - UTS - UNIX time sharing system
        - own hostname & domain name
    - User - USER
        - maps user & group identifiers
        - different permissions settings
    - IPC - Inter-Process communication
        - communication between process in different containers controlling

### cgroups
> Linux kernel feature allows to allocate & manage resources

- resource allocation
- limiting resource
- prioritizing containers
- monitoring the resource

### union filesystems
- Layered Structure
    - This structure enables efficient handling of changes by only updating the writable layer, while the read-only layers preserve the original data.
- Resource sharing
    - allow multiple containers to share common base layers while running separately.

## Data persistence
### Bind mount
> `HOST` managed

- share with host
- operate at host level
- storage location map to host
- data will be lost if host directory is deleted
### Volume mount
> `Docker` managed

- Ref: https://docs.docker.com/storage/volumes/
- share between containers
- managed by Docker
- storage location is managed by Docker
- data persist even if container is removed

## Runtime configuration
- Resource mgmt → cpu, memory…
- Security → ~~root user~~, another user
- Networking → `-p` (publish port); `--hostname` & `--dns` publish dns