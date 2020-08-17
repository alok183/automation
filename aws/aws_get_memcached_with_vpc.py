def getMemcachedList(vpc_list):
    session_obj = createSession(os.getenv('REGION'),
                        os.getenv('ACCESS_KEY_ID'),
                        os.getenv('SECRET_KEY'))
    try:
        client = session_obj.client('elasticache')
        response = client.describe_cache_clusters()
        # logger.info(response)
        logger.info("Cache CacheClusterId is/are")
        cacheID=""
        for cache in response['CacheClusters']:
            # logger.info(cache['CacheSubnetGroupName'])
            response = client.describe_cache_subnet_groups(
                CacheSubnetGroupName=cache['CacheSubnetGroupName'],
            )
            # logger.info(response['CacheSubnetGroups'][0]['VpcId'])
            if response['CacheSubnetGroups'][0]['VpcId'] in vpc_list:
                logger.info(response['CacheSubnetGroups'][0]['VpcId'])
                if cacheID:
                    cacheID=cacheID+','
                cacheID=cacheID + cache['CacheClusterId']

        if cacheID:
            addMetricToCloudWatchTemplate("AWS/ElastiCache", "CacheClusterId", cacheID)
        else:
            logger.info("No Memcached found in {0}".format(vpc_list))
    except ClientError as e:
        logger.error(e)
