# snapshotalyzer-30000

Demo project to manage AWS EC@ instance snapshots

## About

This project is a demo, and uses BOTO3 to manage AWS EC@ instance and snapshots.

## Configuring

shotty uses configutration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run "python shotty.shotty.py <command> <subcommand>
<--project=PROJECT>"`

*command* is instances, volumes, or snapshots.
*subcommand* - depends on command.
*project* is optional
