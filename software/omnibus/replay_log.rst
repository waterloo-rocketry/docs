Replay Log
==========

There is a sink called "Global Log" which we use to log data to `.log` files. Replay log is used to replay these logs for debugging purposes.

This is an explanation of all the arguments

* replay_speed
    * the replay log source attempts to send messages at the same time they were originally logged, relative to the first message. You can set this option
      to make the log replay at a different speed. This can be any floating point value greater than 0.
* log_file
    * the log file that you want to replay. This argument is optional. If you don't specifiy it, you will be prompted with a few candidate files and you may
      select from among them. It search the entirity of the omnibus repository for candidate files and displays some number of them.
* max_logs
    * This specifies the number of candidates printed in the prompt described above.


