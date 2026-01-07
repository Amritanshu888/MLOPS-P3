## Azure Deployment
1. Container Registry
2. Docker Set up in local and push container registry
3. Azure Web app with container
4. Configured the github Deployment center

- Now initially the first step will be that i will convert my web application or whatever application i have created into a docker image. Then this docker image will be deployed in the server that we are going to use. In AWS it was EC2 and right now we are going to use Azure Web App.
- In AWS the docker image is currently a private image and not public ---> In companies also the application that u will develop will be private and not public.
- So the docker image is created as a private image and then this private image is deployed into something called as container registry. And this container registry is the Azure's one.
- Like in AWS we have ECR, and there also if u want to upload the dokcer image u use ECR.
- Similarily in Azure we use Azure Container Registry.
- Once we upload docker image over here we need to create azure web app and this web app will be just like my server(just like how we had AWS EC2 instance).
- And the container registry will be pulled over into Azure web app and then installed.
- So this is the mechanism which we will use for Azure Deployment.

## Steps:
- Go to ur microsoft azure and there u search for container registry, Click on Container Registries once it appears. There u will see the container registries that are already been created.
- Click on +Create button on top left to create new container registry. Under project details ur subscription will already be selected(here u have a option of pay as u go).
- Then we will go to the resource group, we will add the name of the resource group something like "testdocker" and click "ok".
- Under instance details for Registry Name enter the same name "testdocker" --> This registry name will be holding ur entire docker image.
- Location we will select as "Central US" and then below we click on "Next Networking" --> Let the default values be there.Then click on "Next Encryption". On the encryption page below click on "Review + create" ---> entire thing will get created there below u click on "Create Button" ---> U basically u are creating a container registry wherein all my docker image that i m actually going to create from my local i will put it over here.

- Next thing is i will create my Azure web app but it will be w.r.t my container bcoz now i m not directly doing the deployment from the web app.

- Ur container registry will be created with the name "testdocker" on that page u will have a button "Go to resource" under next steps, click on it, ur "testdocker" resource will be there.
- On the left sidebar under settings we have 'Access Keys' click on it, it will show u 3 things: Ur Registry Name, Login Server, Admin User(which will be initially disabled) --> U have to enable it. Copy the value in ur Login Server and keep it safe and handy as u will be requiring it. Once u enable it we get the password copy and save that also. Saving this password bcoz i need to give the authentication when i push my docker image to this particular container registry itself.

- In ur container "testdocker" on the left side bar click on 'Overview" ---> U will see that everything is created.

## Azure Web Container
- Search for Azure Web Container after going back to the home page.
- If u don't find it click on + icon of create a resource there u will get "Web App" under it there will be a create button click on it.
- Again ur subscription will be already filled, in Resource Group(A Resource group is a container that holds related resources for an Azure solution) enter the Name* for Resource group: "testdocker" --> It will show the group with the same name already exists , there u can select some different resource name like "mlproject".

- Then under instance details: For Name* enter : testdocker, for publish select: Docker Container for operating system select linux and for region select : Central US, and then below this Linux Plan will already be selected as per the location. Keep rest of the default values as the same, then click "Next:Docker" in options select 'Single Container', keep image source as 'Azure Container Registry', go and select ur registry with the registry name. Then we go to Image which is currently not there.

## How to build the Image ??
- I will build the image from my specific project repository over here.
- U have ur docker file created with u in the same project directory.
- Just open the terminal(u really need to have docker desktop installed and running in backend).
- Run the following from the terminal:

- docker build -t testdocker.azurecr.io/studentperformance1:latest .      ----> (testdocker.azurecr.io) this is the url of my container registry(this is important this is why i saved it earlier).   Here 'studentperformance1' is ur application name(u can take any application name of ur choice).
- Once u do this ur docker image will be builded ---> The docker image which will get generated will be somewhere around 1.5GB
- In the command first we have our container registry url, then we have our application name, and then we have our '.' which says from ur current directory.
- So now we will take this particular image and then we will do the deployment by using the below 2 commands where first we need to login to the registry and then push it into our registry.
- This naming convention is basically saying where ur registry url is or what ur registry url is. This was the reason why we copied and saved ur registry url before.

- docker login testdocker.azurecr.io   ---> Take the above created docker image and push it inside(testdocker.azurecr.io) --> Why ?? Bcoz this is my container registry. By this command we just login to our container registry.
- As u enter it will ask u our username and password saying 'Authenticating with existing credentials..'
- Write ur Username: "testdocker" and password u have already saved in the above steps just enter it. For pasting the password just do right click and then press enter.
- Now there u will see login succeeded

- docker push testdocker.azurecr.io/studentperformance1:latest  ---> The entire docker image is getting pushed into the container registry.

## Coming Back to Azure Web Container
- Go back to the home page
- Then go to container registries --> There u will get ur 'testdocker' container registry and inside this u will be able to see this entire docker image once it comes. Entire 1.5GB of docker image will be pushed to this container registry.
- Ur entire docker image will be pushed to this container registry.
- Go to ur container registry, on left sidebar we have repositories and there u will be able to see ur docker image file.

## Coming Back to Creating Web App
- Home Page ---> Click 'Create Resource' ---> 'Web App'(under this click 'create').
- Enter the resource group i.e. 'testdocker'. And then after selecting this under instance details in Name* we enter 'studentperformancecheck' , under Publish we select 'Docker Container', operating system we select as 'linux', region we select as 'Central US' bcoz its very much near to india itself. Then click 'Next: Docker' in options we select 'Single-Container', Image source we set it as 'Azure Container Registry'. Then in Azure Container Registry Options in Registry* we enter/select 'testdocker' and then in image automatically 'studentperformance1' will be there and the tag field will be 'latest'. Then we click 'Next:Networking'. There enable public access should be 'on'.
- Then click 'Next Monitoring' there Enable Application Insights should be No, everything is ok so then click 'Next:Tags' there also everthing is ok, finally click on 'Next:Review + create'.
- After this under Deployment, in Continuous deployment we can see: "Not enabled/Set up after app creation" finally click the "Create" button below.
- Then in Azure Home page under recents u should be able to see 'testdocker' as resource group. There is also another testdocker as container registry.
- Click on that testdocker resource group here only u will be able to see that web app, once this deployment takes place click on "Go to resource".
- U will be directed to "studentperformancecheck" page, there under deployment click on deployment center and let this get loaded
- In testdocker resource group we have this 'studentperformancecheck' click on it and then there we are going to Deployment Center under Deployment, there we will get a option of Continuous Deployment which will be initially off and we will turn it 'On'. Also there in Source we have to select "Github Actions: Build, deploy, and manage your container app automatically with GitHub Actions". Under organization we can select our organization above it ur GitHub account will be getting displayed like : "Signed in as : Ur account" u can also change it from there , below this we select our required repository through which we want to connect. Branch will be main/master, registry will be testdocker and image automatically will be studentperformance1.

- Now what will happen is that from the github each time the build will happen w.r.t the docker image it will go and replace in this particular registry, it will put entire docker image in this registry. Now all these things are done so on top we have save button where we will save it. 
- Now once u save it and then go to github actions of that particular repo u will see that the workflow in github actions is running. Whenever we make any changes this will automatically run.
- In the workflow for the deploy part u will get Evaluated environment URL, just click on it ---> It will take couple of seconds but then the website will run and will be available.


## Notes:
- Container Registry is used to store docker image, in AWS we had ECR repository for storing the private docker images.
- ECR to AWS RC2 instance and here Container Registry to specifically we are exporting it to the Azure Web App.

- To open the website u can also go to studentperformancecheck ---> (In overview only), there u can click 'Default Domain' or simply the browse option on the nav bar to open ur application. Copy the default domain and paste it in the chrome browser to get ur web app. Once the home page of the web app appears there in front on the url of the web app write this: /predictdata ---> to get the prediction page. Enter the values to predict.

- After doing everything just go and delete the Resource group and Container Registry.
- Note: testdocker is a resource group and under this we have a studentperformancecheck which is a App service(resource type) and testdocker which is a Container Registry(resource type).