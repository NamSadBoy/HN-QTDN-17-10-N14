{
    'name': 'Quản lý Tính Lương',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Tự động tính lương dựa trên chấm công, phạt đi muộn và bảo hiểm',
    'depends': ['base', 'hr', 'nhan_su', 'cham_cong'],
    'data': [
        'security/ir.model.access.csv',
        'views/thuong_phat_views.xml',
        'views/phieu_luong_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}