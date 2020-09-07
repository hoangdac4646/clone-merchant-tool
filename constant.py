from typing import List


class ConstVariables:
    login_urls: List[str] = ["/login"]

    merchant_urls: List[str] = ["/merchant/{}/rule-order",
                                "/merchant/{}/payment",
                                "/merchant/{}/carrier",
                                ]

    place_urls: List[str] = ["/place/{}/commission",
                             "/place/{}/zalo/contacts",
                             "/place/{}/options",
                             "/place/{}/option-group",
                             "/place/{}/products",
                             ]

    identify_element_template: str = "//*[contains(text(),'{}')]"
    input_txt_element_template: str = "//*[contains(text(),'{}')]/following-sibling::input"
    input_cbb_element_template: str = "//*[contains(text(),'{}')]/following::input"
    input_txt_area_element_template: str = "//*[contains(text(),'{}')]/following::textarea"
    button_element_template: str = "//button[text()='{}']"

    login_element: List[str] = [
        identify_element_template.format('Đăng nhập'),
        "//input[@name='username']",
        "//input[@name='password']",
        button_element_template.format('Đăng nhập')]

    merchant_rule_order_element: List[str] = [identify_element_template.format('Thiết lập phí giao hàng'),
                                              "//div[text()='{}']".format('Thiết lập phí giao hàng'),
                                              input_txt_element_template.format('Phí cơ sở'),
                                              input_txt_element_template.format('Quãng đường cơ sở'),
                                              input_txt_element_template.format('Cước phí 1km'),
                                              input_txt_element_template.format('Giá trị gia tăng của đơn hàng'),
                                              input_txt_element_template.format('Mức giảm cho phí cơ sở'),
                                              input_txt_element_template.format('Mức tăng cho quãng đường cơ sở'),
                                              input_cbb_element_template.format('Loại hoa hồng'),
                                              input_txt_element_template.format('Phí hoa hồng'),
                                              button_element_template.format('Tạo'),
                                              button_element_template.format('Cập nhật')
                                              ]

    merchant_payment_element: List[str] = [
        identify_element_template.format('Phương thức thanh toán'),
        identify_element_template.format('Thêm mới'),
        input_cbb_element_template.format("Chọn phương thức thanh toán"),
        input_txt_element_template.format("Thứ tự ưu tiên"),
        button_element_template.format('Xác nhận'),
    ]

    merchant_carrier_element: List[str] = [
        identify_element_template.format('Đối tác vận chuyển'),
        identify_element_template.format('Thêm mới'),
        input_cbb_element_template.format("Chọn đối tác vận chuyển"),
        input_txt_element_template.format("Thứ tự ưu tiên"),
        button_element_template.format('Xác nhận'),
    ]

    place_commission_rule_element: List[str] = [
        identify_element_template.format('Commission Rule'),
        input_cbb_element_template.format('Cách tính tiền hoa hồng'),
        input_txt_element_template.format('Số tiền hoa hồng'),
        input_txt_element_template.format('Số tiền hoa hồng tối đa'),
        input_cbb_element_template.format('Cách tính Cashback'),
        input_txt_element_template.format("Số tiền Cashback"),
        input_txt_element_template.format("Số tiền Cashback tối đa"),
        button_element_template.format("Cập nhật"),
    ]

    place_zalo_element: List[str] = [
        identify_element_template.format('Zalo'),
        identify_element_template.format('Thêm mới'),
        input_txt_element_template.format("Số điện thoại"),
        button_element_template.format('Xác nhận'),
    ]

    place_option_element: List[str] = [
        identify_element_template.format('Tuỳ chọn'),
        identify_element_template.format('Thêm mới'),
        input_txt_element_template.format("Tiêu đề"),
        input_txt_element_template.format("Giá"),
        input_txt_element_template.format("Số lượng tối thiểu"),
        input_txt_element_template.format("Số lượng tối đa"),
        button_element_template.format('Xác nhận'),
    ]

    place_option_group_element: List[str] = [
        identify_element_template.format('Tuỳ chọn nhóm'),
        identify_element_template.format('Thêm mới'),
        input_txt_element_template.format("Tiêu đề"),
        "//input[@id='{}']".format("react-select-2-input"),
        input_txt_element_template.format("Số lượng tối thiểu"),
        input_txt_element_template.format("Số lượng tối đa"),
        button_element_template.format('Xác nhận'),
        button_element_template.format('Cập nhật')
    ]

    place_product_category_element: List[str] = [
        identify_element_template.format('Tạo danh mục'),
        "//div[text()='{}']".format('Tạo danh mục'),
        input_txt_element_template.format("Tên"),
        input_txt_element_template.format("Thứ tự"),
        button_element_template.format('Xác nhận'),
        button_element_template.format('Cập nhật')
    ]

    place_product_element: List[str] = [
        identify_element_template,
        "//p[text()='{}']/following::div[@class='icon-create-product']",
        input_cbb_element_template.format("Catalog"),
        input_txt_element_template.format("Tên"),
        input_txt_area_element_template.format("Mô tả"),
        input_cbb_element_template.format("Tuỳ chọn thêm"),
        input_txt_element_template.format("Thứ tự"),
        input_txt_element_template.format("Giá bán"),
        input_txt_element_template.format("Giá Sale"),
        input_txt_element_template.format("Số lượng tối thiểu"),
        input_txt_element_template.format("Số lượng tối đa"),
        input_txt_element_template.format("Phần trăm giảm giá"),
        identify_element_template.format("Upload hình ảnh"),
        "//input[@type='{}']".format("file"),
        button_element_template.format('Xác nhận')
    ]
