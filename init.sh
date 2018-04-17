git clone -b '1.1.3' https://github.com/scrapy/scrapy.git
pyenv virtualenv 2.7.14 gather
pyenv local gather
pip install -e scrapy
