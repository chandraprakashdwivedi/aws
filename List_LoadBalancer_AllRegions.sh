for region in `aws ec2 describe-regions --output text | cut -f3`;do echo -e "\nListing Auto scaling group in region:'$region'"; aws elb describe-load-balancers --region $region;done
