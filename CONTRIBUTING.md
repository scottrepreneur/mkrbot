# Contribute new commands to @mkr.bot

It'd be great to have additional commands for @mkr.bot. If you have suggestions open an issue and a pull request is more than welcome. [Check out the full list of commands](https://docs.google.com/spreadsheets/d/1apOxgKIeeCTUnisfSRS0TLxiXsIFFB0xvtYLoxSpYX0/edit?usp=sharing) and feel free to suggest additional or alternative commands.

## Getting the development environment set up

- dev-docker-compose.yml
- env files

## Development start

`docker-compose -f dev-docker-compose.yml up`

- POST to localhost:8000
    - need authentication token
    - JSON body includes user, channel, and message properties
