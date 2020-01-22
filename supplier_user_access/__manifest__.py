# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Supplier Access",
    "category": "Security",
    "version": "12.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "depends": [
        "purchase_order_line_quant",
        "supplier_stock",
        "stock_view_adjust_oaw",
        "sale_order_line_quant",
        "website",
    ],
    "summary": """""",
    "description": """
    """,
    "data": [
        "security/supplier_security.xml",
        "security/base_security.xml",
        "security/ir.model.access.csv",
        "views/account_fiscal_year_views.xml",
        "views/enable_advance_search.xml",
        "views/product_category_views.xml",
        "views/product_product_views.xml",
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/sale_views.xml",
        "views/stock_move_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_quant_views.xml",
        "views/stock_views.xml",
        "views/supplier_stock_views.xml",
        "views/website_views.xml",
        "reports/account_invoice_reports.xml",
        "reports/common_templates.xml",
        "reports/sale_order_reports.xml",
        "reports/stock_picking_reports.xml",
        "reports/supplier_reports.xml",
    ],
    "qweb": ["static/src/xml/base.xml"],
    "installable": True,
}
