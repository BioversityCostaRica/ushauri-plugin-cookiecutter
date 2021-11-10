# Ushauri Plugins Template

A Cookiecutter (project template) for creating Ushauri plugins.

Requirements
------------

* Python 3.6
* [Ushauri](https://github.com/BioversityCostaRica/ushauri-plugin-cookiecutter)
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Usage
-----

1. Generate a Ushauri plugin project, following the prompts from the command
    ```sh
    $ cookiecutter https://github.com/BioversityCostaRica/ushauri-plugin-cookiecutter
    ```
2. Finish configuring the plugin by creating a virtual environment and installing your new project. 
    ```sh
    $ . ./formshare_virtual_env/bin/activate
    $ cd myUshauriPlugin
    $ python setup.py develop
    ```
3. Add the plugin to the Ushauri list of plugins by editing the following line in development.ini or production.ini
    ```
        #ushauri.plugins = examplePlugin
        ushauri.plugins = myformshareplugin
    ```
4. Run Ushauri
