# Deploy R Code to AWS Lambda using Docker and GitHub Actions 


### Overview
This repository provides a working example to demonstrate deploying an R script to AWS Lambda via a Docker container. This is all automated through the AWS Cloud Development Kit (CDK) and GitHub Actions.


### Usage

Add your AWS credentials as GitHub secrets named AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

A GitHub Actions workflow is already configured in ```.github/workflows/main.yml```

Pushing changes to the main branch or manually running the workflow will initiate the GitHub Actions workflow.



