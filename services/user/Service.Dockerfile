FROM nameko-microservices-base

COPY . .

CMD [ "nameko", "run", "--config", "config.yml", "service" , "--dev"]
