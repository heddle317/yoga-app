source keys.sh
heroku config:set SECRET_KEY=$SECRET_KEY
heroku config:set ENVIRONMENT='production'
heroku config:set POSTMARK_API_KEY=$POSTMARK_API_KEY
heroku config:set POSTMARK_SMTP_SERVER=$POSTMARK_SMTP_SERVER
heroku config:set POSTMARK_INBOUND_ADDRESS=$POSTMARK_INBOUND_ADDRESS
heroku config:set EMAIL_PORT=$EMAIL_PORT
heroku config:set DEFAULT_FROM_EMAIL=$DEFAULT_FROM_EMAIL
heroku config:set DEFAULT_REPLY_EMAIL=$DEFAULT_REPLY_EMAIL
heroku config:set PERSONAL_EMAIL=$PERSONAL_EMAIL
heroku config:set AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
heroku config:set AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
heroku config:set AWS_BUCKET_KEY=$AWS_BUCKET_KEY
