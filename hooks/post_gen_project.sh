#!/bin/bash

git init
git submodule add {{ cookiecutter.upstream_url }} upstream
git add .
git commit --message "Initialize repository for {{ cookiecutter.implementation_name }}"
