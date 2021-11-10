from textwrap import dedent


def main():
    display_actions_message()


def display_actions_message():

    vars = dict(separator="=" * 79)
    msg = dedent(
        """
        %(separator)s
        This is a scaffolding of a Ushauri plugin. You can use it
        to create complex plugins.
        %(separator)s

        To make Ushauri to run this plugin do:
            
        Activate the Ushauri environment .
            . /path/to/ushauri/bin/activate
            
        Change directory into your newly created plugin.
            cd {{ cookiecutter.plugin_name }}

        Build the plugin
            python setup.py develop

        Add the plugin to the Ushauri list of plugins by editing the line
            #ushauri.plugins = examplePlugin
            ushauri.plugins = {{ cookiecutter.plugin_name }}
        

        Run Ushauri again
        """
        % vars
    )
    print(msg)


if __name__ == "__main__":
    main()
