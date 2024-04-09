import data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from Locators import UrbanRoutesLocators


class UrbanRoutesMethods:

    def __init__(self, driver):
        # Inicialización de la página con el controlador de Selenium
        self.driver = driver
        self.locators = UrbanRoutesLocators()

    # Método para establecer la dirección "from"
    def set_from(self, from_address):
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    # Método para establecer la dirección "to"
    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    # Método para obtener la dirección "from"
    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    # Método para obtener la dirección "to"
    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # Método para solicitar un taxi
    def click_request_taxi_button(self):
        self.driver.find_element(*self.locators.request_taxi_button).click()

    # Método combinado para establecer la ruta completa y solicitar el taxi
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        # Esperar a que aparezca el botón "pedir taxi"
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.request_taxi_button)
        )
        # Hacer clic en el botón "pedir taxi"
        self.click_request_taxi_button()

    # Método para seleccionar la tarifa comfort
    def select_comfort_option(self):
        # Espera a que aparezca el elemento "tarifa comfort"
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.comfort_option)
        )
        # Selecciona la tarifa "Comfort"
        comfort_option_element = self.driver.find_element(*self.locators.comfort_option)
        comfort_option_element.click()

    # Método para obtener el texto del elemento "tarifa comfort"
    def get_tariff_name(self):
        return self.driver.find_element(*self.locators.comfort_option).text

    # Método para ingresar el número de teléfono
    def set_phone_number(self, phone_number):
        # Hace clic en el campo para ingresar el número de teléfono
        phone_field = self.driver.find_element(*self.locators.phone_field)
        phone_field.click()

        # Espera a que aparezca la pantalla emergente con el campo de entrada para ingresar el número de teléfono
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.phone_input_field))

        # Encuentra el campo de entrada de número de teléfono e ingresa el número
        phone_input_field = self.driver.find_element(*self.locators.phone_input_field)
        phone_input_field.clear()  # Limpiar cualquier contenido anterior
        phone_input_field.send_keys(phone_number)

        # Hace clic en el botón para guardar el número de teléfono
        add_number = self.driver.find_element(*self.locators.add_number_button)
        add_number.click()

    # Método para obtener el código de seguridad del teléfono ingresado
    @staticmethod
    def retrieve_phone_code(driver) -> str:
        """Esta función recupera y llena el código de confirmación del teléfono."""
        import json
        import time

        # Localizador del campo de código de confirmación
        phone_code = (By.ID, 'code')
        # Localizador del botón "Aceptar código de confirmación"
        accept_code_button = (By.CLASS_NAME, 'button.full')
        # Localizador del elemento fuera del campo de código de confirmación
        element_outside_code_field = (By.XPATH, '//div[@class="section active"]')

        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                  {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu "
                                "aplicación.")

            # Encuentra el campo de entrada de código de confirmación y lo ingresa
            code_input_field = WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable(phone_code)
            )
            code_input_field.clear()  # Limpiar cualquier contenido anterior
            code_input_field.send_keys(code)
            return

    # Método para guardar código de seguridad de teléfono
    def click_accept_code_number_button(self):
        accept_code_number = self.driver.find_element(*self.locators.accept_code_button)
        accept_code_number.click()

    # Método para añadir forma de pago
    def add_payment_method(self):
        # Hace click en el campo para ingresar el método de pago
        payment_field = self.driver.find_element(*self.locators.payment_field)
        payment_field.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.card_field))

        # Hace clic en el campo para agregar una tarjeta
        card_field = self.driver.find_element(*self.locators.card_field)
        card_field.click()

    # Método para ingresar datos de la tarjeta
    def set_card_details(self, card_number, card_code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.card_number_input))

        # Encuentra los campos de entrada de número de tarjeta y código y los ingresa
        card_number_field = self.driver.find_element(*self.locators.card_number_input)
        card_code_field = self.driver.find_element(*self.locators.card_code_input)
        card_number_field.clear()  # Limpiar cualquier contenido anterior
        card_code_field.clear()  # Limpiar cualquier contenido anterior
        card_number_field.send_keys(card_number)
        card_code_field.send_keys(card_code)

    # Método para simular un click fuera de la pantalla de tarjeta para poder activar el botón "guardar"
    def simulate_clicking_on_screen(self):
        element = self.driver.find_element(*self.locators.press_screen)
        element.click()

    # Método para guardar datos de tarjeta
    def click_added_card_button(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(
                self.locators.added_card_button
            )
        )
        # Hace clic en el botón guardar datos de tarjeta
        added_card_button = self.driver.find_element(
            *self.locators.added_card_button
        )
        added_card_button.click()

        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(
                self.locators.close_card_details_window_button
            )
        )

        # Hace clic en el botón de cerrar pantalla de método de pago
        close_button_payment_method_window = self.driver.find_element(
            *self.locators.close_card_details_window_button
        )
        close_button_payment_method_window.click()

    # Método combinado para añadir una nueva tarjeta
    def add_new_card(self, card_number, card_code):
        self.add_payment_method()
        self.set_card_details(card_number, card_code)
        self.simulate_clicking_on_screen()

    # Método para obtener el texto en el campo de método de pago
    def get_payment_field_text(self):
        return self.driver.find_element(*self.locators.payment_field_added).text

    # Método para dejar un mensaje al conductor
    def set_message_for_driver(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.message_driver_field))
        # Encontrar y llenar el campo de entrada del mensaje
        message = self.driver.find_element(*self.locators.message_driver_field)
        message.clear()  # Limpiar cualquier contenido anterior
        message.send_keys(data.message_for_driver)

    # Método para solicitar ítems durante el viaje (manta y pañuelos)
    def travel_request(self):
        extra_request = self.driver.find_element(*self.locators.request_blanket_and_tissues)
        extra_request.click()

    # Método para solicitar ítems adicionales durante el viaje (dos helados)
    def request_two_ice_creams(self):
        ice_cream_element = self.driver.find_element(*self.locators.ice_cream_request)

        # Crear una instancia de ActionChains para realizar acciones del mouse
        action_chains = ActionChains(self.driver)

        # Hacer clic dos veces en el elemento de helado
        action_chains.double_click(ice_cream_element).perform()

    # Método para verificar que el botón "Pedir taxi" se haya activado correctamente
    def click_on_the_button_to_order_a_cab(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.order_a_cab_button))
        order_a_cab = self.driver.find_element(*self.locators.order_a_cab_button)
        order_a_cab.click()

    # Método para obtener la etiqueta del botón "pedir taxi" para corroborar que se activó correctamente
    def get_order_cab_button_label(self):
        return self.driver.find_element(*self.locators.order_a_cab_button).text

    # Método para verificar que se pidió el taxi y apareció el temporizador
    def looking_for_a_car_window(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.looking_for_a_car))
        # Devuelve el texto en la ventana de búsqueda de taxi
        return self.driver.find_element(*self.locators.looking_for_a_car).text

    # Método para visualizar los detalles del viaje
    def get_ride_details(self):
        # Espera a que el temporizador haya llegado a 0
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.locators.ride_details))

        # Devuelve el texto de la ventana de los detalles del viaje
        return self.driver.find_element(*self.locators.ride_details).text
