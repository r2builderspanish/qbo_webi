import cherrypy
from mako.template import Template
from tabsClass import TabClass
import rospy
import subprocess
from subprocess import Popen, PIPE, STDOUT
import signal
import shlex

class LaunchersTabManager(TabClass):

    def __init__(self,language):
          self.language = language
          self.htmlTemplate = Template(filename='launchersTab/templates/launchersTabTemplate.html')


    @cherrypy.expose
    def index(self):
        return self.htmlTemplate.render(language=self.language)

    @cherrypy.expose
    def phonelauncher(self):
        try:
            cmd = "rosrun qbo_mjpeg_server mjpeg_server"
            self.mjpegNode = subprocess.Popen(cmd.split())
            cmd = "rosrun qbo_http_api_login qbo_http_api_login.py"
            self.httpapiNode = subprocess.Popen(cmd.split())
        except:
            return "false"            
        return "true"	

    @cherrypy.expose
    def musicplayer(self):
        try:    
            cmd = "roslaunch qbo_music_player hand_gesture_node.launch"
            self.musicNode = subprocess.Popen(cmd.split())
        except:
            return "false"
        return "true"

    @cherrypy.expose
    def randommove(self):
        try:
            cmd = "roslaunch qbo_random_move random_move_face_demo.launch"
            self.randommoveNode = subprocess.Popen(cmd.split())
        except:
            return "false"
        return "true"

    @cherrypy.expose
    def facetraking(self):
        try:
            cmd = "roslaunch qbo_webi qbo_face_recognition_training.launch"
            self.faceNode = subprocess.Popen(cmd.split())
        except:
            return "false"
        return "true"

    @cherrypy.expose
    def stopFacetraking(self):
        try:
            rospy.loginfo("Qbo Webi: Killing Face Recognizer nodes")
            self.faceNode.send_signal(signal.SIGINT)
        except Exception as e:
            rospy.loginfo("ERROR when trying to kill Face Recognizer Process"+e)
        return "true"


    @cherrypy.expose
    def stopPhonelauncher(self):
        try:
            rospy.loginfo("Qbo Webi: Killing Face Recognizer nodes")
            self.mjpegNode.send_signal(signal.SIGINT)
            self.httpapiNode.send_signal(signal.SIGINT)
        except Exception as e:
            rospy.loginfo("ERROR when trying to kill Face Recognizer Process"+e)
        return "true"

    @cherrypy.expose
    def stopMusicplayer(self):
        try:
            rospy.loginfo("Qbo Webi: Killing Face Recognizer nodes")
            self.musicNode.send_signal(signal.SIGINT)
        except Exception as e:
            rospy.loginfo("ERROR when trying to kill Face Recognizer Process"+e)
        return "true"

    @cherrypy.expose
    def stopRandommove(self):
        try:
            rospy.loginfo("Qbo Webi: Killing Face Recognizer nodes")
            self.randommoveNode.send_signal(signal.SIGINT)
        except Exception as e:
            rospy.loginfo("ERROR when trying to kill Face Recognizer Process"+e)
        return "true"

