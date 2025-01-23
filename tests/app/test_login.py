import pytest
from pages.app.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import URL_ETRM, TENANT_CREDENTIALS


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):  # Supongamos que tienes un fixture que proporciona el driver
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.url = URL_ETRM
        self.credentials = TENANT_CREDENTIALS["tbsg"]
        self.username = self.credentials["username"]
        self.password = self.credentials["password"]

    def test_login(self):
        """Prueba de login exitoso."""
        self.login_page.open_login_page(self.url)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()

        # Verificar el nombre de usuario después del login
        user_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user_name"))
        ).text
        assert user_name == self.username, "El nombre de usuario no coincide."

    def test_cerrar_sesion(self):
        """Prueba de cierre de sesión después de login."""        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user_name"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="logoutMenuItem"]'))
        ).click()

        # Verificar que se redirige al login
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.username_input)
        ), "No se volvió a la página de login."

    def test_contraseña_incorrecta(self):
        """Prueba de contraseña incorrecta."""
        self.login_page.open_login_page(self.url)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password("wrong_password")
        self.login_page.click_login_button()

        # Verificar mensaje de error
        assert "No puede iniciar sesión" in self.login_page.get_notification_message()

    def test_usuario_incorrecto(self):
        """Prueba de usuario incorrecto."""
        self.login_page.open_login_page(self.url)
        self.login_page.enter_username("wrong_username")
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()

        # Verificar mensaje de error
        assert "No puede iniciar sesión" in self.login_page.get_notification_message()

    def test_campos_vacio(self):
        """Prueba de validación de campos vacíos."""
        self.login_page.open_login_page(self.url)

        # Verificar botón deshabilitado con campos vacíos
        assert not self.login_page.is_login_button_enabled(),"El botón está habilitado con campos vacíos."

        # Usuario lleno, contraseña vacía
        self.login_page.enter_username(self.username)
        assert not self.login_page.is_login_button_enabled(), "El botón está habilitado con sólo el usuario ingresado."
        self.login_page.clear_username()

        # Usuario vacío, contraseña llena
        self.login_page.enter_password(self.password)
        assert not self.login_page.is_login_button_enabled(), "El botón está habilitado con sólo la contraseña ingresada."

    def test_recuperar_contraseña(self):
        """Prueba de recuperación de contraseña."""
        self.login_page.open_login_page(self.url)
        self.login_page.click_recover_password()

        # Verificar redirección
        WebDriverWait(self.driver, 10).until(EC.url_contains("/recover-password"))
        current_url = self.driver.current_url
        assert current_url.endswith("/recover-password"), "La URL no es la esperada."
