FROM jenkins/jenkins:lts

USER root

# Install Python + pip + Docker client
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    docker.io \
    && apt-get clean

# Install Jenkins plugins from list
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Copy JCasC file
COPY jenkins.yaml /var/jenkins_home/casc_configs/jenkins.yaml

# Copy groovy init scripts
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/

USER jenkins
