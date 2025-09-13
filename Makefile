DOCKER_USERNAME ?= hsiangjenli
APPLICATION_NAME ?= hexo-icarus
DATE ?= $(shell date +%Y-%m-%d)

build:
	docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE} .
	docker tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

push:
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE}
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

serve:
	docker run --rm -it -v ${PWD}/source:/app/source -v ${PWD}/scripts:/app/scripts -w /app -p 4000:4000 ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest