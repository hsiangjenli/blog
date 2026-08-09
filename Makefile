DOCKER_USERNAME ?= hsiangjenli
APPLICATION_NAME ?= hexo-icarus
DATE ?= $(shell date +%Y-%m-%d)
DRAFT_TEMPLATE ?= source/_templates/it_blog.md
DRAFT_FILE ?= source/_posts/draft.md

.PHONY: build push serve draft

draft:
	cp $(DRAFT_TEMPLATE) $(DRAFT_FILE)

build:
	docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE} . --no-cache
	docker tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

push:
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:${DATE}
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

serve:
	docker run --rm -it \
	-v ${PWD}/source:/app/source \
	-v ${PWD}/scripts:/app/scripts -w /app \
	-v ${PWD}/_config.yml:/app/_config.yml \
	-v ${PWD}/_config_icarus.yml:/app/_config_icarus.yml \
	-p 4000:4000 ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest