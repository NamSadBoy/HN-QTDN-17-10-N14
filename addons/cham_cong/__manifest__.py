{
    'name': 'Quản lý Chấm Công',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý ca làm, check-in/out, tính đi muộn về sớm và ngày lễ',
    'depends': ['base', 'hr', 'nhan_su'],
    'data': [
        'security/ir.model.access.csv',
        'views/kieu_ke_hoach_views.xml',
        'views/ke_hoach_views.xml',
        'views/ngay_le_views.xml',
        'views/cham_cong_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}