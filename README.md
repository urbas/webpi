# webpi

# Quickstart
Install docker and docker-compose (see the "Dependencies" section below) and run:
```bash
NODE_VERSION=$(cat .nvmrc) PYTHON_VERSION=$(cat .python-version) docker-compose up --build backend frontend
```
The command will spin up:

- the frontend at http://localhost:3000
- the backend REST API at http://localhost:5000

# Development tasks
See instructions for individual components on how to unit-test, format, and lint your code:

- [backend](./backend/README.md)
- [frontend](./frontend/README.md)

Recommended: open the workspace `webpi.code-workspace` in Visual Studio Code.

## Interactive integration tests
Bring up Cypress GUI so you can run integration tests interactively:
```bash
cd itests && CYPRESS_baseUrl=http://localhost:3000 npm start
```
Note that you will have to start a working webpi cluster separately (just follow the quickstart above). Frontend server has to be available at the url you specify with the `CYPRESS_*Url` environment variables.

# CI/CD
Navigate to the [CI/CD dashboard].

The CI/CD pipeline is defined in [`bitbucket-pipelines.yml`](./bitbucket-pipelines.yml).

# Dependencies

## nvm
To manage the nodejs version usesd throughout this project, you should use nvm. The currently supported nodejs/npm version is encoded in the [`.nvmrc`](./.nvmrc) file.

Please follow [nvm installation instructions].

[oh-my-zsh] also has an [nvm plugin] which you can use directly.

Run `nvm use` in the root of the repository. This should activate the node version required.

Optional: Follow the [nvm shell integration notes] or the [zsh nvm plugin notes] to make your shell automatically load the node environment when `cd`ing into the project directory.

## docker
If you're using Ubuntu, you can use [Docker installation instructions].

Follow [sudoless docker instructions] so you'll be able to manage docker without sudo.

You can verify that you've installed docker correctly with this command:
```bash
docker run hello-world
```

## docker-compose
After you've installed docker, you should also install docker-compose. We use docker-compose to set up the development environment.

Just follow [docker-compose installation instructions].


[CI/CD dashboard]: https://bitbucket.org/webpi/webpi-web/addon/pipelines/home
[Docker installation instructions]: https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
[docker-compose installation instructions]: https://docs.docker.com/compose/install/#install-compose
[nvm installation instructions]: https://github.com/creationix/nvm
[nvm plugin]: https://github.com/lukechilds/zsh-nvm
[nvm shell integration notes]: https://github.com/creationix/nvm#deeper-shell-integration
[oh-my-zsh]: https://github.com/robbyrussell/oh-my-zsh
[sudoless docker instructions]: https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user
[zsh nvm plugin notes]: https://github.com/lukechilds/zsh-nvm#auto-use