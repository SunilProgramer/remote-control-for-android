# Copyright 2010 Christian Zommerfelds
# 
# This file is part of RemoteControl for Android.
# 
# RemoteControl for Android is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# RemoteControl for Android is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with RemoteControl for Android.
# If not, see <http://www.gnu.org/licenses/>.import RemoteControlServer as rcs

import subprocess

def play():
    subprocess.call(['rhythmbox-client','--play'])
def pause():
    subprocess.call(['rhythmbox-client','--pause'])
def next():
    subprocess.call(['rhythmbox-client','--next'])
def previous():
    subprocess.call(['rhythmbox-client','--previous'])
def show():
    subprocess.call(['rhythmbox-client','--notify'])    

butDef = rcs.ButtonDefinition()
butDef.addButton("Play",play)
butDef.addButton("Pause",pause)
butDef.addButton("Next",next)
butDef.addButton("Previous",previous)
butDef.addButton("Show track",show)

server = rcs.Server(butDef)
server.run()
