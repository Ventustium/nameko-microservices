SERVICES := user library web-ui user-library

# build-base:
# 	docker build -t nameko-microservices-base -f Dockerfile .
# 	docker build -t nameko-microservices-phpmyadmin -f phpmyadmin.Dockerfile .

# build: build-base
build:
	for service in $(SERVICES); do make -C ./services/$$service build-images service-name=$$service; done
	