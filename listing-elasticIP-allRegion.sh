for region in `aws ec2 describe-regions --output text | cut -f3`;do echo -e "\nListing Elastic IP in region:'$region'"; aws ec2 describe-addresses --region $region;done
