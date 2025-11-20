FROM jenkins/jenkins:lts

# Disable setup wizard (NEW REQUIRED ENV)
ENV JENKINS_INSTALL_RUN_SETUP_WIZARD=false

# Older JAVA_OPTS still OK
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

USER root
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
USER jenkins

# Install plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# JCasC configuration MUST be in /usr/share/jenkins/ref/casc_configs
COPY jenkins.yaml /usr/share/jenkins/ref/casc_configs/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/casc_configs/jenkins.yaml

# Init Groovy scripts
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/
