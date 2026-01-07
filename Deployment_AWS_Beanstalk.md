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

## Deployment
- Initially go to your AWS Console.
- There u search for Elastic Beanstalk(Run and Manage Web Apps) --> Inside this, under top features: Click on application
- There u will see the applications that have got created.
- Above click on : Create a new application and then under the header Get Started on next page we have a "Create Application" button ---> Click this to create the application.

## Basic Idea of What we are doing w.r.t Deployment
- We will be using Elasic Beanstalk(This is just like a server or cloud environment of some kind of instance), instance basically means it can be a linux machine. Here we create a environment and we deploy our code. -----> And this is basically present in the AWS.
- The next thing is basically ur Github Repository. Ur code is basically there in ur Github repository.
- Only thing Elastic Beanstalk requires is the configuration over there, configuration u have actually set it up with that extensions file and u have created that python.config file.
- For deployment part we already have the github repo and there we already have the code.
- This above configuration has already been made over there in the github repository.

- For deployment there should be a way such that our code is sended to the AWS Beanstalk, whatever changes is happening in ur github code repo it should be updated at AWS Beanstalk also. For this we need to create a pipeline from github repo to AWS Beanstalk.
- For this we use something which is present in AWS and is called Codepipeline.
- What this codepipeline will do is that whatever code is over there it will commit or deploy it automatically as soom as u click a button inside this elastic beanstalk which is just like a linux machine.
- So in github repo u have the code, whenever there is any code changes automatically a button will get created saying "Do u want to deploy this code" click it u will deploy this code in the AWS elastic beanstalk and that deployment will get completed.
- So CodePipeline is a kind of a pipeline and this pipeline we say as continuous delivery pipeline.
- CodePipeline we will integrate with our github repo and then we will continue the deployment over here into the Elastic Beanstalk.

## Continuing after Elastic Beanstalk "Create Application Step"
- After u click on "Create Application"
- Next page will come with header: Create a web app
- Under Application Information, enter Application Name. --> Write any name like "studentperformance"
- On the same page under platform go and select Python.
- Under Application Code we have two options : Sample Application and Upload your code.
- If u select upload ur code then in source code origin we can upload our local zip file
- For now we are selecting : Sample Application. --> Bcoz i need to integrate with my github repo that is present.
- After selecting sample application click : "Create Application"
- As soon as i click it will be creating an environment also.
- Now we have done this part our environment will be getting created which will be our AWS Elastic Beanstalk(linux machine).

## Now we have to focus on creating our CodePipeline and integrating with the Github Repo
- Open AWS Console again
- There u search for something called as CodePipeline --> It is nothing but "Release Software using Continious Delivery". It is a CD pipeline it will automatically create CI also.
- Click on CodePipeline, then click on Create Pipeline
- In pipeline settings enter Pipeline name, give it as : studentperformance then click next
- On the next page u have a source provider like here we are integrating with the Github there may be other companies which will be using something else like gitlab
- In source provider we select : GitHub(Version 1), then click Connect to Github Button, then a dialog box will appear saying "Processing OAuth request" there u click on Confirm, then it will be successfully configured with github.
- After this under repositories we will select our repository which we want to connect, and in Branch we will enter main, then click on next.
- We will be on next page: "Add Build Stage", right now skip this stage.
- Next we will be on page saying "Add Deploy Stage" --> Here we have deploy provider, where i want to deploy from my code pipelines to AWS Beanstalk.
- In deploy provider select AWS Elastic Beanstalk, under application name select: studentperformance, under environment select the environment which we have created previously in beanstalk, then click on next.
- On the next page it will show us our entire pipeline settings. It will be showing u ur entire stages which we have. There on this page click on "Create Pipeline". Make ensure u delete the app.py file to make it easy for the AWS to deploy it. Only application.py file should be there. Delete app.py and keep application.py which has the same code.
- After the deployment in done click on the link given in the deployment, there u have the environment, URL is also provided to see the application.
- Once u click the URL , u will be able to see that ur Home Page(from our app) is running.
- In front of link u just write : /predictdata ---> U will be on the prediction page where u can enter the values and predict to get the prediction value.
- U go to the same repo on github, and then go to actions u will see that nothing has happened this is bcoz we have created a CD pipeline and not CI pipeline, if u also create CI pipeline u will be able to see everything in this github actions also.

- Now lets say if i make some simple changes in the github repo, like if i go to requirements.txt and add some simple library or some extra space and then commiting it, now automatically as soon as i commit it, in the studentperformance pipeline it will ask for "Release Change" ---> that update it is being able to understand, now if u go and do the release change, the entire pipeline will run again and the deployment will happen w.r.t the new code that has been changed.