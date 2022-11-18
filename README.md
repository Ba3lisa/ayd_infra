## Prerequisites
- Because we are using github free we can't protect branches so please only use PRs to push to branches
- Make sure to have an account on https://hub.docker.com/
- Install docker-compose on your system current tested version:
```
❯ docker-compose --version
Docker Compose version v2.12.2
```

## Installation steps
1. Run `./update_images.sh`
2. Run `docker-compose up`
3. To run dev bot first in another terminal run `docker exec -it dev-bot bash` then inside the container run `python main.py`
4. Start Developing
