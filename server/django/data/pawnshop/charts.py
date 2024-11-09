from .models import City, Graphics
from django.db.models import Sum
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
from django.core.files import File
import random

matplotlib.use('agg')

def get_chart():
    fig, ax = plt.subplots(figsize=(16, 9))
      
    fig.text(0.97, 0.93, 'ИКБО-03-22 Смирнов Даниил Анатольевич', fontsize = 30,
         color ='black', ha ='right')
    return fig, ax


def set_settings(ax):
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.grid(visible=True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)


def generate_line_chart(values, labels):
    fig, ax = get_chart()
    set_settings(ax)
    ax.plot(labels, values, marker='o', linestyle='-')
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.set_xticks(labels)
    ax.set_xticklabels(labels, rotation=90)
    
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer
 
    
def generate_bar_chart(values, labels):
    fig, ax = get_chart()   
    set_settings(ax)
    ax.barh(labels, values)
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer


def generate_pie_chart(values, labels):
    fig, ax = get_chart()
    explode = [random.random() * 0.5 for _ in range(len(values))]
    ax.pie(values, labels=labels, explode=explode, startangle=45)
    
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer
  

def generate_charts():
    data = City.objects.values('country').annotate(total=Sum('number')).distinct().all().order_by('country')
    if not data.exists():
        return None
    values = [item['total'] for item in data]
    labels = [item['country'] for item in data]
    charts = {
        'line': {
            'title': "Линейный график",
            'buffer': generate_line_chart(values, labels), 
        }, 
        'bar': {
            "title": "Стобчатая диаграмма",
            'buffer': generate_bar_chart(values, labels),
        }, 
        'pie': {
            "title": "Круговая диаграмма",
            'buffer': generate_pie_chart(values, labels)
        }
    }
    results = []
    for chart in charts:
        obj = Graphics.objects.create(
                name=charts[chart]['title'],
                file=File(
                    charts[chart]['buffer'], 
                    name=chart + '.png')
        )
        results.append(obj)
    return results
    
    