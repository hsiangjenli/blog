DOCKER_USERNAME ?= hsiangjenli
APPLICATION_NAME ?= hexo-icarus

build:
	docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME} .

push:
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}

serve:
	docker run --rm -it -v ${PWD}/source:/app/source -v ${PWD}/scripts:/app/scripts -w /app -p 4000:4000 ${DOCKER_USERNAME}/${APPLICATION_NAME}