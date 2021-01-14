## warmup_project

![alt text](https://github.com/lnealer/warmup_project/blob/main/drive_square.gif)

### Overview
The drive_square behavior works by setting the bot's linear velocity for a fixed amount of time and then turning 90 degrees four times.

### Code structure
The bulk of my code is contained in the square class' run attribute. It works in a loop which repeats 4 times. Linear.x is set to 0.2 for 5 seconds. Then the bot stops and angular velocity is set to pi/2 for 1 second. 

In addition, I wrote one helper function "wait_t_secs". It retrieves an initial time from rospy, and then runs in a loop until the given amount of time has passed. I used this function to let the bot run at certain speeds for certain amounts of time.



