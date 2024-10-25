
echo $ENTRYPOINT
if [[ "$ENTRYPOINT" = "web" ]]
then
   echo "Starting web" && gunicorn --config gunicorn_config.py  app.main:app
else
  echo Error, cannot find entrypoint "$ENTRYPOINT" to start
fi
