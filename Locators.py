from selenium.webdriver.common.by import By


# clase para los localizadores
class UrbanRoutesLocators:
    # Localizadores para los campos "from" y "to" y el botón de pedido de taxi
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CLASS_NAME, 'button.round')

    # Localizadores para elección de tarifa
    comfort_option = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")

    # Localizadores para agregar teléfono
    phone_field = (By.CLASS_NAME, 'np-button')
    phone_input_field = (By.ID, 'phone')
    add_number_button = (By.CLASS_NAME, 'button.full')
    phone_code = (By.ID, 'code')
    section_code_window = (By.CLASS_NAME, 'section active')
    accept_code_button = (By.XPATH, "//button[text()='Confirmar'] ")

    # Localizadores para los campos de tarjeta y método de pago
    payment_field = (By.CLASS_NAME, 'pp-text')
    payment_field_added = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
    card_field = (By.CLASS_NAME, 'pp-plus')
    card_number_input = (By.CLASS_NAME, 'card-input')
    card_code_input = (By.CSS_SELECTOR, "input[name='code']")
    press_screen = (By.CLASS_NAME, 'card-wrapper')
    added_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_card_details_window_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    # Localizador para mensaje al conductor
    message_driver_field = (By.ID, 'comment')

    # Localizador para extras de viaje
    request_blanket_and_tissues = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    ice_cream_request = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    ice_cream_added = (By.XPATH, "//div[@class='counter-value' and text()='2']")

    # Localizadores para ordenar un taxi
    order_a_cab_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    looking_for_a_car = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[2]')
    ride_details = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')
