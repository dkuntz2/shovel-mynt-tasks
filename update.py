from shovel import task
from subprocess import call
#from lessc import compile

import os, glob, subprocess

@task
def update():
	'''
		Update the site, including pushing a git repo to wherever...
		
		Yeah, that's right, just update stuffs and whatever...
	'''

	# compile less
	#compile("style.less", path="./source/_assets/css")
	#call(["lessc", "source/_assets/css/style.less", ">", "source/_assets/css/style.css"])

	# add source git...
	os.chdir("source")
	call(["git", "add", "."])
	call(["git", "commit", "-m", "'update script'"])
	call(["git", "push"])

	# generate
	os.chdir("../")
	call(["mynt", "gen", "-f", "source", "generated"])

	# add gen git
	cp = subprocess.Popen("cp generated/* git/ -r", shell=True)
	result, err = cp.communicate()
	print "copying error" if err else "copying fine"

	os.chdir("git")
	call(["git", "add", "."])
	call(["git", "commit", "-m", "'update script'"])
	call(["git", "push"])

