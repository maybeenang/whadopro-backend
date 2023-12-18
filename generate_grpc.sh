# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc user
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/user --pyi_out=./grpc_server/user --grpc_python_out=./grpc_server/user ./grpc/user.proto

# generate grpc member
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/member --pyi_out=./grpc_server/member --grpc_python_out=./grpc_server/member ./grpc/member.proto

# generate grpc task
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/task --pyi_out=./grpc_server/task --grpc_python_out=./grpc_server/task ./grpc/task.proto

# generate grpc project
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/project --pyi_out=./grpc_server/project --grpc_python_out=./grpc_server/project ./grpc/project.proto

# generate grpc notif
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/notif --pyi_out=./grpc_server/notif --grpc_python_out=./grpc_server/notif ./grpc/notif.proto