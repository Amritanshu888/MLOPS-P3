- Here we need to setup two important configurations whenever we are working with Elastic Beanstalk(instance that will be provided to u where u willbe able to deploy your entire application).

- Create a folder .ebextensions where we have a file: python.config
- python.config file is mainly to tell to the elastic beanstalk that what is the entry point of ur application.
- Container that we are using there is python, the code mentioned there is specifically for container as python.

- option_settings:
  "aws:elasticbeanstalk:container:python": 
    WSGIPath: application:application

- This application should be your app.py name, the entry point of the file and inside the app.py we will update the name to application(The flask app name will be application).

- In python.config we have to give in the above format only.
- Create a file application.py and copy and paste the same code from app.py.
- Note: In the application.py file code same as app.py code, remove debug=True from last(whenever we are deploying we remove that).
- application.py is basically created for deployment.

- These are the two settings that are probably required to do the deployment.