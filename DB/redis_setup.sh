#!bash
DB_PW=dev
DB_DATA_PATH=/home/data
DB_PROT=6379

apt update
apt install docker python3 python3-pip
python3 -m pip install redis

docker pull redis
docker run -p ${DB_PROT}:6379 --name redis_test -v ${DB_DATA_PATH}:/data -d redis redis-server --appendonly yes --requirepass ${DB_PW}
#docker run -it --link redis_test:redis --rm redis redis-cli -h redis -p 6379 -a "dev"