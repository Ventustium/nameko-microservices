build-images:
	docker build -t nameko-microservices-$(service-name)-service -f ./Service.Dockerfile .
	docker build -t nameko-microservices-$(service-name)-gateway -f ./Gateway.Dockerfile .