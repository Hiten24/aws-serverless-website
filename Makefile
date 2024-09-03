.PHONY: build

build:
	sam build


deploy-infra:
	sam build && aws-vault exec hiten --no-session -- sam deploy


deploy-site:
	aws-vault exec hiten --no-session -- aws s3 sync ./website s3://hiten-cloud-resume

invoke-get-visitors:
	aws-vault exec hiten --no-session -- sam local invoke GetVisitorsFunction

invoke-put-visitors:
	aws-vault exec hiten --no-session -- sam local invoke PutVisitorsFunction