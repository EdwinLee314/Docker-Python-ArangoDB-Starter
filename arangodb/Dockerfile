# this is an official Arango runtime, used as the parent image
FROM arangodb/arangodb:3.3.8

# copy the startup script
# ADD ./scripts /scripts

# copy the install files
# ADD ./guesser-foxx.zip /install/guesser-foxx.zip

# expose data, apps and logs
# VOLUME ["/data", "/apps", "/apps-dev", "/logs"]

# database is running on port 8529
EXPOSE 8529

# start the node server
# CMD [ "/scripts/start.sh" ]