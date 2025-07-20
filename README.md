# taskcli - A Simple To Do List App

![Alt Text](https://github.com/keandrake-24/task-cli/blob/master/preview.gif)

## Description

**taskcli is a to do list CLI command tool, allowing users to write down and manage their tasks effectively. taskcli is great for simple usage.**

## Installation

**taskcli does not require installation, but commands have to be run in the directory where it was downloaded**



go into the directory where you want it to be installed e.g: `/home/user/dedicated-github-downloads-folder` on linux

* #### After going into the directory of your choice, run:

```bash
git clone https://github.com/keandrake-24/task-cli.git
```

* #### this should create a new directory task-cli, move into that directory and run the linux only file:

```bash
cd task-cli && ./taskcli
```

> **_NOTE:_**
> On windows, taskcli is run by doing `python taskcli.py` instead of `./taskcli`

## Usage

### Creating a New Task

to create a new task, run:
```bash
./taskcli add task
```
or on Windows:
```
python taskcli.py add task
```
This will create a new task with an ID.

> **_NOTE:_**
>  **In future operations with this task, input the ID instead of the task name**
> 
### Updating a Tasks Status

There are **3** possible statuses for a task:
1. Incomplete
2. Complete
3. In-progress

to set a tasks status, run:
```bash
./taskcli set-(status) task-id
```
or on Windows:
```
python taskcli.py set-(status) task-id
```
`(status)` should be replaced with one of these **3** values:
* `incomplete`
* `in-progress` 
* `complete` 

For example:
```bash
./taskcli set-in-progress 1
```

### Renaming a task

to rename a task, run:
```bash
./taskcli update task-id new-name
```
or on Windows:
```
python taskcli.py update task-id new-name
```

### Listing Tasks

To list all tasks, you can run:

```bash
./taskcli list
```
or on Windows:
```
python taskcli.py list
```

This will list all tasks, each task has these 5 attributes which will be shown:
* ID
* Description
* Status
* CreatedAt
* UpdatedAt

### Listing Specific Types of Tasks
  
To list specfic types of tasks, you can run:

```bash
./taskcli list type-of-task
```
or on Windows:
```
python taskcli.py list type-of-task
```

`type-of-task` can be of these 3 types:
* `incomplete`
* `in-progress` 
* `complete` 

