build:
	clear
	docker build -t python_local_image .
run:
	clear
	docker run --name python_local_container python_local_image
