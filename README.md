### AWS SAM CI/CD
This is a sample application demonstrating the capababilities of AWS Serverless Application Model [(AWS SAM)](https://aws.amazon.com/serverless/sam/)

![alt text](https://github-cf.sourabh.org/images/aws_sam_build_process.png)


* Clone the repository
```
git clone https://github.com/soumoks/sam-python-example.git
```

There are no additional dependencies for this application.
However, a requirements.txt file is required for AWS SAM.

* Run the application
```
python create_stack.py
```

The above command creates a Cloudformation(Cfn) stack. The Cfn stack creates a AWS CodeBuild Project and necessary IAM roles.
This is part of a CI/CD pipeline which creates/updates AWS Lambda and API GW resources on a git commit using AWS SAM. 
Change git repo urls in sam_template.yml to point to your git repositories.

Further details on the CI/CD pipeline are present [here](https://medium.com/@soumoks/developing-a-serverless-ci-cd-pipeline-using-aws-sam-and-codebuild-bbd5c80d9a67).

