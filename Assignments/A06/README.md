## Project Title : Software Tool Presentation(GitLab)
## Name : Nitish Kumar Erelli
## GitLab: Overview and Features

GitLab is a Source code management platform that provides
- open-source development platform
- version control
- continuous integration/continuous deployment (CI/CD)
- project management, and collaboration features
in a single integrated solution.

## Requirements
- GitLab
- Maven
- Visual Studio Code
- Git Bash
 
### Version Control
GitLab is built on Git, the widely-used distributed version control system. It provides a robust and scalable platform for managing your source code repositories. With GitLab, you can easily create, clone, branch, and merge repositories, making it simple to collaborate with team members and manage your codebase effectively. 

### Integrated CI/CD

- Continuous Integration (CI): The practice of frequently and automatically integrating code changes from multiple developers into a shared repository. CI aims to detect and address integration issues early by automatically building, testing, and validating code changes.

- Continuous Deployment (CD): The practice of automatically deploying code changes to production or staging environments after they have passed the necessary tests and validations. CD aims to enable rapid and frequent releases of software, ensuring that working and tested code is deployed to production as quickly as possible.

### Project Management

- GitLab includes a range of project management features, making it more than just a version control system. It provides tools for 
  issue tracking
- allowing you to create and manage tasks, bugs, and feature requests within your projects
  assign issues
- set due dates
- add labels and track progress
- streamlining collaboration and ensuring project milestones are met.

### Collaboration and Code Review

- GitLab focuses on fostering collaboration within development teams
- It provides features such as merge requests (pull requests), code review tools, and discussions
- Developers can create merge requests to propose changes, review code, leave comments, and discuss implementation details
- GitLab also supports inline commenting and versioned discussions, enabling thorough and efficient code collaboration.

## Steps to authenticate GitLab using SSH keys:

- Generate an SSH key in Windows using command line
 ```shell
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- Paste the SSH key in GitLab
- Check the authentication
```shell
 `ssh -T git@gitlab.com
```


## Terminology:

- ### Merge Request: 
  A Request to merge one branch into another. 
  It provides a space to have a conversation with the team about the changes on a branch.
It is a central place where changes to the code are reviewed and verified

- ### Issue: 
  An Issue is a way to track work related to a GitLab project.
  Issues can be used to report bugs, track tasks, request new features, and ask questions

- ### Maven:
    - Maven is a powerful build automation and project management tool used primarily for Java-based projects.
    - It provides a comprehensive and standardized way to manage dependencies, build, test, and deploy applications.
    - Maven uses a declarative XML-based configuration file called "pom.xml" (Project Object Model) to define the project structure, dependencies, and build process.

### Pipeline: 
A CI/CD pipeline is a series of automated steps or stages that code changes go through from development to deployment. 

### Jobs:
 A job is a specific task or set of tasks within a CI/CD pipeline. It represents a unit of work that is executed as part of the pipeline. 
Jobs can include tasks such as building the code, running tests, generating artifacts, deploying to environments, or performing other custom actions. 
### Runners: 
Runners are the agents or machines responsible for executing the jobs defined in the CI/CD pipeline. 
They are responsible for running the job's tasks, executing commands, and providing the necessary computing resources.
Stages: 
Stages provide logical separation and allow for better organization and control of the pipeline flow. 
Common stages in a pipeline can include 
### Build
Test
Deploy
post-deploy stages
Jobs within the same stage are often executed in parallel, while stages are executed sequentially.

## Demo Project to show CI/CD pipeline

### Steps to run the pipeline
- Authenticate the GitLab using SSH through the command line
- Create a new group from the left panel group dashboard as shown below
- Create a new project 
- Clone the repository to the local machine
- Add required configuration to .gitlab-ci.yml file
- Add the project to the directory
- Push the changes to remote repository to trigger the pipeline

## Conclusion
GitLab offers a comprehensive DevOps platform that integrates version control, CI/CD, project management, and collaboration features. Its built-in CI/CD capabilities, powered by GitLab CI/CD and its YAML-based markup language, streamline the development and deployment process. With GitLab, teams can effectively manage their code repositories, automate their build and release pipelines, and collaborate seamlessly, all within a single platform.

