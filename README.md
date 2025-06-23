::include{file=.gitlab/badges.md}
# ![](https://gitlab.com/pl.rachuna-net/infrastructure/terraform/modules/gitlab-project/-/raw/main/images/ansible.png){height=20px} Konfiguracja serwera SSH

Ansible role to configure SSH

::include{file=docs/main.md}
::include{file=.gitlab/contributions.md}
::include{file=.gitlab/license.md}
::include{file=.gitlab/authors.md}

docker run --rm -it --name ansible-dev -u root -v /repo:/repo -v /etc/ssl/certs:/etc/ssl/certs -v ~/.profile:/root/.profile -e WORKSPACE=$PWD -e DOCKER_IMAGE=registry.gitlab.com/pl.rachuna-net/containers/ansible:1.0.1 -w $PWD registry.gitlab.com/pl.rachuna-net/containers/ansible:1.0.1 bash