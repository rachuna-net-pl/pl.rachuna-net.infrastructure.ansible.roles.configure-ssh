import pytest

SSHD_SERVICE_NAME = "sshd"
SSHD_CONFIG_PATH = "/etc/ssh/sshd_config"
SSHD_PORT = "22"
PERMIT_ROOT_LOGIN = "no"
PASSWORD_AUTHENTICATION = "no"

def get_hostname(host):
    """Pobiera rzeczywisty hostname testowanego serwera"""
    return host.check_output("hostname")


def test_sshd_running_and_enabled(host):
    """Test sprawdzający, czy usługa SSHD działa i jest włączona"""
    ssh_service = host.service(SSHD_SERVICE_NAME)

    assert ssh_service.is_running, "❌ SSHD nie jest uruchomione!"
    assert ssh_service.is_enabled, "❌ SSHD nie jest ustawione do uruchamiania przy starcie systemu!"

def test_sshd_config_exist(host):
    """Test sprawdzający poprawność konfiguracji SSHD"""

    sshd_config = host.file(SSHD_CONFIG_PATH)
    assert sshd_config.exists, f"❌ Plik konfiguracji SSHD nie istnieje: {SSHD_CONFIG_PATH}"

def test_sshd_config_check_mode(host):
    """Test sprawdzający uprawnienia pliku konfiguracji SSHD"""  

    sshd_config = host.file(SSHD_CONFIG_PATH)
    assert sshd_config.user == "root", "❌ Plik konfiguracji SSHD nie jest własnością roota!"
    assert sshd_config.group == "root", "❌ Plik konfiguracji SSHD nie jest grupy roota!"
    assert sshd_config.mode == 0o644, "❌ Plik konfiguracji SSHD nie ma praw 644!"

def test_sshd_config_is_empty(host):
    """Test sprawdzający zawartość konfiguracji SSHD"""

    sshd_config = host.file(SSHD_CONFIG_PATH)
    sshd_config_content = sshd_config.content_string.strip()
    assert sshd_config_content, "❌ Plik konfiguracji SSHD jest pusty!"

def test_sshd_config_is_set_permit_root_login(host):
    """Test sprawdzający, czy w konfiguracji SSHD jest ustawione `PermitRootLogin`"""
    sshd_config = host.file(SSHD_CONFIG_PATH)
    sshd_config_content = sshd_config.content_string

    assert "PermitRootLogin "+PERMIT_ROOT_LOGIN in sshd_config_content, "❌ `PermitRootLogin {PERMIT_ROOT_LOGIN}` nie jest ustawione!"

def test_sshd_config_is_set_password_authentication(host):
    """Test sprawdzający, czy w konfiguracji SSHD jest ustawione `PasswordAuthentication`"""
    sshd_config = host.file(SSHD_CONFIG_PATH)
    sshd_config_content = sshd_config.content_string

    assert "PasswordAuthentication "+PASSWORD_AUTHENTICATION in sshd_config_content, "❌ `PermitRootLogin {PASSWORD_AUTHENTICATION}` nie jest ustawione!"

def test_sshd_config_is_set_port(host):
    """Test sprawdzający, czy w konfiguracji SSHD jest ustawione `Port`"""
    sshd_config = host.file(SSHD_CONFIG_PATH)
    sshd_config_content = sshd_config.content_string

    assert "Port "+SSHD_PORT in sshd_config_content, "❌ `Port {SSHD_PORT}` nie jest ustawione!"   

