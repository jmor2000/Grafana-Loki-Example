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
 
 # Grafana-Dashboard
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
 
    Grafana
    1. Download folder "Source"
    2. Run Source\Grafana "Docker_grafana.cmd"
    3. Upon successful installation of grafana in docker, open up web-browser: http://localhost:3000
    4. login to grafana, navigate to loki2 dashboard http://localhost:3000/d/1ODPrIU7z/loki2?orgId=1&refresh=1m
    Note: Grafana can be pre-configured via grafanan.ini
    
    Loki
    5. Run Source\Loki "Docker_loki.cmd"
    6. Check for  successful installation of loki in docker
    Note: Loki can be pre-configured via Source\loki\local-config.yaml
    
    Promtail
    7. Update Source\Grafana-Promtail\config.yaml with your new file paths
           filename: C:\Users\JEF\Documents\GitHub\Grafana-Loki-Example\Source\Grafana-Promtail\positions.yaml # This location needs to be writeable by Promtail.
           __path__: C:\Users\JEF\Documents\GitHub\Grafana-Loki-Example\Source\Python Logger\app1.log       
    8. Run Source\Grafana-Promtail "Launch_promtail.cmd"
    9. Wait for promtail to load config and confirm successful operation.
    Note: Lanuched Promtail config can be checked at http://localhost:9080/targets
    Note: Promtail can be pre-configured via Source\Grafana-Promtail\config.yaml
    
    Python
    10. Run Source\Python Logger "Launch_Python.cmd"
    11. Got to Grafana loki2 dashboard and refresh to see data
    
# Useful Links

  Grafana-Loki
  - https://grafana.com/docs/loki/latest/getting-started/?pg=oss-loki&plcmt=resources
  - https://grafana.com/docs/loki/latest/logql/
    
  Log File data extraction, with regex:
  - https://regex101.com/
  - https://github.com/google/re2/wiki/Syntax#ascii
  - https://grafana.com/docs/loki/latest/clients/promtail/stages/regex/
