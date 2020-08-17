def get_asg(vpcid):
    today = datetime.utcnow().strftime('%Y%m%d')
    session = get_session(os.getenv('REGION'),
                          os.getenv('ACCESS_KEY_ID'),
                          os.getenv('SECRET_KEY'))
    # # Connect to asg
    client = session.client('autoscaling')
    response = client.describe_auto_scaling_groups()
    # print(response)
    subnetList = get_subnet(vpcid)
    asgList = []
    os.makedirs(os.path.join(data_path,vpcid) , exist_ok="TRUE")
    for asg in response['AutoScalingGroups']:
        # print (instance)
        subnet_id = asg['VPCZoneIdentifier'].split(',')
        subnet_id = subnet_id[0]
        if subnet_id in subnetList:
            asg_name = asg['AutoScalingGroupName']
            logger.info("Creating file for ASG : {0}".format(asg_name))
            asgList.append(asg_name)
            min_size = asg['MinSize']
            desired_capacity = asg['DesiredCapacity']
            if (min_size > 0 or desired_capacity > 0):
                with open(os.path.join(data_path,vpcid,asg_name+'.asg'), "w") as f:
                    f.write(asg_name+'____'+str(min_size)+'____'+str(desired_capacity))
                    f.close()
    return asgList
