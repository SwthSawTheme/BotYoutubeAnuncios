from selenium import webdriver

# Inicializa o driver do navegador (certifique-se de ter o driver correspondente instalado, como ChromeDriver)
driver = webdriver.Chrome()

# Abre o YouTube
driver.get("https://www.youtube.com")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o driver do navegador (certifique-se de ter o driver correspondente instalado, como ChromeDriver)
driver = webdriver.Chrome()

# Abre o YouTube
driver.get("https://www.youtube.com")

# Aguarda o carregamento da página do YouTube
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))

# Encontra a barra de pesquisa e insere um termo de busca (qualquer termo)
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("Python programming")  # Por exemplo, pesquisaremos por vídeos de programação Python
search_box.submit()

# Aguarda o carregamento da página de resultados da pesquisa
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contents")))

# Encontra o primeiro vídeo na lista de resultados e clica nele
first_video = driver.find_element(By.CSS_SELECTOR, "#contents ytd-video-renderer")
first_video.click()
