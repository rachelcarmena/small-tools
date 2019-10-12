#!/bin/bash

# NOTE: It only considers the first 100 contributors!
# If there are more than 100 contributors, request more pages of results

OWNER=
REPOSITORY=

# In order not to have a limit of 60 requests per hour
USER=
TOKEN=

curl "https://api.github.com/repos/$OWNER/$REPOSITORY/contributors?per_page=100&page=1" | jq '.[] | @uri "https://api.github.com/users/\(.login)"' > contributors.txt

for contributor in $(cat contributors.txt); do 
    CONTRIBUTOR=$(echo $contributor | tr -d \")
    curl -u $USER:$TOKEN $CONTRIBUTOR | jq '. | {name: .name, avatar: .avatar_url} | @sh "<div id=contributor><img src=\(.avatar) /><br /><div id=name>\(.name)</div></div>"'
done
