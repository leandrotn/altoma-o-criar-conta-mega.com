from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time

def generate_random_name(length=8):
    """Gera um nome aleatório com letras maiúsculas e minúsculas."""
    return ''.join(random.choices(string.ascii_letters, k=length))

# URLs das páginas
mega_url = "https://mega.nz/register"
guerrilla_mail_url = "https://www.guerrillamail.com/inbox"

# Inicializa o driver do navegador (Chrome)
driver = webdriver.Chrome()

# Acessa o site Mega.nz
driver.get(mega_url)

# Aguarda o carregamento dos elementos de nome e sobrenome
try:
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Nome"]'))
    )
    last_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Sobrenome"]'))
    )
except Exception as e:
    print("Erro ao localizar os campos de entrada:", e)
    driver.quit()
    exit()

# Gera nomes aleatórios
first_name = generate_random_name()
last_name = generate_random_name()

# Preenche os campos com os nomes gerados
first_name_field.clear()
first_name_field.send_keys(first_name)

last_name_field.clear()
last_name_field.send_keys(last_name)

# Imprime os nomes gerados no terminal
print(f"Nome gerado: {first_name}")
print(f"Sobrenome gerado: {last_name}")

# Abre uma nova guia e acessa o site Guerrilla Mail
driver.execute_script("window.open('');")  # Abre uma nova guia em branco
driver.switch_to.window(driver.window_handles[1])  # Alterna para a nova guia
driver.get(guerrilla_mail_url)  # Acessa o site Guerrilla Mail

# Aguarda o elemento de e-mail ficar disponível e captura o valor
try:
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email-widget"))
    )
    email_address = email_element.text  # Obtém o texto do e-mail
    print(f"E-mail temporário capturado: {email_address}")
except Exception as e:
    print("Erro ao capturar o e-mail temporário:", e)
    driver.quit()
    exit()

# Volta para a guia inicial (Mega.nz)
driver.switch_to.window(driver.window_handles[0])

# Aguarda o campo de e-mail no Mega.nz e preenche com o e-mail capturado
try:
    email_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "register-email-registerpage2"))
    )
    email_input_field.clear()
    email_input_field.send_keys(email_address)
    print(f"E-mail preenchido na página Mega.nz: {email_address}")
except Exception as e:
    print("Erro ao preencher o e-mail na página Mega.nz:", e)
    driver.quit()
    exit()

# Preenche os campos de senha
password = "leonardotn192"  # Senha padrão

# Aguarda o campo de senha e interage com ele
try:
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "register-password-registerpage2"))
    )
    password_field.click()
    time.sleep(0.5)
    password_field.clear()
    password_field.send_keys(password)
    print("Senha preenchida com:", password)
except Exception as e:
    print("Erro ao preencher o campo de senha:", e)
    driver.quit()
    exit()

# Aguarda o campo de confirmação de senha e preenche com a mesma senha
try:
    confirm_password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "register-password-registerpage3"))
    )
    confirm_password_field.click()
    time.sleep(0.5)
    confirm_password_field.clear()
    confirm_password_field.send_keys(password)
    print("Confirmação de senha preenchida com:", password)
except Exception as e:
    print("Erro ao preencher o campo de confirmação de senha:", e)
    driver.quit()
    exit()

# Aguarda a primeira caixinha de verificação e clica nela
try:
    checkbox1_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.checkbox-block.pw-remind .checkbox'))
    )
    driver.execute_script("arguments[0].click();", checkbox1_element)  # Força o clique via JavaScript
    print("Primeira caixinha de verificação marcada com sucesso.")
except Exception as e:
    print("Erro ao marcar a primeira caixinha de verificação:", e)
    driver.save_screenshot('debug_checkbox1.png')  # Captura uma tela para debugging
    driver.quit()
    exit()

# Aguarda a segunda caixinha de verificação e clica nela
try:
    checkbox2_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "register-check-registerpage2"))
    )
    driver.execute_script("arguments[0].click();", checkbox2_element)  # Força o clique via JavaScript
    print("Segunda caixinha de verificação marcada com sucesso.")
except Exception as e:
    print("Erro ao marcar a segunda caixinha de verificação:", e)
    driver.save_screenshot('debug_checkbox2.png')  # Captura uma tela para debugging
    driver.quit()
    exit()

# Aguarda o botão "Criar uma conta no MEGA" e clica nele
try:
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mega-button.branded-red.large.register-button.right.active'))
    )
    register_button.click()  # Realiza o clique no botão
    print("Botão 'Criar uma conta no MEGA' clicado com sucesso.")
except Exception as e:
    print("Erro ao clicar no botão 'Criar uma conta no MEGA':", e)
    driver.quit()
    exit()

# Aguarda a mensagem de sucesso de registro
try:
    success_message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.reg-success-normal div'))
    )
    time.sleep(2)
    print("Mensagem de sucesso capturada:", success_message.text)
except Exception as e:
    print("Erro ao capturar a mensagem de sucesso:", e)
    driver.quit()
    exit()

# Volta para a guia do Guerrilla Mail
try:
    driver.switch_to.window(driver.window_handles[1])  # Alterna para a aba Guerrilla Mail
    print("Retornando para a guia do Guerrilla Mail.")
except Exception as e:
    print("Erro ao alternar para a guia do Guerrilla Mail:", e)
    driver.quit()
    exit()


# Aguarda e clica na mensagem "MEGA - Confirme o seu email" no Guerrilla Mail
print("Aguardando a mensagem 'MEGA - Confirme o seu email'...")

timeout = 300  # Tempo máximo de espera em segundos
interval = 10  # Intervalo entre verificações em segundos
start_time = time.time()

while True:
    try:
        # Obtém a tabela de mensagens
        email_list = driver.find_element(By.ID, "email_list")
        
        # Verifica se há uma mensagem com o texto "MEGA - Confirme o seu email"
        mega_email_row = email_list.find_element(By.XPATH, './/tr[contains(., "MEGA - Confirme o seu email")]')
        
        # Se encontrada, clica na mensagem
        mega_email_row.click()
        print("Mensagem encontrada e clicada: 'MEGA - Confirme o seu email'")
        break  # Sai do loop após encontrar e clicar na mensagem
    except Exception:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print("Tempo máximo de espera atingido. O e-mail não foi encontrado.")
            driver.quit()
            exit()
        print(f"Mensagem ainda não encontrada. Verificando novamente em {interval} segundos...")
        time.sleep(interval)


try:
    # Aguarda o carregamento do conteúdo do e-mail
    email_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//td[@valign="top" and contains(@style, "background-color:#d90007;")]//a'))
    )
    
    # Obtém o link do botão "Ativar a conta"
    activation_link = email_content.get_attribute("href")
    print(f"Link de ativação encontrado: {activation_link}")
    
    # Abre o link em uma nova aba
    driver.execute_script(f"window.open('{activation_link}', '_blank');")
    print("Link de ativação aberto em uma nova aba.")
except Exception as e:
    print("Erro ao capturar ou abrir o link de ativação:", e)
    driver.quit()
    exit()


try:
    # Alterna para a última aba aberta (página de ativação)
    driver.switch_to.window(driver.window_handles[-1])
    print("Alternado para a aba de ativação da conta.")
    
    # Aguarda o campo de senha ficar disponível
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-password2"))
    )
    
    # Preenche o campo de senha
    password = "leonardotn192"
    password_field.clear()
    password_field.send_keys(password)
    print(f"Senha '{password}' preenchida com sucesso.")
except Exception as e:
    print("Erro ao preencher a senha na página de ativação:", e)
    driver.quit()
    exit()


try:
    # Aguarda o botão "Confirme a sua conta" ficar disponível
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "mega-button positive login-button") and span[text()="Confirme a sua conta"]]'))
    )
    
    # Clica no botão
    confirm_button.click()
    print("Botão 'Confirme a sua conta' clicado com sucesso.")
except Exception as e:
    print("Erro ao clicar no botão 'Confirme a sua conta':", e)
    driver.quit()
    exit()


# Mantém o navegador aberto indefinidamente
try:
    print("Os sites estão abertos. Pressione Ctrl+C no terminal para encerrar.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando...")
    driver.quit()
