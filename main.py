import time
from typing import List

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import os

from constant import ConstVariables
from dev import DevVariables
from prod import ProdVariables
from step import TestStep
from variable import Variables

CONST_VAR: ConstVariables = ConstVariables()
ENV_VAR: Variables = DevVariables()
chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")
WEBDRIVER = webdriver.Chrome(options=chromeOptions)


def main():
    execute('dev')


def clear_element(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)


def step_0():
    login_url: str = ENV_VAR.domain + CONST_VAR.login_urls[0]
    elements = CONST_VAR.login_element
    WEBDRIVER.get(login_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))

    # Fill form
    input_username = WEBDRIVER.find_element_by_xpath(elements[1])
    input_username.send_keys(ENV_VAR.username)

    input_password = WEBDRIVER.find_element_by_xpath(elements[2])
    input_password.send_keys(ENV_VAR.password)

    # Submit
    WEBDRIVER.find_element_by_xpath(elements[3]).click()

    WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "number-report-item")))


def step_1(params_list):
    # Init
    delivery_fee_url: str = ENV_VAR.domain + CONST_VAR.merchant_urls[0].format(BUSINESS_ID)
    elements = CONST_VAR.merchant_rule_order_element
    params = params_list
    WEBDRIVER.get(delivery_fee_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))
    try:
        WEBDRIVER.find_element_by_xpath(elements[1]).click()
    except:
        pass

    # Fill form
    input_base_shipping_fee_amount = WEBDRIVER.find_element_by_xpath(elements[2])
    clear_element(input_base_shipping_fee_amount)
    input_base_shipping_fee_amount.send_keys(int(params[0]))

    input_base_shipping_fee_distance = WEBDRIVER.find_element_by_xpath(elements[3])
    clear_element(input_base_shipping_fee_distance)
    input_base_shipping_fee_distance.send_keys(params[1])

    input_shipping_fee_per_unit = WEBDRIVER.find_element_by_xpath(elements[4])
    clear_element(input_shipping_fee_per_unit)
    input_shipping_fee_per_unit.send_keys(params[2])

    input_subtotal_increment = WEBDRIVER.find_element_by_xpath(elements[5])
    clear_element(input_subtotal_increment)
    input_subtotal_increment.send_keys(params[3])

    input_base_shipping_fee_amount_decrement = WEBDRIVER.find_element_by_xpath(elements[6])
    clear_element(input_base_shipping_fee_amount_decrement)
    input_base_shipping_fee_amount_decrement.send_keys(params[4])

    input_base_shipping_fee_distance_increment = WEBDRIVER.find_element_by_xpath(elements[7])
    clear_element(input_base_shipping_fee_distance_increment)
    input_base_shipping_fee_distance_increment.send_keys(params[5])

    input_commission_type = WEBDRIVER.find_element_by_xpath(elements[8])
    input_commission_type.send_keys(params[6])
    input_commission_type.send_keys(Keys.ENTER)

    input_commission_value = WEBDRIVER.find_element_by_xpath(elements[9])
    clear_element(input_commission_value)
    input_commission_value.send_keys(params[7])

    # Submit
    try:
        WEBDRIVER.find_element_by_xpath(elements[10]).click()
    except:
        WEBDRIVER.find_element_by_xpath(elements[11]).click()

    # @Todo: wait for submit
    # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_2(params_list):
    payment_method_url: str = ENV_VAR.domain + CONST_VAR.merchant_urls[1].format(BUSINESS_ID)
    elements = CONST_VAR.merchant_payment_element
    params = params_list
    WEBDRIVER.get(payment_method_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))
    WEBDRIVER.find_element_by_xpath(elements[1]).click()

    # Fill form
    input_payment_method = WEBDRIVER.find_element_by_xpath(elements[2])
    input_payment_method.send_keys(params[0])
    input_payment_method.send_keys(Keys.ENTER)

    input_payment_weight = WEBDRIVER.find_element_by_xpath(elements[3])
    clear_element(input_payment_weight)
    input_payment_weight.send_keys(params[1])

    WEBDRIVER.find_element_by_xpath(elements[4]).click()

    # @Todo: wait for submit
    # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_3(params_list):
    shipping_carrier_url: str = ENV_VAR.domain + CONST_VAR.merchant_urls[2].format(BUSINESS_ID)
    elements = CONST_VAR.merchant_carrier_element
    params = params_list
    WEBDRIVER.get(shipping_carrier_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))
    WEBDRIVER.find_element_by_xpath(elements[1]).click()

    # Fill form
    input_shipping_carrier = WEBDRIVER.find_element_by_xpath(elements[2])
    input_shipping_carrier.send_keys(params[0])
    input_shipping_carrier.send_keys(Keys.ENTER)

    input_carrier_weight = WEBDRIVER.find_element_by_xpath(elements[3])
    clear_element(input_carrier_weight)
    input_carrier_weight.send_keys(params[1])

    # Submit
    WEBDRIVER.find_element_by_xpath(elements[4]).click()

    # @Todo: wait for submit
    # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_4(params_list):
    commission_rule_url: str = ENV_VAR.domain + CONST_VAR.place_urls[0].format(PLACE_ID)
    elements = CONST_VAR.place_commission_rule_element
    params = params_list
    WEBDRIVER.get(commission_rule_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))

    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[1])))

    # Fill form
    input_commission_type = WEBDRIVER.find_element_by_xpath(elements[1])
    input_commission_type.send_keys(params[0])
    input_commission_type.send_keys(Keys.ENTER)

    input_commission_value = WEBDRIVER.find_element_by_xpath(elements[2])
    clear_element(input_commission_value)
    input_commission_value.send_keys(int(params[1]))

    input_max_commission_value = WEBDRIVER.find_element_by_xpath(elements[3])
    clear_element(input_max_commission_value)
    input_max_commission_value.send_keys(int(params[2]))

    input_cashback_type = WEBDRIVER.find_element_by_xpath(elements[4])
    input_cashback_type.send_keys(params[3])
    input_cashback_type.send_keys(Keys.ENTER)

    input_cashback_value = WEBDRIVER.find_element_by_xpath(elements[5])
    clear_element(input_cashback_value)
    input_cashback_value.send_keys(int(params[4]))

    input_max_cashback_value = WEBDRIVER.find_element_by_xpath(elements[6])
    clear_element(input_max_cashback_value)
    input_max_cashback_value.send_keys(int(params[5]))

    # Submit
    # WEBDRIVER.find_element_by_xpath(elements[7]).click()

    # @Todo: wait for submit
    # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_5(params_list):
    zalo_contact_url: str = ENV_VAR.domain + CONST_VAR.place_urls[1].format(PLACE_ID)
    elements = CONST_VAR.place_zalo_element
    params = params_list
    WEBDRIVER.get(zalo_contact_url)

    # Identify page
    WebDriverWait(WEBDRIVER, 10).until(
        EC.presence_of_element_located((By.XPATH, elements[0])))
    WEBDRIVER.find_element_by_xpath(elements[1]).click()

    # Fill form
    input_phone_number = WEBDRIVER.find_element_by_xpath(elements[2])
    input_phone_number.send_keys('0836190198')

    # Submit
    # WEBDRIVER.find_element_by_xpath(elements[3]).click()

    # @Todo: wait for submit
    # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_6(params_list):
    option_url: str = ENV_VAR.domain + CONST_VAR.place_urls[2].format(PLACE_ID)
    elements = CONST_VAR.place_option_element

    params_list.pop(0)
    for params in params_list:
        WEBDRIVER.get(option_url)
        # Identify page
        WebDriverWait(WEBDRIVER, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, elements[0])))

        # Fill form
        try:
            btn_edit = WebDriverWait(WEBDRIVER, 2).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='{}']".format(params[0]))))

            btn_edit.click()
        except Exception as ex:
            print(ex)
            WEBDRIVER.find_element_by_xpath(elements[1]).click()
        finally:
            WebDriverWait(WEBDRIVER, 10).until(
                EC.visibility_of_element_located((By.XPATH, elements[2])))

            input_title = WEBDRIVER.find_element_by_xpath(elements[2])
            clear_element(input_title)
            input_title.send_keys(params[0])

            input_price = WEBDRIVER.find_element_by_xpath(elements[3])
            clear_element(input_price)
            input_price.send_keys(int(params[1]))

            input_min_quantity = WEBDRIVER.find_element_by_xpath(elements[4])
            clear_element(input_min_quantity)
            input_min_quantity.send_keys(int(params[2]))

            input_max_quantity = WEBDRIVER.find_element_by_xpath(elements[5])
            clear_element(input_max_quantity)
            input_max_quantity.send_keys(int(params[3]))

            # Submit
            try:
                WEBDRIVER.find_element_by_xpath(elements[6]).click()
            except Exception as ex:
                print(ex)

        # @Todo: wait for submit
        # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_7(params_list):
    option_group_url: str = ENV_VAR.domain + CONST_VAR.place_urls[3].format(PLACE_ID)
    elements = CONST_VAR.place_option_group_element

    params_list.pop(0)
    for params in params_list:
        WEBDRIVER.get(option_group_url)

        # Identify page
        WebDriverWait(WEBDRIVER, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, elements[0])))

        # Fill form
        try:
            WEBDRIVER.find_element_by_xpath("//*[text()='{}']".format(params[0])).click()
        except Exception as ex:
            print(ex)
            WEBDRIVER.find_element_by_xpath(elements[1]).click()

        finally:
            WebDriverWait(WEBDRIVER, 10).until(
                EC.visibility_of_element_located((By.XPATH, elements[2])))

            input_title = WEBDRIVER.find_element_by_xpath(elements[2])
            clear_element(input_title)
            input_title.send_keys(params[0])

            input_option = WebDriverWait(WEBDRIVER, 10).until(
                EC.visibility_of_element_located((By.XPATH, elements[3])))
            clear_element(input_option)
            options = params[1].split(",")
            for option in options:
                input_option.send_keys(option)
                input_option.send_keys(Keys.ENTER)

            input_min_quantity = WEBDRIVER.find_element_by_xpath(elements[4])
            clear_element(input_min_quantity)
            input_min_quantity.send_keys(int(params[2]))

            input_max_quantity = WEBDRIVER.find_element_by_xpath(elements[5])
            clear_element(input_max_quantity)
            input_max_quantity.send_keys(int(params[3]))

            # Submit
            try:
                WEBDRIVER.find_element_by_xpath(elements[6]).click()
            except:
                WEBDRIVER.find_element_by_xpath(elements[7]).click()

        # @Todo: wait for submit
        # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_8(params_list):
    product_category_url: str = ENV_VAR.domain + CONST_VAR.place_urls[4].format(PLACE_ID)
    elements = CONST_VAR.place_product_category_element

    params_list.pop(0)
    for params in params_list:
        WEBDRIVER.get(product_category_url)

        # Identify page
        WebDriverWait(WEBDRIVER, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, elements[0])))

        # Fill form
        try:
            WEBDRIVER.find_element_by_xpath(
                "//p[text()='{}']/following::div[@class='icon-edit']".format(params[0])).click()
        except:
            WEBDRIVER.find_element_by_xpath(elements[1]).click()
        finally:
            WebDriverWait(WEBDRIVER, 10).until(
                EC.visibility_of_element_located((By.XPATH, elements[2])))

            input_name = WEBDRIVER.find_element_by_xpath(elements[2])
            clear_element(input_name)
            input_name.send_keys(params[0])

            input_weight = WEBDRIVER.find_element_by_xpath(elements[3])
            clear_element(input_weight)
            input_weight.send_keys(params[1])

            # Submit
            try:
                WEBDRIVER.find_element_by_xpath(elements[4]).click()
            except:
                WEBDRIVER.find_element_by_xpath(elements[5]).click()
        # @Todo: wait for submit
        # WebDriverWait(WEBDRIVER, 10).until(EC.presence_of_element_located((By.XPATH, elements[0])))


def step_9(params_list):
    product_url: str = ENV_VAR.domain + CONST_VAR.place_urls[4].format(PLACE_ID)
    elements = CONST_VAR.place_product_element

    params_list.pop(0)
    for params in params_list:
        WEBDRIVER.get(product_url)

        # Identify page
        WebDriverWait(WEBDRIVER, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, elements[0].format(params[0]))))

        # Fill form
        WEBDRIVER.find_element_by_xpath(elements[1].format(params[0])).click()

        input_catalog = WebDriverWait(WEBDRIVER, 10).until(
            EC.visibility_of_element_located((By.XPATH, elements[2])))

        input_name = WEBDRIVER.find_element_by_xpath(elements[3])
        input_name.send_keys(params[1])

        input_excerpt = WEBDRIVER.find_element_by_xpath(elements[4])
        if params[2] != '':
            clear_element(input_excerpt)
            input_excerpt.send_keys(params[2])

        input_more_option = WebDriverWait(WEBDRIVER, 10).until(
            EC.visibility_of_element_located((By.XPATH, elements[5])))
        clear_element(input_more_option)
        options = params[3].split(",")
        for option in options:
            input_more_option.send_keys(option)
            input_more_option.send_keys(Keys.ENTER)

        input_weight = WEBDRIVER.find_element_by_xpath(elements[6])
        clear_element(input_weight)
        input_weight.send_keys(int(params[4]))

        input_price = WEBDRIVER.find_element_by_xpath(elements[7])
        clear_element(input_price)
        input_price.send_keys(int(params[5]))

        input_sale_price = WEBDRIVER.find_element_by_xpath(elements[8])
        clear_element(input_sale_price)
        input_sale_price.send_keys(int(params[6]))

        input_min_quantity = WEBDRIVER.find_element_by_xpath(elements[9])
        clear_element(input_min_quantity)
        input_min_quantity.send_keys(int(params[7]))

        input_max_quantity = WEBDRIVER.find_element_by_xpath(elements[10])
        clear_element(input_max_quantity)
        input_max_quantity.send_keys(int(params[8]))

        input_discount_percent = WEBDRIVER.find_element_by_xpath(elements[11])
        clear_element(input_discount_percent)
        input_discount_percent.send_keys(int(params[9]))

        WEBDRIVER.find_element_by_xpath(elements[12]).click()

        WEBDRIVER.find_element_by_xpath(elements[13]).click()
        try:
            input_image = WebDriverWait(WEBDRIVER, 10).until(
                EC.presence_of_element_located((By.XPATH, elements[14])))
            input_image.send_keys(os.path.dirname(os.path.abspath(__file__)) + "/img/product/{}".format(params[10]))

            WEBDRIVER.find_element_by_xpath(elements[15]).click()

        except Exception as ex:
            print(ex)

        # Submit
        time.sleep(2)

        btn_submit = WEBDRIVER.find_element_by_xpath(elements[16])

        ActionChains(WEBDRIVER).move_to_element(btn_submit).perform()

        btn_submit.click()
        # @Todo: wait for submit


def import_file():
    import csv

    with open('test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        step = 0
        step_list = list()
        step_list_item = list()
        option_list = list()

        for row in csv_reader:
            row = normalize(row)

            if len(row) > 0:
                if "Thiết lập ID" in row[0]:
                    step = 0
                elif "Thiết lập phí giao hàng" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 1
                elif "Phương phức thanh toán" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 2
                elif "Đối tác vận chuyển" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 3
                elif "Commission Rule" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 4
                elif "Zalo" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 5
                elif ". Tùy chọn" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 6
                elif ". Tùy chọn nhóm" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 7
                elif "Tạo danh mục" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 8
                elif "Tạo sản phẩm trong danh mục" in row[0]:
                    step_list.append(step_list_item)
                    step_list_item = list()
                    step = 9

                else:
                    if step >= 6:
                        option_list = list()
                        for r in range(0, len(row)):
                            option_list.append(row[r])
                        step_list_item.append(option_list)
                    elif step >= 0:
                        step_list_item.append(row[1] if len(row) > 1 else '')

                line_count += 1

        step_list.append(step_list_item)
        print(f'Processed {line_count} lines.')
        return step_list


def normalize(data):
    result = data[::-1]

    if len(result) > 0:
        while result[0] == '':
            result.pop(0)
            if len(result) == 0:
                break

    return result[::-1]


def execute(environment: str = 'dev'):
    global BUSINESS_ID, PLACE_ID
    ENV_VAR = DevVariables if environment == 'dev' else ProdVariables

    process_step: List[TestStep] = []
    step = 0

    data_list = import_file()

    business_ids = data_list[0][0].split(",")
    place_ids = data_list[0][1].split(",")
    business_count = 0
    place_count = 0

    try:
        # Step 0 (Login)
        step = 0
        step_0()

        for business_id in business_ids:
            BUSINESS_ID = business_id
            business_count += 1

            # # Step 1 (Thiết lập phí giao hàng)
            # step = 1
            # step_1(data_list[1])
            #
            # # Step 2 (Phương phức thanh toán)
            # step = 2
            # step_2(data_list[2])
            #
            # # Step 3 (Đối tác vận chuyển)
            # step = 3
            # step_3(data_list[3])

            # # Step 4 (Commission Rule)
            # step = 4
            # step_4(step_list[4])
            #

            # # Step 5 (Zalo)
            # step = 5
            # step_5(step_list[4])

        for place_id in place_ids:
            PLACE_ID = place_id
            place_count += 1

            # # Step 6 (Tùy chọn)
            # step = 6
            # step_6(data_list[5])
            #
            # # Step 7 (Tùy chọn nhóm)
            # step = 7
            # step_7(data_list[6])
            #
            # # Step 8 (Tạo danh mục)
            # step = 8
            # step_8(data_list[7])

            # Step 9 (Tạo mới sản phẩm)
            step = 9
            step_9(data_list[8])

            print('Finish...\n')

    except Exception as ex:
        print(ex)
        print("Step {} Error\n"
              "Business id: {}\n"
              "Place id: {}\n"
              "Business count: {}\n"
              "Place count: {}\n".format(step, BUSINESS_ID, PLACE_ID, business_count, place_count))
        # "Place count: {}\n".format(step, business_id, place_id, business_count, place_count))

    finally:
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
