# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import signal

class Process(object):

    def __init__(self, pid):
        self.proc = '/proc/%d' % pid
        f = open(os.path.join(self.proc, 'stat'))
        pid, command, state, parent_pid = f.read().strip().split()[:4]
        f.close()
        command = command[1:-1]
        self.pid = int(pid)
        self.command = command
        self.state = state
        try:
            self.parent_pid = int(parent_pid)
        except:
            self.parent_pid = int(0)

        self.parent = None
        self.children = []

    def kill(self, sig = signal.SIGTERM):
        os.kill(self.pid, sig)

    def __repr__(self):
        return '%r' % self.pid

    def getcwd(self):
        try:
            return os.readlink(os.path.join(self.proc, 'cwd'))
        except OSError:
            return None


class ProcessList(object):

    def __init__(self):
        self.by_pid = {}
        self.by_command = {}
        for f in os.listdir('/proc'):
            try:
                if f.isdigit():
                    process = Process(int(f))
                    self.by_pid[process.pid] = process
                    self.by_command.setdefault(process.command, []).append(process)
            except IOError:
                pass

        for process in self.by_pid.values():
            try:
                parent = self.by_pid[process.parent_pid]
                parent.children.append(process)
                process.parent = parent
            except KeyError:
                pass

    def named(self, name):
        return self.by_command.get(name, [])
