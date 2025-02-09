FROM node:20-alpine

WORKDIR /app

COPY package.json yarn.lock /app/

RUN apk add --no-cache bash git openssh \
    && npm install --production \
    && npm install -g hexo-cli hexo-theme-icarus make sass

COPY . /app/

CMD ["sh", "-c", "hexo clean && hexo generate && hexo server -p 4000"]