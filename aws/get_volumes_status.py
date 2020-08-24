import boto3
import os
import datetime

os.environ['AWS_SECRET_ACCESS_KEY']="<secret_key>"
os.environ['REGION']="us-west-2"
os.environ['AWS_ACCESS_KEY_ID']="<access_key>"


client = boto3.client('ec2',region_name="us-west-2")
# Retrieves all regions/endpoints that work with EC2
response = client.describe_regions()
for reg in response['Regions']:
    print('Region:', reg['RegionName'])
    print("VOLUME_ID              | STATUS    | ATTACEMENTS   | CREATION_DATE  | EVENT                                        | EVENT_DATE")

    client = boto3.client('ec2',region_name=reg['RegionName'])

    # create a list where the volume ids of unused volumes will be stored
    volumes_to_delete = list()

    # call describe_volumes() method of client to get the details of all ebs volumes in given region
    volume_detail = client.describe_volumes()

    # process each volume in volume_detail
    if volume_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
        # print(volume_detail)
        for each_volume in volume_detail['Volumes']:
            # the volumes which do not have 'Attachments' key and their state is 'available' is considered to be unused
            if len(each_volume['Attachments']) == 0 and each_volume['State'] == 'available':
                volumes_to_delete.append(each_volume['VolumeId'])
                volumeid=each_volume['VolumeId']
                state=each_volume['State']
                attachmnet_count=len(each_volume['Attachments'])
                created_date=each_volume['CreateTime']
                event_name=""
                event_time=""
                # print(each_volume['VolumeId'])
                client = boto3.client('cloudtrail',region_name=reg['RegionName'])
                response = client.lookup_events(
                                LookupAttributes=[
                                    {
                                        'AttributeKey': 'ResourceName',
                                        'AttributeValue': each_volume['VolumeId']
                                    },
                                ]
                            )
                if response['Events']:
                    for  event in response['Events']:
                            # print(event['CloudTrailEvent'])
                        if event_name not in ["DetachVolume","AttachVolume"]:
                            if event['EventName'] in ["DetachVolume","AttachVolume"]:
                                event_name=event['EventName']                      
                                print(volumeid+"  | "+state+" | "+str(attachmnet_count)+"             | "+str(created_date.strftime('%b/%d/%Y'))+"    | "+event_name+"                                 | "+str(event['EventTime'].strftime('%b/%d/%Y')))
                            else:
                                event_name="No Detach/Attach events found in last 90 days"
                                event_time="NA"
                                print(volumeid+"  | "+state+" | "+str(attachmnet_count)+"             | "+str(created_date.strftime('%b/%d/%Y'))+"    | "+event_name+"| "+event_time)

                else:
                    event_name="No events from last 90 days"
                    event_time="NA"
                    print(volumeid+"  | "+state+" | "+str(attachmnet_count)+"             | "+str(created_date.strftime('%b/%d/%Y'))+"    | "+event_name+"                  | "+event_time)

    print(len(volumes_to_delete))
        
