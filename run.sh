un=$1
pw=$2
if [ $3 = "qa" ];
then
  virtualenv -p /usr/bin/python3.7 venv
  source venv/bin/activate
  pip install -r requirements.txt
  pytest -s -v --html=report.html --capture=tee-sys --username=${un} --password=${pw}
fi