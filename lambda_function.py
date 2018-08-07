import jenkins

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    print(response)

    return response

def lambda_handler(event, context):
    print (event['currentIntent']['slots']['JenkinsJobName'])
    if event['currentIntent']['slots']['JenkinsJobName'] == "prod":
        server = jenkins.Jenkins('http://54.85.232.121:8080/', username='deloitteadmin', password='')
        server.build_job('deploy_pizza_to_prod_app_server',
                     {'ip_address': '34.198.25.2', 'deploy_db': 'True', 'deploy_backend': 'True',
                      'deploy_frontend': 'True'})
    data = "Build " + event['currentIntent']['slots']['JenkinsJobName'] + " Triggered"
    return close(event['sessionAttributes'], 'Fulfilled', {'contentType': 'PlainText', 'content': data})

if __name__ == '__main__':
    lambda_handler(event=None, context=None)

# from jenkinsapi.jenkins import Jenkins
#
# jenkins_url = 'http://<server url>/'
# server = Jenkins(jenkins_url, username = 'myUser', password = myPass)
#
# job_instance = server.get_job('the job name')
# running = job_instance.is_queued_or_running()
# if not running:
#    latestBuild=job_instance.get_last_build()
#    print latestBuild.get_status()