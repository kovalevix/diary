lint:
	black project
	isort project
	flakeheaven lint project
	mypy project

run-local:
	uvicorn project.server.app:app --reload
