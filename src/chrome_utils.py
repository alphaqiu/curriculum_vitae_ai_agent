import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def chrome_browser_options():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1200x800")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-cache")
    options.add_argument("--incognito")
    options.add_argument("--allow-file-access-from-files")
    options.add_argument("--disable-web-security")

    return options


def init_browser() -> webdriver.Chrome:
    try:
        options = chrome_browser_options()
        # Use webdriver_manager to handle ChromeDriver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        logger.debug("Chrome browser initialized successfully.")
        return driver
    except Exception as e:
        logger.error(f"Failed to initialize browser: {str(e)}")
        raise RuntimeError(f"Failed to initialize browser: {str(e)}")


def HTML_to_PDF(localFileUrl: str, driver: webdriver.Chrome):
    """将HTML转换为PDF

    Args
        localFileUrl (str): HTML文件路径,以file://开头 例如：file:///Path/to/your/index.html
        driver (webdriver.Chrome): 浏览器驱动

    Returns:
        str: PDF的base64编码

    Raises:
        RuntimeError: 当WebDriver发生异常时抛出
    """
    try:
        driver.get(localFileUrl)
        # 等待页面完全加载
        time.sleep(2)  # 对于复杂的HTML可能需要增加等待时间

        # 执行CDP命令将页面打印为PDF
        pdf_base64 = driver.execute_cdp_cmd(
            "Page.printToPDF",
            {
                "printBackground": True,  # 在打印中包含背景
                "landscape": False,  # 页面方向（False为纵向）
                "paperWidth": 8.27,  # 纸张宽度（A4，单位：英寸）
                "paperHeight": 11.69,  # 纸张高度（A4，单位：英寸）
                "marginTop": 0.8,  # 上边距（单位：英寸，约2厘米）
                "marginBottom": 0.8,  # 下边距（单位：英寸，约2厘米）
                "marginLeft": 0.5,  # 左边距（单位：英寸，约1.27厘米）
                "marginRight": 0.5,  # 右边距（单位：英寸，约1.27厘米）
                "displayHeaderFooter": False,  # 不显示页眉和页脚
                "preferCSSPageSize": True,  # 优先使用CSS页面尺寸
                "generateDocumentOutline": True,  # 成文档大纲
                "generateTaggedPDF": False,  # 不生成带标签的PDF
                "transferMode": "ReturnAsBase64",  # 以base64字符串形式返回PDF
            },
        )
        return pdf_base64["data"]
    except Exception as e:
        logger.error(f"发生WebDriver异常: {e}")
        raise RuntimeError(f"发生WebDriver异常: {e}")
