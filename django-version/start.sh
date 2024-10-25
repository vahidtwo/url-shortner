
echo $ENTRYPOINT
if [[ "$ENTRYPOINT" = "web" ]]
then
  python manage.py collectstatic --noinput && \
   echo "Starting web" && gunicorn --config gunicorn_config.py  settings.wsgi:application
elif [[ "$ENTRYPOINT" = "migration" ]]
then
  echo "Starting migration"
  python manage.py migrate
else
  echo Error, cannot find entrypoint "$ENTRYPOINT" to start
fi
