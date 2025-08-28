#!/bin/sh
cd ..

export TTOFF_LOGIN_TOKEN=dev

/usr/bin/python3 -m toontown.launcher.TTOffQuickStartLauncher
