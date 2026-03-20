from odoo import models, fields

class DonVi(models.Model):
    _inherit = 'hr.department'
    # Module hr mặc định đã đủ dùng, nhưng ta tạo file này để sẵn sàng mở rộng sau này (VD: thêm ngân sách phòng ban).