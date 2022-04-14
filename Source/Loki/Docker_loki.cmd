docker run -d --name=loki1 ^
-v "%cd%\loki:/etc/loki" ^
-p 3100:3100 grafana/loki:latest
cmd /k