docker run -d -p 3000:3000 --name=grafana1 ^
-v "%cd%\grafana-storage:/var/lib/grafana" ^
-v "%cd%\grafana.ini:/etc/grafana/grafana.ini" ^
grafana/grafana-oss:latest
cmd /k

