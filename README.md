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

### Shell

### Salt
  - jinja - [jinja load and merge yml](jinja_load_and_merge_yml.jinja)\
    usage:\
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
