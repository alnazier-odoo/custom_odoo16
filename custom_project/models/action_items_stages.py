from odoo import fields, models, api


class ActionItemStages(models.Model):
    _name = 'action.items.stages'
    _description = 'Description'

    name = fields.Char()

    stage_name = fields.Char(
        string='Stage Name',
        required=False)