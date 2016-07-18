# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today Paulo Oneda.
#                            (<http://www.oneda.net.br>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Report for sale',
    'author': 'Paulo Ricardo',
    'category': 'Sales Management',
    'website': 'http://www.oneda.net.br',
    'version': '8.0.0.0.0',
    'sequence': 1,
    'depends': ['sale','l10n_br_sale','sale_layout', 'trust_installment_plans','l10n_br_sale_discount_total'],
    'data': [
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'auto_install': False
}
