# Odoo Test Project
This is my test project for learning Odoo development.

Trying to learn how to develop custom modules for Odoo 16 specifically. The learning process also involves an extra step, which is to develop with [Docker containers](https://www.docker.com/resources/what-container/) instead of publishing with it. Additionally, Dev Containers, an extension for VS Code, is also used to make development within the container easier.

This repository includes the [project setup](#Setup "Go to Setup"), [recommended worflow](#Workflow "Go to Workflow"), and also [what I've learned](#Learnings). *This repository is also mostly just a massive "note to myself". Goodluck and goodjob, me.*

**NOTE: Do not use the containers for production. The environment variables are not yet hidden, and this is solely for development purposes only. The actual Odoo 16 server is setup in an Ubuntu virtual environment, with Odoo and Postgres installed and proper configurations.**

# Setup
To setup the odoo server inside a docker container, make sure that you have the requirements installed first. Then, follow the steps below to start the development process. Note that this project has not been tested for Linux and Mac environments yet, only on Windows.

## Requirements
1. Docker desktop ([installation guide](https://docs.docker.com/desktop/install/windows-install/ "How to install?"))
2. [VS Code](https://code.visualstudio.com/ "What's VS Code? How to install?") and Dev Containers (if you have docker installed, VS Code will automatically detect that you may need Dev Containers and other Docker-related extensions.)

## Steps to start
1. Pull the project (git repository) locally and open using VS Code ("odoo-test-project" is the current workspace).
2. Once the project is opened, a popup will show with a prompt "*Folder contains a Dev Container configuration file. Reopen folder to develop in a container*", then click the Reopen button and wait for the initial build (show log to see progress). **To do this manually**, click the double bracket icon at the bottom left then select "*Reopen in Container*", or open the command palette (`Ctrl + Shift + P`), type "*reopen*", and you should be able to select the same thing. Once this is done, you should be able to see "odoo-test-project" (a docker compose) together with "odoo-db" (postgres15 image) and "odoo-web" (custom odoo16 image) in your containers in docker desktop.
3. You should now be able to see the same files in the directory ("mnt" is the current workspace) with an extra folder `extra-addons`. Start coding inside the `extra-addons` directory. **Note** that at this point, you are working inside an Ubuntu environment since that is the default OS for odoo.

## Important notes
1. The `.docker/Dockerfile.dev` file specifies that `sudo` is to be installed inside the container. This is to enable restarting the server directly inside the container.
2. The `compose.yml` file specifies that the `modules` folder is to be mounted in `/mnt/extra-addons` folder. This is because the `odoo:16` docker container initially requires custom addons to be put inside this folder ([![see dockerhub documentation](https://hub.docker.com/_/odoo "DockerHub documentation for Odoo")]). I reckon you can modify this, but be mindful of the `odoo.conf` file which should have the addons path.
3. The `extra-addons` folder will appear in your local repo, but is empty. This is fine, the folder is included in `.gitignore`.
4. Just to be safe, always push changes to a different branch other than `main`, and just pull it afterwards. This is because all the files are sometimes recommitted (idk why) when you commit inside the container.

# Workflow
Once the setup is done, you should now be able to work on the code. Some good rule of thumbs are the following.
1. Always `git pull` first before changing anything. You can also do this inside the dev container once the [setup](#Setup "Go to Setup") is done.
2. Edit on the `extra-addons` folder. Although editing on `modules` folder is also possible, the odoo server fetches files from `extra-addons` first. And so, this is just to remove the delay on file syncing (synced through mounting in docker).
3. To push changes, just simply use the usual git commands `add`, `commit`, and `push`. *Note* that you should be working in a different branch other than `main`, say,`devcontainer`.

# Learnings
This section will be updated every once in a while.
1. Docker: `pull`, `build`, `run`, `compose`.
2. A general workflow on developing inside a docker container. This mostly for cases in which I do not want to download packages locally.
3. General idea of developing odoo modules. Still need to watch more tutorials.
4. Some common licenses available in GitHub. This project has an MIT Lisence.

# Contact
If you wish to contact me, please direct message me in LinkedIn ([in/johnangeloalgarne](https://www.linkedin.com/in/johnangeloalgarne/)).