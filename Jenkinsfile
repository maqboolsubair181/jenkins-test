pipeline {
    agent any // Run this pipeline on any available Jenkins agent

    environment {
        // Define variables
        DEPLOY_SERVER_IP = "3.107.188.76" // IMPORTANT: Change this!
        EC2_SSH_KEY = 'ec2-ssh-key'
        PROJECT_DIR = '/var/www/my-python-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                // Clean the workspace before cloning
                cleanWs()
                git branch: 'master', url: 'https://github.com/maqboolsubair181/jenkins-test.git' // IMPORTANT: Change this!
            }
        }

        stage('Deploy to EC2') {
            steps {
                echo "Deploying the new version to the EC2 instance..."
                // Use the stored SSH key credential
                withCredentials([sshUserPrivateKey(credentialsId: env.EC2_SSH_KEY, keyFileVariable: 'SSH_KEY')]) {
                    // 1. Copy all application files to the deployment server
                    sh "scp -o StrictHostKeyChecking=no -i ${SSH_KEY} * ubuntu@${env.DEPLOY_SERVER_IP}:${env.PROJECT_DIR}"

                    // 2. Execute the setup and restart script on the deployment server
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ubuntu@${env.DEPLOY_SERVER_IP} '
                            cd ${env.PROJECT_DIR} &&

                            # Create a Python virtual environment if it doesn't exist
                            python3 -m venv venv &&

                            # Activate it and install/update dependencies
                            source venv/bin/activate &&
                            pip install -r requirements.txt &&

                            # Move the service file to the systemd directory
                            sudo cp mywebapp.service /etc/systemd/system/mywebapp.service &&

                            # Reload systemd, enable the service, and restart it
                            sudo systemctl daemon-reload &&
                            sudo systemctl enable mywebapp &&
                            sudo systemctl restart mywebapp
                        '
                    """
                }
            }
        }
    }
}
