import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromeDriverManager
from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromeDriverManager().install())
        print("Luching Edge Brouser..........")

    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager)().install()
        print("Luching firefox browser.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager).install()


def pytest_addoption(parser):   #this wil get the value from CLI /hooks
    parser,addoption("--browser")

@pytest.fixture()
def browser(request):   #thi wil return then browser value to setup method
    return request.config.getoption("--browser")

###################### pytet HTML reports ###############

# its hook for adding environment info to HTMLreport
def pytest_configure(config):
    config_.metadata['project name'] = 'Opencart'
    config._metadata["Module Name"] = 'CustRegistration'
    config._metadata['Tester'] = "soumya"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.popa("JAVA_HOME",None)
    metadata.pop("Plugins",None)

#spefying report folder location and save report with timestamp
@pytest.hookimpl(tryfast=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html "