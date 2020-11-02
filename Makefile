.PHONY: deploy deploy-local run-integration-test run-unit-test

deploy: 
	sls deploy

deploy-local:
	sls deploy --stage local --region ${REGION} --config ./serverless-localstack.yml
	chmod u=rwx,go=r .serverless/homeboy-sls-local.zip

run-integration-test: