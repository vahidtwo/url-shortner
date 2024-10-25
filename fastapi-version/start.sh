
echo $ENTRYPOINT
if [[ "$ENTRYPOINT" = "web" ]]
then
   echo "Starting web" && gunicorn --config gunicorn_config.py  url_shortener.app:fastapi_appf
else
  echo Error, cannot find entrypoint "$ENTRYPOINT" to start
fi
