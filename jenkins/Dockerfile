FROM jenkins/jenkins:lts

# Disable setup wizard
ENV JENKINS_INSTALL_RUN_SETUP_WIZARD=false
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

USER root

# Install Python + pip + venv + Docker CLI
RUN apt-get update && apt-get install -y \
    python3-full \
    python3-pip \
    python3-venv \
    docker.io && \
    groupadd -f docker && \
    usermod -aG docker jenkins && \
    chmod 666 /var/run/docker.sock || true && \
    rm -rf /var/lib/apt/lists/*

USER jenkins

# Plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# JCasC
COPY jenkins.yaml /usr/share/jenkins/ref/casc_configs/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/casc_configs/jenkins.yaml

# Init scripts
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/