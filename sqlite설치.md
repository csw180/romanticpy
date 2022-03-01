## Ubuntu 에 최선버젼의  SQlite 를 설치하는 방법                 
wget https://www.sqlite.org/2022/sqlite-autoconf-3380000.tar.gz             
tar xvfz sqlite-autoconf-3380000.tar.gz                   
sudo mv sqlite-autoconf-3380000 /opt/sqlite3                 
cd /opt/sqlite3                  
./configure --prefix=/usr             
make -j 2               
sudo make install           
sqlite3 --version            
