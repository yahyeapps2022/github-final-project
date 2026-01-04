FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# build: in this simple static example there is no build step, we'll serve source
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app /app
RUN npm install -g serve
EXPOSE 3000
CMD ["serve","-s","/app/src","-l","3000"]
