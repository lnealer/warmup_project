## warmup_project

### Drive Square
![alt text](https://github.com/lnealer/warmup_project/blob/main/drive_square.gif)

The drive_square behavior works by setting the bot's linear velocity for a fixed amount of time and then turning 90 degrees four times.

The bulk of my code is contained in the square class' run attribute. It works in a loop which repeats 4 times. Linear.x is set to 0.2 for 5 seconds. Then the bot stops and angular velocity is set to pi/2 for 1 second. 

I also wrote one helper function "wait_t_secs". It retrieves an initial time from rospy, and then runs in a loop until, checking the current time each iteration, until the given amount of time has passed. I used this function to let the bot run at certain speeds for certain amounts of time.



### Wall Follower
![alt text](https://github.com/lnealer/warmup_project/blob/main/wall_follower.gif)

The wall_follower behavior receives information about the distance to the wall in front and to the right of the bot. Based on these distances, the bot will turn 90 degrees or drive straight, using proportion control to make small adjustments to stay approximately 0.5 meters from the wall as it drives counter clockwise.

First, I set two variables, forward_dist and right_dist to the distances at 90 and 270 degrees from the scan topic.

The first if statement of the process_scan function tells the bot to set its speed to -0.3 to back up if its forward distance is less than 0.2. This was mostly useful while I was debugging so that the bot could right itself if he got stuck somewhere, but I decided to leave it in because I think it's a helpful functionality (even though in this simulation the bot should never be able to run into a wall).

Next, the bot checks if the forward distance to the wall is less than 0.9. If it is, the angular velocity is set to 90 degrees and the bot turns. Since its linear.x velocity is always o.4, this distance places the bot about 0.5 meters from the wall after the turn, so less adjustment is necessary.

Finally, if the bot is a greater distance from the wall, it uses proportion control to adjust its right_dist. K=0.1 and error = 0.5 - right_dist.


In future work I might make the robots velocity variable. This would require adjusting the distance at which the bot makes its turn so it can stay within the desired distance from the wall without too much adjustment needed. It also might warrant changing the k value so the movement will still look smooth.

Additionally, when the bot is first finding the wall its angular velocity is quite large due to the distance, this causes it to spin for a second until its close enough to the wall. I don't think this behavior is too problematic, but it could be corrected by having the bot check if its in the middle of a room based on its forward and right distances. 

### Person Follower
![alt text](https://github.com/lnealer/warmup_project/blob/main/person_follower.gif)
Person follower works by finding the item closest to it, and then rotating and moving forwards until it's 0.5 meters away.

First, I iterate through the distances from scan 360 degrees around the bot, and find the minimum. I save this angle and distance and use proportion control on both. For the angle, k is 2.3 and the error is the difference with 0. For distance, k is 0.55 and the error the difference with 0.5. Before this I subtract 360 from the angle if its greater than 180 and convert to radians to make it a usable value in angular.z.

In the future, I would be interested in improving this behavior figuring out how to distinguish between a wall and a figure. Currently, if the bot was placed in an enclosed room, it would mistake the walls for a figure and stick to them. 

One of the main challenges I faced was learning how subscribing to a topic works. To execute a right turn, I initially used a similar technique to that in drive_square, where I set the angular velocity for a certain amount of time. For unknown reasons at the time this caused the bot to act really erratically. Eventually I realized that process_scan() is running  every time something is published to the scan function, which is approximately every second. This meant that if I waited even 2 seconds of real time to make a turn, process_scan() will still run, but with the now incorrect scan data from a few seconds ago. Instead, I set angular velocity to 90 degrees, and let the next run of process_scan interrupt the turn in 1 second. 

#### Takeaways
I have the following takeaways for all three of these projects:
* Most values of k (within reason) will work.
  * While testing out various values of k, I found that most worked for making the bot do what I wanted eventually. I chose the values I did mostly because they give a visually smooth result. For example, a large value of k in person_follower makes the bot drift a lot more due to the greater acceleration. A larger value means that you can also see the bot oscillating back and forth as it tries to correct its angle relative to the person. A smaller value in wall_follower meant that the bot took longer to correct itself, and might spend more time away from the ideal distance. 
* When subscribing to a topic, keep in mind that your subscriber function will run in real time every time the topic is published to.
  * I discussed this a above already, but if you're going to try to do something every t fixed amount of time after publishing, keep in mind how often that topic is published to. 

