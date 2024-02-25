from odoo import models, fields, api

class TrainingClassWizard(models.TransientModel):
    _name = 'training.class.wizard'
    _description = 'Training Class Wizard'

    name = fields.Char('Name', required=True)
    max_person_wizard = fields.Integer('Max Peserta')
    
    def action_change(self):
        records = self.env[self._context.get('active_model')].browse(
            self._context.get('active_ids'))
        new_values = {
            'name': self.name,
            'max_peserta': self.max_person_wizard
            }
        records.write(new_values)

    