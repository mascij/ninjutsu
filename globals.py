# server url
SERVER_URL = "ninja.skygrid.cloud"

# Keys - AccessKey: SecretKey
PASS_PHRASE = "kHU2oPHTpjOBtea5ayVM:JtNp2lyIiGfeurkRFOJUD4GtrpYV3FVUN4DRlCVF"

# Blueprints
BLUEPRINTS = "/api/1.0/blueprints"

# URL to get list of Apps
GET_APPS = "/api/1.0/apps"

NEW_BLUEPRINT = "{\r\n   \"editable\":true,\r\n   \"inactive\":false,\r\n   \"blueprintType\":\"VM_COMPOSE\",\r\n   \"composeVersion\":\"VM\",\r\n   \"version\":\"1.0\",\r\n   \"entitlementType\":\"OWNER\",\r\n   \"params\":[\r\n\r\n   ],\r\n   \"visibility\":\"READABLE\",\r\n   \"licenseModel\":\"LICENSE_INCLUDED\",\r\n   \"yml\":\"Machine: \\n  region: HG-Datacenter\\n  group: santest\\n  image: VMT-Ubuntu1604\\n  instanceType: cpu=1,memory=1GB,disk=40GB\\n  storageAccount: vsanDatastore\\n  affinity: true \\n  network: dvs-compute-26\\n  skipAgentInstall: false\\n  authenticationType: SSH\\n  password: \\\"{{credentials | 2c91808867c8b0d70167d2296e5323a4 }}\\\"\\n  count: 1\\n  terminationProtection: DISABLED\",\r\n   \"resourcePool\":{\r\n      \"id\":\"2c91808867c8b0d70167d2287caf2390\",\r\n      \"inactive\":false,\r\n      \"deleted\":false,\r\n      \"lockVersion\":null,\r\n      \"lastModifiedDate\":null,\r\n      \"lastModifiedBy\":\"MONITORING SERVICE\",\r\n      \"createdDate\":null,\r\n      \"createdBy\":\"santosh\",\r\n      \"owner\":null,\r\n      \"ownerPk\":\"2c91808867c8b0d70167d225d06c2355\",\r\n      \"tenant\":null,\r\n      \"tenantPk\":\"2c91808867c8b0d70167d225cfc02352\",\r\n      \"entitlementType\":\"OWNER\",\r\n      \"entitledUserGroups\":null,\r\n      \"entitledUsers\":null,\r\n      \"entitledUsersPks\":[\r\n\r\n      ],\r\n      \"entitledGroupsPks\":[\r\n\r\n      ],\r\n      \"entitledTenants\":null,\r\n      \"entitledTenantsPks\":[\r\n\r\n      ],\r\n      \"name\":\"RP.VMW.HYP-HGvCenter-AZ01.RP01\",\r\n      \"cpu\":96,\r\n      \"mem\":96,\r\n      \"disk\":2048,\r\n      \"spendLimit\":1000,\r\n      \"spent\":0,\r\n      \"cpuUsed\":10,\r\n      \"memUsed\":10,\r\n      \"diskUsed\":1060,\r\n      \"cpuReserved\":0,\r\n      \"memReserved\":0,\r\n      \"diskReserved\":0,\r\n      \"provider\":null,\r\n      \"rpType\":\"RESOURCE_POOL\",\r\n      \"azId\":\"2c91808867c8b0d70167d2260814235d\",\r\n      \"azName\":\"QT.VMW.HYP-HGvCenter-AZ01.QT.VMW.HYP-HGvCenter-AZ01.QT02\",\r\n      \"quotaType\":\"restricted\",\r\n      \"resourcePoolTrigger\":null,\r\n      \"triggerEnabled\":false,\r\n      \"vmPatternEnable\":false,\r\n      \"vmPattern\":null,\r\n      \"lastAlert\":null,\r\n      \"aresourcePool\":true,\r\n      \"lastUpdated\":1545525402683,\r\n      \"createUser\":\"santosh\",\r\n      \"lastUpdateUser\":\"MONITORING SERVICE\",\r\n      \"created\":1545419127983\r\n   },\r\n   \"cloudProvider\":{\r\n      \"id\":\"2c91808866e657160166ef75a3a32462\",\r\n      \"inactive\":false,\r\n      \"deleted\":false,\r\n      \"lockVersion\":1,\r\n      \"lastModifiedDate\":null,\r\n      \"lastModifiedBy\":\"admin\",\r\n      \"createdDate\":null,\r\n      \"createdBy\":\"admin\",\r\n      \"owner\":{\r\n         \"id\":\"402881834d9ee4d1014d9ee5d73f0014\",\r\n         \"inactive\":false,\r\n         \"deleted\":false,\r\n         \"username\":\"admin\",\r\n         \"firstname\":\"HyperCloud\",\r\n         \"lastname\":\"Administrator\"\r\n      },\r\n      \"ownerPk\":\"402881834d9ee4d1014d9ee5d73f0014\",\r\n      \"tenant\":{\r\n         \"id\":\"402881834d9ee4d1014d9ee5d73f0010\",\r\n         \"inactive\":false,\r\n         \"deleted\":false,\r\n         \"name\":\"HyperCloud\"\r\n      },\r\n      \"tenantPk\":\"402881834d9ee4d1014d9ee5d73f0010\",\r\n      \"entitlementType\":null,\r\n      \"entitledUserGroups\":[\r\n\r\n      ],\r\n      \"entitledUsers\":[\r\n\r\n      ],\r\n      \"entitledUsersPks\":[\r\n\r\n      ],\r\n      \"entitledGroupsPks\":[\r\n\r\n      ],\r\n      \"accountType\":\"AVAILABILITY_ZONE\",\r\n      \"name\":\"HYP-HGvCenter-AZ01\",\r\n      \"url\":null,\r\n      \"email\":null,\r\n      \"username\":null,\r\n      \"password\":\"password-hidden\",\r\n      \"opts\":null,\r\n      \"groupName\":null,\r\n      \"hardwareId\":\"vsanDatastore\",\r\n      \"region\":\"HG-Datacenter\",\r\n      \"imageId\":\"hc-Management\",\r\n      \"imageUsername\":null,\r\n      \"imagePassword\":\"password-hidden\",\r\n      \"securityGroupId\":null,\r\n      \"networkId\":\"HG-Cluster01\",\r\n      \"referenceId\":\"2c91808866e657160166ef7333922434\",\r\n      \"referenceName\":null,\r\n      \"freeFormEntitlement\":true,\r\n      \"vmQuota\":null,\r\n      \"sizeLimit\":null,\r\n      \"approvalEnforced\":null,\r\n      \"leaseTime\":null,\r\n      \"usageStats\":null,\r\n      \"blueprintEntitlementType\":null,\r\n      \"entitledBlueprint\":[\r\n\r\n      ],\r\n      \"entitledBlueprintPks\":[\r\n\r\n      ],\r\n      \"quotaPolicies\":[\r\n\r\n      ],\r\n      \"quotaPolicyPks\":[\r\n\r\n      ],\r\n      \"capacity\":null,\r\n      \"vlanId\":null,\r\n      \"passwordHint\":null,\r\n      \"lastUpdated\":1541615756195,\r\n      \"createUser\":\"admin\",\r\n      \"lastUpdateUser\":\"admin\",\r\n      \"created\":1541615756195\r\n   },"