# Tork

Tork is a rapid development, deployment, and process management system for use with the Tornado Web Server and Python.  It simplifies and automates many of the common tasks of creating a Tornado Web application.  Then, there is more time for the developer(s) to focus on the core features of the application and less time worrying about deployment.  As a process management system, it can also help with monitoring server instances.

## History

Tork was created in late 2009 as a result of code created for Boston.StartupWeekend.org (#swboston).  It managed our Tornado Web server instances and handled the deployment pipeline.  But it wasn't perfect or general enough to apply to other projects.  So, thus, Tork was born.  It is cleaned up, re-factored, and improved from our experience using it.

## The Gist
### Development

    $ tork init %project_name%                # completed
    $ tork start|stop|restart %app_name%      # planned
    
### Monitoring & Deployment
Tork is actually used to monitor other Tork instances.  Add you servers to the tork-monitor and Tork will periodically check server status and alert you if a server is down.  It also displays useful statistics such as number of open asynchronous connections, plots page hits per second, response time, etc.  Upon server failure, in the report, you can see the most recent stack trace that caused the error, you can reboot the instance, you can rollback to a previous revision, etc.

If you tie Tork into Git & Github, like we do, you can manage your deployments using Tork through the processes of continuous integration and continuous deployment.  If you make a commit and push to Github, tork-monitor can automatically run xUnit tests and deploy on success to a fleet of servers.  You can divide the tests among multiple slave servers as well to shorten test time.  If any tests fail, the deployment does not go through.  Or even if you don't like the current revision, you can revert to a previous state quickly and easily through tork-monitor.  

## Quick Start
### Git it on

The source code for Tork is managed via Git and is hosted on GitHub.com.  For more information on installing Git, please see the the GitHub [help documentation](http://help.github.com/).  

### Git your copy

To obtain a copy of Tork, perform the following commands:

    $ git clone git@github.com/thegoleffect/Tork.git

### WE'LL Git THERE WHEN WE Git THERE!

At the moment, there's no code... so you can neither install nor truly run Tork.  

If you're feeling adventurous though, you can check out the most recent build and simply add /FOLDER-YOU-STORE-TORK-IN/tork/bin to your PATH environment variable and /FOLDER-YOU-STORE-TORK-IN/ to your PYTHONPATH environment variable.  This will allow you to call "$tork init project_name".  After that, you need to add your project name's directory to the pythonpath variable.  

For the time being, I will not give any support for Tork until its officially released.

## License

Tork is released under the MIT License. See the LICENSE file for details.