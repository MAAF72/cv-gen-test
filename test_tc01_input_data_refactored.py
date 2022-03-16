import time
import os
import pytest
from BrowserExtend import BrowserExtend
from dotenv import load_dotenv

def test_tc01_input_data():
    PHOTO_PATH = os.path.join(os.getcwd(), 'resources', 'photo.png')

    myBrowser = BrowserExtend()

    # Get page
    myBrowser.get("http://cv-gen-dipl.herokuapp.com:80")

    assert myBrowser.title == "Landing page", "wrong landing page"

    myBrowser.click('#create-cv')

    assert myBrowser.title == "Input Data", "wrong input data page"

    myBrowser.fill('#form-customer #photo', PHOTO_PATH)

    with pytest.raises(Exception, match="no such alert"):
        myBrowser.switch_to.alert

    myBrowser.fill('#form-customer #nama', 'John Doe')
    myBrowser.fill('#form-customer #email', 'john.doe@github.com')
    myBrowser.fill('#form-customer #no_hp', '085335831111')
    myBrowser.fill('#form-customer #portfolio', 'john-doe.github.io')
    myBrowser.fill('#form-customer #job', 'Quality Assurance')
    myBrowser.fill('#form-customer #deskripsi', 'Tester')

    myBrowser.click('#form-socialmedia .content-socialmedia:last-child #delete-socialmedia')

    myBrowser.click('#form-edukasi .content-edukasi:last-child #delete-edukasi')

    myBrowser.click('#form-penghargaan .content-penghargaan:last-child #delete-penghargaan')

    myBrowser.click('#form-pengalaman .content-pengalaman:last-child #delete-pengalaman')

    myBrowser.click('#form-rujukan .content-rujukan:last-child #delete-rujukan')

    myBrowser.click('#form-bahasa .content-bahasa:last-child #delete-bahasa')

    myBrowser.click('#form-kemampuan .content-kemampuan:last-child #delete-kemampuan')

    myBrowser.execute_script("window.scroll(0, 0);")

    myBrowser.click('#btn-choose-template')

    myBrowser.wait_title('Choose Template')

    assert myBrowser.title == "Choose Template"

    myBrowser.quit()

load_dotenv()
test_tc01_input_data()