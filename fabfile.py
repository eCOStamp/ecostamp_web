from fabric.api import local, cd
from time import sleep

WORKING_DIRECTORY = "/root/ecostamp/ecostamp_web"
INI_FILE = ""
PID_FILE = "/tmp/ecostamp.pid"

def start():
	with cd(WORKING_DIRECTORY):
		local("uwsgi --ini uwsgi.ini")

def stop():
	with cd(WORKING_DIRECTORY):
		local("uwsgi --stop %s" % PID_FILE)

def restart():
	stop()
	sleep(1)
	start()

def status():
	with cd(WORKING_DIRECTORY):
		local("cat %s" % PID_FILE)

