# Grafana-Loki-Example
This is an example of how to use Grafana-Loki to monitor log files, and present the data in grafana.

# Technologies used:
- Docker*
- *Loki
- *Grafana
- Python (logging script)
- Grafana-Promtail
- Google Chrome
- windows 10 64bit OS
- Command line scripts (.cmd) launchs all programs

# Functional Flow:
1. Pyton script executes and logs data to a log file
    -Log entries: Starting Process, Process Started, Alive, Exiting.
    -Alive is written every 1 second.
2. Grafana-Promtail is configured to:
   -Monitor the log file being added to by the python script
   -Seperate key data points: "info" "content"
   -Re2 expression used to do this "(?P<time>\\S+ *\\S+) - (?P<type>\\S+) - (?P<info>\\S+) - (?P<content>.*)"
   -Send data to Loki
3. Loki recieves the data, stores it, and makes it available on request.
4. Grafana connects to Loki and queries its data to create specific metrics.
   In this example, grafana is counting how many times a certain log line is stored, e.g Alive, Starting, Stopped, etc.
   Data is displayed in single counters or on an x y graph.
5. Users can view the data via a browser

![alt text](https://github.com/jmor2000/Grafana-Loki-Example/blob/e9cd2ac48ef775422565cc9438779f083160ca8d/Images/Overview.JPG?raw=true)


# Grafana Displays
    
Single Counts:
count_over_time({info="INFO",job="app1"}|="Alive"[60m])
count_over_time({info="INFO",job="app1"}|="Exiting"[60m])
count_over_time({info="INFO",job="app1"}|="Started"[60m])
count_over_time({info="INFO",job="app1"}|="Starting"[60m])

Graph X Y:
count_over_time({job="app1"}[$__interval])

Log List:
{job="app1"} != "Alive"

![alt text](https://github.com/jmor2000/Grafana-Loki-Example/blob/24ab8aef5b7ceb6c0dc24fc234e8331582a6af8d/Images/Dashboard.JPG?raw=true)
    
 # Installation Steps
    a.
    b.
    c.
    
    to be continued [14_April_2022]
    
