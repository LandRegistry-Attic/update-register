source /tmp/.venv/update-register/bin/activate

export SETTINGS="config.DevelopmentConfig"

cd /vagrant/apps/update-register

python manage.py db upgrade
