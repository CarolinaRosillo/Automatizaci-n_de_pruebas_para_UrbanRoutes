import time
import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import UrbanRoutesLocators
from Methods import UrbanRoutesMethods


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # Para obtener un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--perfLoggingPrefs=enableNetwork')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.urban_routes_methods = UrbanRoutesMethods(cls.driver)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesMethods(cls.driver)
        time.sleep(5)

    def test_set_route(self):
        # Establece las direcciones de origen y destino usando el método set_route
        self.routes_page.set_route(data.address_from, data.address_to)

        # Verifica que las direcciones se establecieron correctamente
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_select_comfort_option(self):
        # Llama al método para seleccionar tarifa comfort
        self.urban_routes_methods.select_comfort_option()

        # Verifica que la tarifa seleccionada sea comfort
        selected_tariff = self.routes_page.get_tariff_name()
        expected_tariff = 'Comfort\n$10'
        assert selected_tariff == expected_tariff

    def test_fill_in_the_number_field(self):
        # Espera a que el campo de teléfono sea visible
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesLocators.phone_field)
        )

        # Llama al método para establecer el número de teléfono
        self.urban_routes_methods.set_phone_number(data.phone_number)

        # Espera a que el campo de código de teléfono sea visible
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesLocators.phone_code)
        )

        # Llama al método para ingresar y guardar el código de teléfono
        UrbanRoutesMethods.retrieve_phone_code(driver=self.driver)
        self.urban_routes_methods.click_accept_code_number_button()

    def test_add_new_card(self):
        # Llama al método para añadir una nueva tarjeta
        self.urban_routes_methods.add_new_card(data.card_number, data.card_code)
        # Llama al método para guardar detalles de la tarjeta
        self.urban_routes_methods.click_added_card_button()

    def test_set_message_for_driver(self):
        # Llama al método para dejar un mensaje al conductor
        self.urban_routes_methods.set_message_for_driver()

    def test_request_blanket_and_tissues(self):
        # Llama al método para solicitar ítems (manta y pañuelos)
        self.urban_routes_methods.travel_request()

    def test_request_two_ice_creams(self):
        # Llama a la función para agregar ítems adicionales (2 helados)
        self.urban_routes_methods.request_two_ice_creams()

    def test_request_a_cab(self):
        # Espera a que aparezca el botón "Pedir un taxi"
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesLocators.order_a_cab_button))

        # Llama al método para dar click al botón "Pedir un taxi"
        self.urban_routes_methods.click_on_the_button_to_order_a_cab()

        # Verifica que el botón "Pedir taxi" se haya activado correctamente
        label_on_button = self.urban_routes_methods.get_order_cab_button_label()
        expected_label_on_button = 'Pedir un taxi'
        assert label_on_button.startswith(
            expected_label_on_button), f"El texto en el botón de pedido de taxi no comienza con '{expected_label_on_button}'"

    def test_looking_for_a_car(self):
        # Llama al método para comprobar que se haya solicitado el taxi y aparezca la ventana de espera
        self.urban_routes_methods.looking_for_a_car_window()

        # Verifica que la ventana emergente se haya abierto y el temporizador empiece a contar
        label_on_window = self.urban_routes_methods.looking_for_a_car_window()
        expected_label_on_window = '00:'
        assert label_on_window.startswith(
            expected_label_on_window), f"El texto en el botón no comienza con '{expected_label_on_window}'"

    def test_get_driver_details(self):
        # Llama al método para comprobar que aparezcan los detalles del viaje
        self.urban_routes_methods.get_ride_details()

        # Verifica que la ventana emergente con los detalles de viaje se haya abierto
        details = self.routes_page.get_ride_details()
        expected_details = 'driver.name'
        assert details.startswith(
            expected_details), f"El texto en el botón de pedido de taxi no comienza con '{expected_details}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

