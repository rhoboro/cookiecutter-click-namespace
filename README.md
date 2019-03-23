# cookiecutter-click-namespace

cookiecutter-click-namespace is a template for pluginable cli command based on [Click](https://palletsprojects.com/p/click/).  
Commands created with this template can add subcommands using `pip`.

This repository is a main package template and plugin package template is [here](https://github.com/rhoboro/cookiecutter-click-namespace-plugin).

## How to use

This tutorial create two packages `flowers` and `flowers-tulip`.  
The `flowers` is also namespace command like `aws` command or `gcloud` command.
The `flowers-tulip` package is for `tulip` subcommand like `aws ec2` command or `gcloud compute`.
You can also add other commands such as `rose` or `dandelion` by developing a plugin.

### Installing a namespace command

```shell
# Install cookiecutter
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install cookiecutter

# Create a main package for namespace command
(venv) $ cookiecutter https://github.com/rhoboro/cookiecutter-click-namespace
namespace [maincommand]: flowers
author [yourname]: rhoboro
author_email [yourname@domain]: rhoboro@example.com
(venv) $ ls
flowers venv

# And install
(venv) $ pip install flowers/  # Don't forget the trailing slash
Processing ./flowers
Requirement already satisfied: click in ./venv/lib/python3.7/site-packages (from flowers==1.0.0) (7.0)
Installing collected packages: flowers
  Running setup.py install for flowers ... done
Successfully installed flowers-1.0.0

# The namespace command has been installed
(venv) $ flowers
Usage: flowers [OPTIONS] COMMAND [ARGS]...

  Namespace for extra commands

Options:
  -v, --verbose [NONE|DEBUG|INFO|WARNING|ERROR]
                                  to set log level  [default: NONE]
  -h, --help                      Show this message and exit.
```

### Install extra command

```shell
# Create a extra package for subcommand
(venv) $ cookiecutter https://github.com/rhoboro/cookiecutter-click-namespace-plugin
namespace [maincommand]: flowers  # Same as above
plugin [subcommand]: tulip  # Extra command name
author [yourname]: rhoboro
author_email [yourname@domain]: rhoboro@example.com
(venv) $ ls
flowers       flowers.tulip venv

# And install
(venv) $ pip install flowers.tulip/  # Don't forget the trailing slash
Processing ./flowers.tulip
Requirement already satisfied: click in ./venv/lib/python3.7/site-packages (from flowers-tulip==1.0.0) (7.0)
Installing collected packages: flowers-tulip
  Running setup.py install for flowers-tulip ... done
Successfully installed flowers-tulip-1.0.0

# Finally, subcommand has been installed
(venv) $ flowers tulip
Usage: flowers tulip [OPTIONS] COMMAND [ARGS]...

  Command Group

Options:
  -h, --help  Show this message and exit.

Commands:
  sample  Sample command
(venv) $ flowers tulip sample
tulip's sample was called
```
