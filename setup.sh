# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# install requirements
./env/Scripts/pip install -e .

# run migrate
# ./env/Scripts/alembic upgrade head

# setup rest server
python3 -m venv ./rest/env

# activate env in windows
./rest/env/Scripts/activate.bat

# install requirements
./rest/env/Scripts/pip install -e ./rest

# setup grpc server
cd grpc_server

# create env member
python3 -m venv ./member/env

# activate env in windows
./member/env/Scripts/activate.bat

# install requirements
./member/env/Scripts/pip install -e ./member

# create env notif
python3 -m venv ./notif/env

# activate env in windows
./notif/env/Scripts/activate.bat

# install requirements
./notif/env/Scripts/pip install -e ./notif

# create env project
python3 -m venv ./project/env

# activate env in windows
./project/env/Scripts/activate.bat

# install requirements
./project/env/Scripts/pip install -e ./project

# create env task
python3 -m venv ./task/env

# activate env in windows
./task/env/Scripts/activate.bat

# install requirements
./task/env/Scripts/pip install -e ./task

# create env user
python3 -m venv ./user/env

# activate env in windows
./user/env/Scripts/activate.bat

# install requirements
./user/env/Scripts/pip install -e ./user




