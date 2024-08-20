FROM guacamole/guacamole:1.5.5
EXPOSE 8080
RUN mkdir -p /opt/guacamole/adhoc &>/dev/null
COPY init.d/guacamole-auth-quickconnect-1.5.5.jar /opt/guacamole/adhoc/guacamole-auth-quickconnect-1.5.5.jar
COPY init.d/start.sh /opt/guacamole/bin/start.sh
RUN chmod 755 /opt/guacamole/bin/start.sh &>/dev/null