from odoo import models, fields

class QuanLyVanBan(models.Model):
    _name = 'quan_ly_van_ban.van_ban'
    _description = 'Quản lý Văn bản & Quyết định'

    name = fields.Char(string='Số hiệu / Tên văn bản', required=True)
    loai_van_ban = fields.Selection([
        ('hop_dong', 'Hợp đồng lao động'),
        ('quyet_dinh', 'Quyết định bổ nhiệm/tăng lương'),
        ('ky_luat', 'Biên bản kỷ luật'),
        ('khac', 'Tài liệu khác')
    ], string='Loại văn bản', required=True, default='hop_dong')

    # Liên kết với nhân viên nào
    employee_id = fields.Many2one('hr.employee', string='Nhân viên áp dụng', required=True)
    
    ngay_ban_hanh = fields.Date(string='Ngày ban hành', default=fields.Date.context_today)
    ngay_hieu_luc = fields.Date(string='Ngày hiệu lực')

    # Xử lý file đính kèm
    tep_dinh_kem = fields.Binary(string='Tệp đính kèm (PDF/Word/Ảnh)')
    file_name = fields.Char(string='Tên file') # Lưu tên gốc của file khi upload lên

    ghi_chu = fields.Text(string='Ghi chú nội dung')