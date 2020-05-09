import subprocess
import sys
import uuid

def create_stack():
    """
    Helper function to create a stack/changeset
    """
    try:
        #Try creating stack
        subprocess.run('aws cloudformation create-stack --stack-name sam-codebuild-full-iam --template-body file://cloudformation_template_full.yaml --capabilities CAPABILITY_NAMED_IAM',stdout=sys.stdout,stderr=sys.stdout,check=True)
    except subprocess.CalledProcessError as e:
        print("Stack already exists, creating changeset...")
        subprocess.run(f'aws cloudformation create-change-set --stack-name sam-codebuild-full-iam --change-set-name changeset-{uuid.uuid4()} --change-set-type UPDATE --template-body file://cloudformation_template_full.yaml --capabilities CAPABILITY_NAMED_IAM',stdout=sys.stdout,stderr=sys.stdout,check=True)
    
if __name__ == "__main__":
    create_stack()