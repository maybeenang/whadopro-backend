# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc member
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest_api/rest_api/grpc_client/member --pyi_out=./rest_api/rest_api/grpc_client/member --grpc_python_out=./rest_api/rest_api/grpc_client/member ./grpc/member.proto

# generate grpc notif
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest_api/rest_api/grpc_client/notif --pyi_out=./rest_api/rest_api/grpc_client/notif --grpc_python_out=./rest_api/rest_api/grpc_client/notif ./grpc/notif.proto

# generate grpc project
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest_api/rest_api/grpc_client/project --pyi_out=./rest_api/rest_api/grpc_client/project --grpc_python_out=./rest_api/rest_api/grpc_client/project ./grpc/project.proto

# generate grpc task
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest_api/rest_api/grpc_client/task --pyi_out=./rest_api/rest_api/grpc_client/task --grpc_python_out=./rest_api/rest_api/grpc_client/task ./grpc/task.proto

# generate grpc user
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest_api/rest_api/grpc_client/user --pyi_out=./rest_api/rest_api/grpc_client/user --grpc_python_out=./rest_api/rest_api/grpc_client/user ./grpc/user.proto