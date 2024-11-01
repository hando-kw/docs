import pandas as pd
from app.services.models import Category, Service


def run():
    print('Before querying')
    categories = Category.objects.values('name_en', 'name_ar', 'icon')
    services = Service.objects.values('name_en', 'name_ar', 'category__name_en', 'category__name_ar', 'icon')
    print('Queried successfully')
    
    print('Formatting data')
    categories_data = []
    for category in categories:
        category_data = {
            'Name EN': category['name_en'],
            'Name AR': category['name_ar'],
            'Icon Link': category['icon'],
        }
        categories_data.append(category_data)
    
    services_data = []
    for service in services:
        service_data = {
            'Name EN': service['name_en'],
            'Name AR': service['name_ar'],
            'Category EN': service['category__name_en'],
            'Category AR': service['category__name_ar'],
            'Icon Link': service['icon'],
        }
        services_data.append(service_data)
    
    print('Creating dataframes')
    categories_df = pd.DataFrame(categories_data)
    services_df = pd.DataFrame(services_data)
    
    # Adjust link column to be clickable in excel
    categories_df['Icon Link'] = categories_df['Icon Link'].apply(lambda x: f'=HYPERLINK("{x}")')
    services_df['Icon Link'] = services_df['Icon Link'].apply(lambda x: f'=HYPERLINK("{x}")')
    
    # Adjust column width
    print('Exporting data to excel sheet')
    with pd.ExcelWriter('categories_and_services.xlsx') as writer:
        categories_df.to_excel(writer, sheet_name='Categories', index=False)
        services_df.to_excel(writer, sheet_name='Services', index=False)
    
    print('Exported categories and services to categories_and_services.xlsx')