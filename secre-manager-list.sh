CREDS=`aws secretsmanager --region us-east-1 get-secret-value --secret-id arn:aws:secretsmanager:us-east- | jq -r '.SecretString'`
export DBUSER="`echo $CREDS | jq -r '.username'`"
export DBPASS="`echo $CREDS | jq -r '.password'`"
echo "export DBPASS=\"$DBPASS\"" >> /home/ubuntu/.bashrc
echo "export DBUSER=$DBUSER" >> /home/ubuntu/.bashrc
