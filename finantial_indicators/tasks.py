from .synthetic_index import get_synthetic_index
from finantial_indicators.celery import app

def async_calculate_synthetic_index(queryset):
    """
    Asyncronous task to calculate syntetic index
    """
    task_calculate_synthetic_index = calculate_synthetic_index.s(queryset=queryset)
    task_calculate_synthetic_index.set(queue='calculations')

    return task_calculate_synthetic_index

@app.task
def calculate_synthetic_index(queryset):
    return get_synthetic_index(queryset=queryset)