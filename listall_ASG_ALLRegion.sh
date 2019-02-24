for region in `aws ec2 describe-regions --output text | cut -f3`;do echo -e "\nListing Auto scaling group in region:'$region'"; aws autoscaling describe-auto-scaling-groups --region $region;done
