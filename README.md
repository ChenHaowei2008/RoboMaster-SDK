# RoboMaster-SDK but it actually works

This has only been successfuly installed on Ubuntu 18.04! Try at ur own risk.

If u successfully install it on Arch Linux, please do tell me how you did it.

To install, this, you have to first install the libraries in lib. 

Then, you can just `pip install .` or something I forgot.

The current vesion is very patchy and I will try to improve it in the future. At least it works.

The main things that I fixed were:

1. Skips trying to broadcast if the ip address detected is 127.0.0.1. (This prevents "broadcast" key not found error)
2. Allows you to manually pass in a sn_and_ip dictionary, so that the code doesn't have to scan for the drones everytime you run it, and it prevents the issue of the drone returning "ok?" when asking for the serial number of the drone. This prevents the error of "{SN} does not exits!" error, even though your drone is connected to the wifi.

The reason the second bug exists is because the code originaly code is ass, and the drone occasionally returns "ok" instead of the serial number when asking for the serial number :skull:
