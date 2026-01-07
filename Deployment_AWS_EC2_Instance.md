- Additionally i need to create a Dockerfile.
- This Dockerfile will play a very important role, why docker is required ?? --> Bcoz with the help of docker u will be able to create containers irrespective of the OS that is specifically being used in the server.

- In CMD, write : docker images --> u will see already existing/created images
- We will push all this entirely to github and then the deployment will happen

- B4 this we need to understand this workflow .github->workflows->main.yaml file
- Bcoz of this workflow only the entire deployment will happen
- And this workflow has both CI-CD pipeline integrated.

## Steps
1. Docker Build Checked
2. Github Workflow
3. Creating IAM user in AWS

## Creating IAM user
- Go to the AWS console.
- Search for IAM, under IAM click on users. --> There u will have the list of IAM users, we can creat it or delete it.

## Why do we require this IAM ??
- It is nothing but identity and access management.
- Let's say that i m a admin and i want some people to work in my team and my companies entire deployment usually happens in the AWS so being a admin i cannot just give my entire admin access to everyone, so what we do is that for the people who are working in some specific cloud service like in AWS we are probably going to use service like ECR, or EC2 instance , so i will give services for only these two so the users will be able to get permissions and they will be able to work over here.

- So in IAM go to users and add the user by clicking on Add users button above, enter the user name, click on next, on the next page we have permission options under which "Add User to group" is already selected ---> We will have user groups like which group this user belongs. Other Permission Options which we have is : Copy Permissions and Attach Policies directly.

- There we will select "Add Policies Directly" and then under Permission Policies search for "AmazonEC2ContainerRegistryFullAccess" please go ahead and select this and attach this(Container registry i require bcoz i m going to push my docker image over here). Next thing which we will attach is by searching in Permission Policies is "AmazonEC2FullAccess" now these two have been added so now click on next, on the next page under Permissions Summary it has given u the permissions which u have added.
- Click on Create User.
- After creating the user u will be able to see the user in the IAM. Click on that user, go to "Security Credentials" it will give u console sign in link and many other things.
- There under Access Key click on Create Access Key, on the next page select 'Command Line Interface"--> as we will be using this w.r.t the command line interface only, click on the recommendation given below on the same page then click next, on the next page no need to write any Tag value directly click on "Create Access Key".
- This access key is super important as i m going to use this. On that page itself we have a button below to "Download .csv file" download the csv file and keep it handy(details of access key)
- Click on done

## Next Step
- In AWS console search for ECR(Elastic Container Registry) --> Fully managed docker container registry: Share and deploy container software, click on it.
- There we will create a new repository, click on "Get Started", on next page click on "Create Repository", on next page we have some general settings like visibility settings --> keep it private, enter the repository name give any name like "studentperformance" --> This will basically be my ECR URL name, click on "Create Repository". Once its done our repository will be ready, copy the URI from the ECR page and paste it somewhere to save it.

## Once ECR repository created go to the EC2 instance
- EC2 instance --> Virtual Servers in the Cloud. Click on it.
- On next page click on "Launch Instance", select the web server name can be anything like "Studentperformance" next step on the same page under Quick start select "Ubuntu", under instance type we have to select which tier can we use so select "t2.medium", there will be some charges so once u test it kindly delete it.
- Next we have key-pair(login), use any of the previous key-pair name that u have or if u don't create a new key pair.
- Under network settings make ensure u enable "Allow HTTPS traffic from the internet" and "Allow HTTP traffic from the internet"
- We also have Configure storage on the same page we can also increase it as per our needs.
- Then finally click "Launch Instance"
- Now when u click on instances ur "Studentperformance" instance will be there, initially it will be in the pending state.
- After the instance is done created its state will be "Running".
- Then there only click on instance id of the created instance, there on the top left u have a button "Connect"(Connect to instance), click on it we can connect through various ways we are connect through EC2 Instance Connect , select it and then click on "Connect" --> Oncw we do this it will get connected and command prompt will be displayed here we need to do the setup just like how i got my server

- When u create EC2 instance u need to install some packages for the dockers

## Commands(Docker Setup In EC2) --> We our just setting up our linux server

## Optional
- sudo apt-get update -y  --> With help of this ur entire packages will be installed and indexed properly
- sudo apt-get upgrade    

# Required
- curl -fsSL https://get.docker.com -o get-docker.sh   ---> (We are trying to install all the necessary packages that are required specifically by the docker in the linux machine. For this 3 different commands are there and the first one is this.)
- sudo sh get-docker.sh   --> This is the second command(Just to make ensure that all the admin access is provided w.r.t this)
- sudo usermod -aG docker ubuntu   --> So that i don't have to use sudo at every point of time.
- newgrp docker                   --> We will create a new group called as docker.

- Note: Whenever we commit to the github repository that deployment should automatically happen in the EC2 instance
- Just to check if the docker is running or not in the cmd write: docker --> U will see everything

- Our main aim: From github to ECR repository my docker image will go and then docker image will get installed in EC2 instance.

- Go to github --> settings --> actions --> Runners.

- What is the main importance of this runner ??
- Whenver u do any kind of code commit into this automtically this runner should be able to get triggered and do the deployment process.
- In runners on the top right we have "New self-hosted runner", select runner image as linux once i do this i just need to execute this one line over there in command prompt and automatically my runner will start getting created.
- This line of code is under 'Download' header.
- $ mkdir actions-runner && cd actions-runner
- Moving on step by step execute all the commands on that page starting from the above command.
- We are executing all these commands in our EC2 instance command prompt which we opened above.
- When u will be executing all the commands on that page specifically commands under the header "Configure", it will ask u to enter the name of the runner group, we can simply press enter to select the name by default --> so by default the name will be taken.
- Then it will ask to enter the name of the runner: There u enter "self-hosted" --> This is my app runner name.
- Main aim of app runner: Any changes that come in the github actions it will automatically push the deployment.
- We will write self-hosted and then press enter --> self hosted will become the name of the runner.
- Then it will ask to enter "Additional Labels" we don't want to so please press enter
- Enter the name of the work folder : -----> Press enter

- Once it will be connected to github it will be listening for jobs ---> i.e. any push that is basically happening.
- When we go to settings --> actions --> runner we will see that a runner has got created named "self-hosted". This is also called as an app runner, currently its in idle state --> waiting for any commit to come.
- Any commit comes it will go ahead and push it into the EC2 instance.


## Next Step(Adding some secret keys)
- Settings --> Secrets and Variables --> Actions and there we will go and add secret keys over here under "Repository Secrets".
- We need to add the 5 keys over there by clicking on "New Repository Secret" button.
- First key: AWS_ACCESS_KEY_ID(Name) ----> It is there in the CSV file which we downloaded, copy it and paste it there in "Secret" section and then click on "Add Secret" button.
- Second Key: AWS_SECRET_ACCESS_KEY ----> again available in the csv file which we downloaded
- Third Key: AWS_REGION(Name*) and us-east-1(Secret*)
- Fourth Key: AWS_ECR_LOGIN_URI(Name*) ---> This we have already created above.(The url which we have kept and copied from above)
Note that u remove '/studentperformance' from the end of the url.
- Fifth Key: ECR_REPOSITORY_NAME(Name*) and studentperformance(Secret*)

## Testing
- Now to test i may make some changes in readme file and as soon as i commit these changes what will happen ??
- Go to the Actions page(in github under the header Actions) it is going to execute the entire workflow which we have seen in main.yaml file(present in .github/workflows)
- To re-run the workflow: Go to Actions ---> Select the workflow ---> on top right click on Re-run jobs there we have two options which are: 1. Re-run failed jobs 2. Re-run all jobs , select what u feel is convenient


- In EC2 instance, go to your instance by clicking on instances, in ur instance click on the instance id, there we have Public IPv4 address open it by clicking on Open address. Initially i will be getting a error.
- There only(after u click on instance id) u go to security, there u go to security-groups by clicking on it(the url id), then click on "Edit Inbound Rules" and there u add another rule: Type=Custom TCP, Protocol=TCP, Port range=8080(in app.py we have this 8080 port given so that is the reason we need to mention it also here in the EC2 instance), Source=Custom, 0.0.0.0/0
- The above address which u opened there in front of url u put this --> :8080 port and then execute u will get ur app web page.
- And then finally if u do like this ---> :8080/predictdata ---> just adding /predictdata over this ur prediction page will be there.
- From there u can input the values and predict the scores.
- Dockers privately if u really want to put it docker images if u want to put in AWS u have to use ECR repository and from there u want to pull and deploy it -> EC2 instance is probably used.

- If we want to scale up further we can also add load balancer.

- Next Thing: Close ur EC2 instance, u can probably go to github actions or Settings->Actions->Runners-> Going to app runner and removing it from there.
- Go to ur EC2 instance which is running, select the instance, click on Instance state and then terminate the instance. ---> As i don't want any charges to happen any more.
- Similarily go to ECR in AWS console, select the repository and delete it.
- Go to IAM user, select the user u created and delete it.
