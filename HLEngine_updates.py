import git
def update(param):
    try:
        # git.Git("Updates/").clone("https://github.com/HLRobotics/QBee.git")
        # print("done downloading .....")
        git_dir = "../../QBee"
        g = git.cmd.Git(git_dir)
        g.pull()
        print("HLEngine:done updating ......")
    except:
        return("HLEngine:cannot connect to cloud")
