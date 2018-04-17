git clone -b '1.1.3' https://github.com/scrapy/scrapy.git packages/scrapy
git clone -b 'twisted-16.4.1' https://github.com/twisted/twisted.git packages/twisted

pyenv uninstall gather
pyenv virtualenv 2.7.14 gather
pyenv local gather

pip install -e packages/twisted
pip install -e packages/scrapy
pip install -r requirements.txt
