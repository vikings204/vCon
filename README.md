# vCon
keyboard-controlled virtual xbox 360 controller, designed to for RDP use

check releases for a windows executable, just remember to install [ViGEmBus](https://github.com/ViGEm/ViGEmBus/releases) first

### as of v1.1.0, the EXE requires admin privilege to receive global input

# compilation
if you don't trust my release exe...

1. download zip
2. install python3+
3. do not install ViGEmBus, it will be prompted later
4. `pip` OR `pip3` `-r requirements.txt`
5. `pip` OR `pip3` `install pyinstaller`
6. if the ViGEmBus prompt did not appear, install from above
7. run the compilation command found [here](https://github.com/vikings204/vCon/blob/master/.idea/runConfigurations/Build.xml)
