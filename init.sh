git clone --depth=1 -b '1.1.3' --single-branch https://github.com/scrapy/scrapy.git packages/scrapy
git clone --depth=1 -b 'twisted-16.4.1' --single-branch https://github.com/twisted/twisted.git packages/twisted
git clone --depth=1 -b 'master' --single-branch https://github.com/rmax/scrapy-inline-requests packages/scrapy-inline-requests

pyenv uninstall gather
pyenv virtualenv 2.7.14 gather
pyenv local gather

pip install -e packages/twisted
pip install -e packages/scrapy
pip install -e packages/scrapy-inline-requests
pip install -r requirements.txt
