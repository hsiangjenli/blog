FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json /app/

RUN apk add --no-cache bash git openssh \
    && npm ci --omit=dev

COPY . /app/

CMD ["sh", "-c", "npm run clean && npm run build && npm run server -- -p 4000"]
