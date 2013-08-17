import sublime, sublime_plugin
import os,sys
from subprocess import Popen

class OpenExplorerCommand(sublime_plugin.WindowCommand):

  def _path(self, path):
    if path:
      return path
    if self.window.active_view():
      return self.window.active_view().file_name()
    if self.window.folders():
      return self.window.folders()[0]
    
    return '.'

  def _windows(self, path):
    full_path = path
    Popen("explorer /select,\"%s\"" % full_path ,shell=True)

  def _cmd(self, path):
    path = os.path.dirname(path)
    drive = os.path.splitdrive(path)[0]
    cmd = ["cmd.exe","/k %s" % drive + " && cd " + path]
    Popen(cmd)

  def _comspec(self):
    cmd = [os.environ["COMSPEC"]]
    Popen(cmd)

  def run(self, *arg, **kwarg):
    if os.name == 'nt':
      path = None 
      if kwarg.has_key("path") and os.path.exists(kwarg["path"]):
        path = kwarg["path"]
      path = self._path(path).encode(sys.getfilesystemencoding())
      if kwarg.has_key("opt"):
        if kwarg["opt"] == "cmd":
            self._cmd(path)
        if kwarg["opt"] == "comspec":
            self._comspec(path)
      else:
        self._windows(path)

