#This script can delete all the instances in all the aws regions whether there termination protection is enabled for more refrence go to url
#https://blog.datasyndrome.com/howto-terminate-all-ec2-instances-in-all-aws-regions-5213302ffa92

for region in `aws ec2 describe-regions --output text | cut -f3`
do
  echo "Terminating region $region..."
  aws ec2 describe-instances --region $region | \
    jq -r .Reservations[].Instances[].InstanceId | \
      xargs -L 1 -I {} aws ec2 modify-instance-attribute \
        --region $region \
        --no-disable-api-termination \
        --instance-id {}
  aws ec2 describe-instances --region $region | \
    jq -r .Reservations[].Instances[].InstanceId | \
      xargs -L 1 -I {} aws ec2 terminate-instances \
        --region $region \
        --instance-id {}
done
