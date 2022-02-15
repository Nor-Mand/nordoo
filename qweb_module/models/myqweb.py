# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Myqweb(models.Model):
    _name = 'myqweb.form'
    _description = 'Formulario'

    name = fields.Char(string='Nombre')
    surnames = fields.Char(string='Apellidos')
    address = fields.Char(string='Direccion')
    phone = fields.Char(string='Telefono')
    email = fields.Char(string='Correo Electronico')
