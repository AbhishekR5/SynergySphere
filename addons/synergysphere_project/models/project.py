from odoo import models, fields, api

class SynergySphereProject(models.Model):
    _inherit = "project.project"

    synergy_progress = fields.Float(
        string="Progress (%)",
        compute="_compute_synergy_progress",
        store=True
    )

    @api.depends('task_ids.stage_id')
    def _compute_synergy_progress(self):
        for project in self:
            tasks = project.task_ids
            if tasks:
                done_tasks = tasks.filtered(lambda t: t.stage_id.fold)
                project.synergy_progress = (len(done_tasks) / len(tasks)) * 100
            else:
                project.synergy_progress = 0.0
