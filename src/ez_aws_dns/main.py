import requests
import boto3

config = {}

def main():
    getAWSCreds()
    getIp()
    getR53Config()
    doUpdate()

def getAWSCreds():
    print("Getting creds")

def getIp():
    r = requests.get("http://icanhazip.com/")

    if r.status_code != 200:
        raise "Can't figure out external ip"

    config["new_ip"] = r.text

def getR53Config():
    config["zone_id"] = "Z3GAVLTARPYGKC"
    config["record_name"] = "test.robmcbride.dev"

def doUpdate():
    client = boto3.client('route53')

    response = client.change_resource_record_sets(
        HostedZoneId=config["zone_id"],
        ChangeBatch={
            "Comment": "Automatic DNS update",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": config["record_name"],
                        "Type": "A",
                        "TTL": 60,
                        "ResourceRecords": [
                            {
                                "Value": config["new_ip"]
                            },
                        ],
                    }
                },
            ]
        }
    )