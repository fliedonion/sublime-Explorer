import sublime, sublime_plugin
import os,sys

class OpenContainsDirectoryCommand(sublime_plugin.TextCommand):

  def _windows(self):
  	from subprocess import Popen
  	path = os.path.dirname(self.view.file_name())
  	cmd = ["explorer", os.path.dirname(self.view.file_name().encode(sys.getfilesystemencoding()))]
  	Popen(cmd)


  def run(self, edit):
  	if os.name == 'nt':
  		self._windows()

