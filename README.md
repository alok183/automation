# GUIDE
### aws
 - boto3 - [aws_get_memcached_filtered by VPC](aws/aws_get_memcached_with_vpc.py)\
   usage:\
   vpc_list = \["vpc1","vpc2","vpc3"\]\
   getMemcachedList(vpc_list)
   
 - boto3 - [auto_scaling_group_filtered by VPC](aws/auto_scaling_group.py)\
   usage:\
   asg_list = get_asg(vpcid)\
   /* this will write asg count in a file and can we read to set back the Minsize and Maxsize of the asg automatically. */
   
 - Controlling your AWS costs by deleting unused Amazon EBS volumes\
   [get_volumes_status.py](aws/get_volumes_status.py)
   
   Description: 
   1. Get output with Volume ID/Creation Date/Attachments/Event name/Event Date
   2. Filter based on the requirement.
   3. Unsed volumes can be filtered for deletion to save cost.
   
   USAGE:
    1. Set the aws credentials
    2. python get_volumes_status.py
   

### Shell

### Salt
  - jinja - [jinja load and merge yml](jinja_load_and_merge_yml.jinja)\
    usage:
    ```yaml
    # usage.sls
    {% from "jinja_load_and_merge_yml.jinja" import config  with context  %}
    create_values_yaml:
    file.managed:
    - name: /opt/user.yaml
    - user: root
    - group: root
    - mode: 640
    - makedirs: True
    - contents: |
         item: {{ config.item1 }}
         userad: "{{ config.user_addrs }}"
    ```
### [Terraform-example](terraform-example) includes

```
1. Define versions  of the terraform and provider aws
2. Usage of Module for different resources
3. AWS authentication provider 
# Terraform first will check environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) and if profile is defined then check in default location ~/.aws/credentials and if location is specified then in the speficied credentials file (if not found in default location)
4. Custom tfvars file(default naming it will auto pick is terraform.tfvars) which can be passed with to the terraform command using -f option 
```
### [kapitan](kapitan) : Generic templated configuration management for Kubernetes, Terraform etc.
```
spin up the container has the kapiton installed with example checkoit from git
command to start containet -
a) go to the kapitan directory
b) run docker-compose up -d
```
