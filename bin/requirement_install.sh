pip install jieba==0.38 --user
pip install prettytable

# pip install python-Levenshtein --user
# pip install tgrocery --user

# more information --> https://www.jianshu.com/p/96c01666aeeb
apt install enchant --user
pip install pyenchant --user


# install mytgrocery
tar -xf MyGrocery.install
cd TextGrocery/
python setup.py install --user
cd ../
rm -rf TextGrocery/

# 配置文件
pip install configparser --user

# the main package of the server
pip install gunicorn
pip install flask --user
pip install flask_cors --user
pip install flask_restplus --user

# the status of cpu, memery and network
pip install psutil --user

# 简体繁体转换
git clone https://github.com/zhanfengchen/Trad_Simp.git
cd Trad_Simp/
python setup.py install --user
cd ..
rm -f -r Trad_Simp/
mkdir log

# 安装crfsuite
wget https://github.com/downloads/chokkan/liblbfgs/liblbfgs-1.10.tar.gz
tar -xf liblbfgs-1.10.tar.gz
cd liblbfgs-1.10/
./configure --prefix=$HOME/local
make
make install
cd ..
rm -rf liblbfgs-1.10/
rm liblbfgs-1.10.tar.gz

wget https://github.com/downloads/chokkan/crfsuite/crfsuite-0.12.tar.gz
tar -xf crfsuite-0.12.tar.gz
cd crfsuite-0.12/
./configure --prefix=$HOME/local --with-liblbfgs=$HOME/local
make
make install
cd swig/python/
./prepare.sh
python setup.py build_ext --include-dir=$HOME/local/include --library-dirs=$HOME/local/lib -R $HOME/local/lib
python setup.py install --user
cd ../../../
rm -rf crfsuite-0.12/
rm crfsuite-0.12-x86_64.tar.gz
