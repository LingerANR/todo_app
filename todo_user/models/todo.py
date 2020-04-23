# -*- coding: utf-8 -*-
#################################################################################
# Author : Real Systems (<www.realsystems.com.mx>)
# Copyright(c): 2019-Present Real Systems
#################################################################################
from odoo import models, fields, api, _
#from odoo import models, fields, api
class TodoTask(models.Model):
      _inherit = 'todo.task'

      user_id = fields.Many2one('res.users','Responsible')
      name = fields.Char(help="What needs to be done?")

      @api.model
      def do_clear_done(self,ids):
          domain =   [('is_done','=',True),
          '|',('user_id','=',self.env.uid),
          ('user_id','=',False)]
          done_recs= self.search(domain)

          done_recs.write({'active': False})
          return True
