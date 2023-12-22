# Odoo Test Project
This is my test project for learning Odoo development.

Trying to learn how to develop custom modules for Odoo 16 specifically. The learning process also involves an extra step, which is to develop with [Docker containers](https://www.docker.com/resources/what-container/) instead of publishing with it. Additionally, Dev Containers, an extension for VS Code, is also used to make development within the container easier.

This repository includes the [project setup](#Setup "Go to Setup"), [recommended worflow](#Workflow "Go to Workflow"), and also [what I've learned](#Learnings). *This repository is also mostly just a massive "note to myself". Goodluck and goodjob, me.*

**NOTE: Do not use the containers for production. The environment variables are not yet hidden, and this is solely for development purposes only. The actual Odoo 16 server is setup in an Ubuntu virtual environment, with Odoo and Postgres installed and proper configurations.**

# Files
1. `.devcontainer` folder contains settings for VS Code Dev Container extension.
2. `extra-addons` folder contains the actual modules.
3. `py_requirements.txt` are all the additional python packages.

# Setup
To setup the odoo server inside a docker container, make sure that you have the requirements installed first. Then, follow the steps below to start the development process. Note that this project has not been tested for Linux and Mac environments yet, only on Windows.

## Requirements
1. Docker desktop ([installation guide](https://docs.docker.com/desktop/install/windows-install/ "How to install?"))
2. [VS Code](https://code.visualstudio.com/ "What's VS Code? How to install?") and Dev Containers (if you have docker installed, VS Code will automatically detect that you may need Dev Containers and other Docker-related extensions.)

## Steps to start
1. Pull the git repository locally and open using VS Code ("odoo-test-project" is the current workspace).
2. Once the project is opened, enter in the terminal `docker compose up -d`.
3. Click the double bracket icon at the bottom left then select "*Reopen in Container*", or open the command palette (`Ctrl + Shift + P`), type "*reopen*", and you should be able to select the same thing. Once this is done, in docker desktop, you should be able to see "odoo-test-project" (a docker compose) together with "odoo-db" (postgres15 image) and "odoo-web" (custom odoo16 image).
3. You should now be able to see the same files in the directory ("mnt" is the current workspace). Start coding inside the `extra-addons` directory. **Note** that at this point, you are working inside an Ubuntu environment since that is the default OS for odoo.

## Important notes
1. The `Dockerfile` file specifies that `sudo` is to be installed inside the container. This is to enable restarting the server directly inside the container.
2. The `compose.yaml` file specifies that the `extra-addons` folder is to be mounted in `/mnt/extra-addons` folder. This is because the `odoo:16` docker container initially requires custom addons to be put inside this folder [see dockerhub documentation](https://hub.docker.com/_/odoo "DockerHub documentation for Odoo"). This can be modified, but be mindful of the `odoo.conf` file which should have the addons path.
3. Just to be safe, always push changes to a different branch other than `main`, and just pull it afterwards. This is because all the files are sometimes recommitted (idk why) when you commit inside the container.

# Workflow
Once the setup is done, you should now be able to work on the code. Some good rule of thumbs are the following.
1. Always `git pull` first before changing anything. You can also do this inside the dev container once the [setup](#Setup "Go to Setup") is done.
2. Edit on the `extra-addons` folder. Although editing on `modules` folder is also possible, the odoo server fetches files from `extra-addons` first. And so, this is just to remove the delay on file syncing (synced through mounting in docker).
3. To push changes, just simply use the usual git commands `add`, `commit`, and `push`. *Note* that you should be working in a different branch other than `main`, say,`devcontainer`.

# Learnings
This section will be updated every once in a while.

## General
- Docker: `pull`, `build`, `run`, `compose`.
- General workflow on developing inside a docker container (I don't want to install locally).
- General idea of developing odoo modules. Still need to watch more tutorials.
- Some common licenses available in GitHub. This project has an MIT Lisence.
- 

## Odoo
- Add `?debug=1` in the address bar (i.e. `localhost:8069?debug=1`) to enable debug mode for updating module lists.
- Always needs at least 1 module enabled in order to see General Settings.

### To create new modules:
1. Create new folder (and add its parent directory on the addons path)
2. Create new folders: `controllers`, `security`, `views`, `models` (others: `data`, `static`, `wizard`)
3. Add `__init__.py` to initialize the folders, except data folders (security and views)
```
# <module>/__init__.py
from . import modules
from . import controllers
# etc.
```
4. Add `__manifest__.py` as module metadata
```
# <module>/__manifest__.py
{
    'name': '',
    'category': 'Application',
    'summary': '',
    'version': '1.0',
    'description': """ """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/*.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
```
5. In `security` folder, make `ir.model.access.csv` with users that can access
``` 
# <module>/security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_world_clock,access.world.clock,model_<model_name>,base.users [or others],1,1,1,1
```
6. In `views` folder, mininum 2 files are expected: `menu_views.xml` and `model_views.xml`
7. In `models` folder, make your models per python file `<model_name>.py`, and make `__init__.py`
``` 
# <module>/models/__init__.py
from . import <model_name>
etc.
```

# Contact
If you wish to contact me, please direct message me in LinkedIn ([in/johnangeloalgarne](https://www.linkedin.com/in/johnangeloalgarne/)).